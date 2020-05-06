import domain
import datetime
from config import WORKLOAD_PERCENTAGE_LIMIT
from util.host_info import get_cpu_core_count

COMMAND = "ps -p %s -o %s"
DELIMITER = ","
PID_PARAM = "pid"
CPU_PARAM = "pcpu"


def collect_cluster_workload(processes, wm_db_connection, host_connection):
    metrics = get_metrics(host_connection, wm_db_connection)

    print(datetime.datetime.now(), ": process count = %s" % len(processes))

    processes_info = get_info_about_all_pg_processes(host_connection, processes, list(metrics.keys()))
    cluster_workload = calculate_cluster_workload(processes_info, metrics)

    print(datetime.datetime.now(), ': cluster workload = %s' % cluster_workload)

    return cluster_workload >= WORKLOAD_PERCENTAGE_LIMIT


def calculate_cluster_workload(processes_info, metrics):
    cluster_workload = 0.0
    for process in processes_info:
        cluster_workload += calculate_process_workload(process, metrics)
    return cluster_workload


def calculate_process_workload(process, metrics):
    pid = ''
    process_workload = 0
    for i in process.items():
        if i[0] == PID_PARAM:
            pid = i[1]
        else:
            try:
                process_workload += float(i[1]) * metrics[i[0]] / 100
            except Exception as error:
                print(error)
    print('pid %s workload is %s' % (pid, process_workload))
    return process_workload


def get_info_about_all_pg_processes(host_connection, processes, params):
    params.insert(0, PID_PARAM)
    ssh_stdin, ssh_stdout, ssh_stderr = host_connection.exec_command(COMMAND % (
        DELIMITER.join(map(lambda process: str(process.pid), processes)),
        DELIMITER.join(params)))
    ssh_stdout.readline()
    result_list = []
    for line in ssh_stdout:
        result_list.append(dict(zip(params, line.split())))
    return result_list


def metrics_to_dict(metrics):
    return dict(zip(
        map(lambda metric: metric['name'], metrics),
        map(lambda metric: metric['priority'], metrics)))


def get_metrics(host_connection, wm_db_connection):
    metrics = []
    try:
        cursor = wm_db_connection.cursor()
        cursor.execute(domain.query_constant.SELECT_METRICS)
        columns = cursor.description
        metrics = [{columns[index][0]: column for index, column in enumerate(value)} for value in cursor.fetchall()]
    except Exception as error:
        print(error)
    finally:
        if wm_db_connection:
            cursor.close()
    metrics = metrics_to_dict(metrics)
    crop_cpu_metric(host_connection, metrics)
    return metrics


def crop_cpu_metric(host_connection, metrics):
    if CPU_PARAM in metrics:
        metrics[CPU_PARAM] = metrics.get('pcpu') / int(get_cpu_core_count(host_connection))

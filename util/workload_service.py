import domain
import datetime
from config import WORKLOAD_PERCENTAGE_LIMIT

COMMAND = "ps -p %s -o %s"


def collect_cluster_workload(processes, wm_db_connection, host_connection):
    metrics = get_metrics(wm_db_connection)
    print(datetime.datetime.now(), ": process count = %s" % len(processes))

    processes_info = get_info_about_all_pg_processes(host_connection, processes,
                                                     list(map(lambda metric: metric['name'], metrics)))

    cluster_workload = cluster_workload = calculate_cluster_workload(processes_info, metrics_to_dict(metrics))

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
        if i[0] == 'pid':
            pid = i[1]
        else:
            try:
                process_workload += float(i[1]) * metrics[i[0]] / 100
            except Exception as error:
                print(error)
    print('pid %s workload is %s' % (pid, process_workload))
    return process_workload


def get_info_about_all_pg_processes(host_connection, processes, params):
    params.insert(0, 'pid')
    ssh_stdin, ssh_stdout, ssh_stderr = host_connection.exec_command(COMMAND % (
        ','.join(map(lambda process: str(process.pid), processes)),
        ','.join(params)))
    ssh_stdout.readline()
    result_list = []
    for line in ssh_stdout:
        result_list.append(dict(zip(params, line.split())))
    return result_list


def metrics_to_dict(metrics):
    return dict(zip(
        map(lambda metric: metric['name'], metrics),
        map(lambda metric: metric['priority'], metrics)))


def get_metrics(wm_db_connection):
    try:
        cursor = wm_db_connection.cursor()
        cursor.execute(domain.query_constant.SELECT_METRICS)
        columns = cursor.description
        return [{columns[index][0]: column for index, column in enumerate(value)} for value in cursor.fetchall()]
    except Exception as error:
        print(error)
    finally:
        if wm_db_connection:
            cursor.close()

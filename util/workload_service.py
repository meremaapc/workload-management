import datetime

from config import CPU_PARAM, RAM_PARAM, PID_PARAM
from connection.workload_managment_db import get_metrics, store_current_workload
from util.host_info import get_cpu_core_count, get_ram_load

COMMAND = "ps -p %s -o %s"
DELIMITER = ","


def collect_cluster_workload(processes, wm_db_connection, host_connection):
    metrics = get_metrics(wm_db_connection)

    print(datetime.datetime.now(), ": process count = %s" % len(processes))

    processes_info = get_info_about_all_pg_processes(host_connection, processes, list(map(lambda metric: metric.name, metrics)))
    cluster_workload = calculate_cluster_workload(host_connection, processes_info, metrics)

    print(datetime.datetime.now(), ': cluster workload = %s' % cluster_workload)

    limit_workload = calculate_workload_percentage_limit(metrics)
    store_current_workload(wm_db_connection, cluster_workload)

    return cluster_workload >= limit_workload


def calculate_workload_percentage_limit(metrics):
    workload_limit = 0
    for metric in metrics:
        workload_limit += metric.threshold * metric.priority / 100
    return workload_limit


def calculate_cluster_workload(host_connection, processes_info, metrics):
    ram_load = get_ram_load(host_connection)
    cpu_load = sum(map(lambda item: float(item[CPU_PARAM]), processes_info))
    metrics_dict = {CPU_PARAM: cpu_load, RAM_PARAM: ram_load}
    return calculate_process_workload(metrics_dict, metrics)


def calculate_process_workload(metric_value, metrics):
    workload = 0
    for metric in metrics:
        workload += metric_value[metric.name] * metric.priority / 100
    return workload


def get_info_about_all_pg_processes(host_connection, processes, params):
    params.insert(0, PID_PARAM)
    ssh_stdin, ssh_stdout, ssh_stderr = host_connection.exec_command(COMMAND % (
        DELIMITER.join(map(lambda process: str(process.pid), processes)),
        DELIMITER.join(params)))
    ssh_stdout.readline()
    result_list = []
    for line in ssh_stdout:
        result_list.append(dict(zip(params, line.split())))
    crop_cpu_metric(host_connection, result_list)
    return result_list


def crop_cpu_metric(host_connection, metrics):
    cpu_cores = int(get_cpu_core_count(host_connection))
    for metric in metrics:
        metric[CPU_PARAM] = float(metric[CPU_PARAM]) / cpu_cores

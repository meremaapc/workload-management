from connection import workload_managment_db
from util.host_info import get_ram_load
from util.workload_service import get_info_about_all_pg_processes, get_metrics


def collect_statistic(wm_db_connection, host_connection, processes):
    metrics = get_metrics(wm_db_connection)
    processes_info = get_info_about_all_pg_processes(host_connection, processes, list(map(lambda metric: metric['name'], metrics)))
    cpu_usage = sum(map(lambda item: float(item['pcpu']), processes_info))
    ram_usage = get_ram_load(host_connection)
    print('CPU load = %s' % cpu_usage)
    print('RAM load = %s' % ram_usage)
    workload_managment_db.store_cluster_statistic(wm_db_connection, cpu_usage, ram_usage)

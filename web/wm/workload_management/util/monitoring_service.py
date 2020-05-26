from web.wm.workload_management.connection import workload_managment_db
from web.wm.workload_management.connection.workload_managment_db import get_metrics
from web.wm.workload_management.util.host_info import get_ram_load
from web.wm.workload_management.util.workload_service import get_info_about_all_pg_processes


def collect_statistic(wm_db_connection, host_connection, processes):
    metrics = get_metrics(wm_db_connection)
    processes_info = get_info_about_all_pg_processes(host_connection, processes, list(map(lambda metric: metric.name, metrics)))
    cpu_usage = sum(map(lambda item: float(item['pcpu']), processes_info))
    ram_usage = get_ram_load(host_connection)
    print('CPU load = %s' % cpu_usage)
    print('RAM load = %s' % ram_usage)
    workload_managment_db.store_cluster_statistic(wm_db_connection, cpu_usage, ram_usage)

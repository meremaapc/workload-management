import util.host_info
from connection import workload_managment_db
from util.host_info import get_ram_load
from util.workload_service import get_info_about_all_pg_processes, get_metrics


def collect_statistic(wm_db_connection, host_connection, processes):
    metrics = get_metrics(host_connection, wm_db_connection)
    processes_info = get_info_about_all_pg_processes(host_connection, processes, list(metrics.keys()))
    cpu_usage = sum(map(lambda item: float(item['pcpu']), processes_info)) / int(
        util.host_info.get_cpu_core_count(host_connection))
    workload_managment_db.store_cluster_statistic(wm_db_connection, cpu_usage, get_ram_load(host_connection))

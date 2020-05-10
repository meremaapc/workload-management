import connection.workload_managment_db_connection
import util.host_info


def collect_statistic(conn, processes, host_conn):
    cpu_usage = sum(map(lambda item: float(item['pcpu']), processes)) / int(
        util.host_info.get_cpu_core_count(host_conn))
    ram_usage = sum(map(lambda item: float(item['pmem']), processes))
    connection.workload_managment_db_connection.store_cluster_statistic(conn, cpu_usage, ram_usage)

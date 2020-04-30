import domain.query_constant
from util.workload_service import calculate_process_workload, get_metrics


def select_resource_intensive_process(processes, host_connection, wm_db_connection):
    metrics = get_metrics(wm_db_connection)
    # todo ?maybe need kill recent process
    result = max(zip(
        map(lambda process: calculate_process_workload(process, metrics, host_connection), processes),
        map(lambda process: process.pid, processes))
    )
    return result[1]


def kill_process_by_pid(pid, conn):
    try:
        cursor = conn.cursor()
        cursor.execute(domain.query_constant.PG_CANCEL_BACKEND % pid)
        print("Killed pid", pid, sep=" ")
    except Exception as error:
        print(error)
    finally:
        if conn and cursor:
            cursor.close()

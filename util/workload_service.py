import domain
from config import WORKLOAD_PERCENTAGE_LIMIT

COMMAND = "ps -p %s -o %s"


def collect_cluster_workload(processes, wm_db_connection, host_connection):
    print("active processes count = %s" % len(processes))
    metrics = get_metrics(wm_db_connection)
    cluster_workload = 0
    for process in processes:
        cluster_workload += calculate_process_workload(process, metrics, host_connection)
    print("cluster workload %s" % cluster_workload)
    return cluster_workload >= WORKLOAD_PERCENTAGE_LIMIT


def calculate_process_workload(process, metrics, host_connection):
    process_workload = 0.0
    for metric in metrics:
        param = metric['name']
        priority = metric['priority']
        ssh_stdin, ssh_stdout, ssh_stderr = host_connection.exec_command(COMMAND % (process.pid, param))
        # skip the row with the column name
        ssh_stdout.readline()
        param_res = ssh_stdout.readline().strip()
        process_workload += float(param_res) * priority / 100
    # print(str(process.pid) + ' workload: ' + str(process_workload))
    return process_workload


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

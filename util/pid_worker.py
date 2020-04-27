def select_resource_intensive_process(processes):
    # todo select pid and return
    for k in processes:
        print(k.pid)
    print("Selecting worst process..")
    return 1


KILL_PG_PROCESS = "SELECT pg_cancel_backend(%s)"


def kill_process_by_pid(pid, conn):
    try:
        cursor = conn.cursor()
        cursor.execute(KILL_PG_PROCESS % pid)
        print("Killed pid", pid, sep=" ")
    except Exception as error:
        print(error)
    finally:
        if conn and cursor:
            cursor.close()

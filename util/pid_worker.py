def select_resource_intensive_process(processes):
    # todo select pid and return
    for k in processes:
        print(k.pid)
    print("Selecting worst process..")
    return 1


def kill_process_by_pid(pid):
    # todo kill
    print("Kill pid", pid, sep=" ")


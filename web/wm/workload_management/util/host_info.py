CORE_COMMAND = 'grep -c ^processor /proc/cpuinfo'
TOP_COMMAND = 'top -b -n1 | grep \'KiB Mem*\''


def get_cpu_core_count(conn):
    ssh_stdin, ssh_stdout, ssh_stderr = conn.exec_command(CORE_COMMAND)
    return ssh_stdout.readline()


def get_ram_load(conn):
    ssh_stdin, ssh_stdout, ssh_stderr = conn.exec_command(TOP_COMMAND)
    result = list(map(str, ssh_stdout.readline().split()))
    return int(result[7]) / int(result[3]) * 100

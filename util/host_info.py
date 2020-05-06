COMMAND = 'grep -c ^processor /proc/cpuinfo'


def get_cpu_core_count(conn):
    ssh_stdin, ssh_stdout, ssh_stderr = conn.exec_command(COMMAND)
    return ssh_stdout.readline()

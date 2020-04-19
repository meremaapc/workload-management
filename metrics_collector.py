PREFIX = "%"
DELIMITER = ","
COMMAND = "ps -p %s -o %s"


def metric_transform(metrics):
    return DELIMITER.join(map(str, metrics))


def process_transform(processes):
    return DELIMITER.join(map(str, processes))


def collect(client, processes, metrics):
    processes = process_transform(processes)
    metrics = metric_transform(metrics)
    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(COMMAND % (processes, metrics))
    for line in iter(ssh_stdout.readline, ""):
        print(line, end="")

MAIN_DB_CONFIG = {
    'host': 'ec2-54-242-190-240.compute-1.amazonaws.com',
    'user': 'postgres',
    'port': '5432',
    'dbname': 'postgres',
    'password': 'postgres'
}

WM_DB_CONFIG = {
    'host': 'ec2-54-242-190-240.compute-1.amazonaws.com',
    'user': 'postgres',
    'port': '5432',
    'dbname': 'workload_management',
    'password': 'postgres'
}

REMOTE_SERVER_CONFIG = {
    'host': 'ec2-54-242-190-240.compute-1.amazonaws.com',
    'user': 'ubuntu',
    'port': '22',
    'key': 'course_work_key.pem'
}


RECALCULATE_SYSTEM_LOAD_PAUSE_SEC = 45
REQUEST_PAUSE_SEC = 45
MONITORING_PAUSE = 30

HINT = '/*backend query*/'
CLIENT_BACKEND = 'client backend'
PID_PARAM = "pid"
CPU_PARAM = "pcpu"
RAM_PARAM = "pmem"

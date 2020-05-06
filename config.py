DB_CONFIG = {
    'host': 'ec2-54-165-11-20.compute-1.amazonaws.com',
    'user': 'postgres',
    'port': '5432',
    'dbname': 'postgres',
    'password': 'postgres'
}

WM_DB_CONFIG = {
    'host': 'ec2-54-165-11-20.compute-1.amazonaws.com',
    'user': 'postgres',
    'port': '5432',
    'dbname': 'workload_management',
    'password': 'postgres'
}

REMOTE_SERVER_CONFIG = {
    'host': 'ec2-54-165-11-20.compute-1.amazonaws.com',
    'user': 'ubuntu',
    'port': '22',
    'key': 'course_work_key.pem'
}


RECALCULATE_SYSTEM_LOAD_PAUSE_SEC = 30
REQUEST_PAUSE_SEC = 30

WORKLOAD_PERCENTAGE_LIMIT = 75

CPU_CORES = 1

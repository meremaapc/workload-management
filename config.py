MAIN_DB_CONFIG = {
    'host': 'ec2-52-90-104-149.compute-1.amazonaws.com',
    'user': 'postgres',
    'port': '5432',
    'dbname': 'postgres',
    'password': 'postgres'
}

WM_DB_CONFIG = {
    'host': 'ec2-52-90-104-149.compute-1.amazonaws.com',
    'user': 'postgres',
    'port': '5432',
    'dbname': 'workload_management',
    'password': 'postgres'
}

REMOTE_SERVER_CONFIG = {
    'host': 'ec2-52-90-104-149.compute-1.amazonaws.com',
    'user': 'ubuntu',
    'port': '22',
    'key': 'course_work_key.pem'
}


RECALCULATE_SYSTEM_LOAD_PAUSE_SEC = 45
REQUEST_PAUSE_SEC = 45
MONITORING_PAUSE = 30

WORKLOAD_PERCENTAGE_LIMIT = 11

HINT = '/*backend query*/'
CLIENT_BACKEND = 'client backend'

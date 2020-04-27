DB_CONFIG = {
    'host': 'ec2-54-152-228-115.compute-1.amazonaws.com',
    'user': 'postgres',
    'port': '5432',
    'dbname': 'test',
    'password': 'postgres'
}

REMOTE_SERVER_CONFIG = {
    'host': 'ec2-54-152-228-115.compute-1.amazonaws.com',
    'user': 'ubuntu',
    'port': '22',
    'key': 'course_work_key.pem'
}

# replace to db
METRICS = ["pid", "%cpu", "%mem"]

RECALCULATE_SYSTEM_LOAD_PAUSE_SEC = 30
REQUEST_PAUSE_SEC = 30

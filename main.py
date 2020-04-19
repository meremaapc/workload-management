import db_connection
import remote_server_connection
import metrics_collector

result = db_connection.pg_stat_activity()
client = remote_server_connection.host_connect()

processes = map(lambda x: x.pid, result)
metrics = ["pid", "%cpu", "%mem"]

metrics_collector.collect(client, processes, metrics)
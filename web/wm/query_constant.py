SELECT_PG_STAT_ACTIVITY = 'SELECT * FROM pg_stat_activity'
PG_CANCEL_BACKEND = 'SELECT pg_cancel_backend(%s)'
SELECT_METRICS = 'SELECT * FROM wm.metrics'
SELECT_LAST_HOUR_WORKLOAD = "SELECT * FROM wm.workload  WHERE date >= current_timestamp - interval '1 hour'"
SELECT_LAST_HOUR_CLUSTER_STATISTIC = "SELECT * FROM wm.cluster_statistic  WHERE date >= current_timestamp - interval '1 hour'"
CREATE_DATABASE = 'SELECT create_workload_management_database(%s, %s);'
INSERT_STATISTIC = 'INSERT INTO wm.cluster_statistic(cpu_usage, ram_usage, date) VALUES (%s, %s, current_timestamp)'
INSERT_WORKLOAD = 'INSERT INTO wm.workload(workload_value) VALUES(%s)'
UPDATE_METRIC = 'UPDATE wm.metrics SET threshold = %s, priority = %s WHERE name = %s'

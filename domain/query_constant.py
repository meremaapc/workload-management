SELECT_PG_STAT_ACTIVITY = 'SELECT * FROM pg_stat_activity'
PG_CANCEL_BACKEND = 'SELECT pg_cancel_backend(%s)'
SELECT_METRICS = 'SELECT * FROM wm.metrics'
CREATE_DATABASE = 'SELECT create_workload_management_database(%s, %s);'
INSERT_STATISTIC = "INSERT INTO wm.cluster_statistic(cpu_usage, ram_usage, date) VALUES (%s, %s, current_timestamp)"

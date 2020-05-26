from django.db import connection

# from web.wm import query_constant
from wm.models import Metric

from wm import query_constant


def get_metrics_info():
    metrics = []
    try:
        cursor = connection.cursor()
        cursor.execute(query_constant.SELECT_METRICS)
        for value in cursor.fetchall():
            metric = Metric(value[0], value[1], value[2], value[3])
            metrics.append(metric)
    except Exception as error:
        print(error)
    finally:
        cursor.close()
    return metrics


def update_metrics_info(metrics):
    try:
        cursor = connection.cursor()
        for metric in metrics:
            cursor.execute(query_constant.UPDATE_METRIC, (metric.threshold, metric.priority, metric.name))
    except Exception as error:
        print(error)
    finally:
        cursor.close()
    return metrics

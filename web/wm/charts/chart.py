import io

from django.db import connection
from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.dates import DateFormatter
from matplotlib.figure import Figure
from wm import query_constant
from wm.models import Workload, Cluster_Statistic


def get_cluster_statistic():
    values = []
    try:
        cursor = connection.cursor()
        cursor.execute(query_constant.SELECT_LAST_HOUR_CLUSTER_STATISTIC)
        for value in cursor.fetchall():
            statistic = Cluster_Statistic(value[0], value[1], value[2])
            values.append(statistic)
    except Exception as error:
        print(error)
    finally:
        cursor.close()
    return values


def get_workload_values():
    values = []
    try:
        cursor = connection.cursor()
        cursor.execute(query_constant.SELECT_LAST_HOUR_WORKLOAD)
        for value in cursor.fetchall():
            workload = Workload(value[0], value[1], value[2])
            values.append(workload)
    except Exception as error:
        print(error)
    finally:
        cursor.close()
    return values


def workload():
    values = get_workload_values()
    x = []
    y = []
    for workload in values:
        y.append(workload.value)
        x.append(workload.date)
    return graphic_creation(x, y)


def cpu():
    values = get_cluster_statistic()
    x = []
    y = []
    for statistic in values:
        y.append(statistic.cpu_usage)
        x.append(statistic.date)
    return graphic_creation(x, y)


def ram():
    values = get_cluster_statistic()
    x = []
    y = []
    for statistic in values:
        y.append(statistic.ram_usage)
        x.append(statistic.date)
    return graphic_creation(x, y)


def graphic_creation(x, y):
    figure = Figure()
    ax = figure.add_subplot(111)
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter("%H:%M:%S"))
    ax.set_ylim([max(0, min(y) - 5), min(max(y) + 5, 100)])
    ax.set_xlim([min(x), max((x))])
    figure.autofmt_xdate()
    canvas = FigureCanvas(figure)
    buf = io.BytesIO()
    canvas.print_png(buf)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    return response

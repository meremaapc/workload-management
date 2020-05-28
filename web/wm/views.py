from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .charts import chart
from .metrics import metrics_action
from .metrics.metrics_action import update_metrics_info
from .models import Metric


def get_metrics(request):
    metrics = metrics_action.get_metrics_info()
    result = dict()
    for metric in metrics:
        if metric.name == 'pcpu':
            result['cpu_priority'] = metric.priority
            result['cpu_threshold'] = metric.threshold
        if metric.name == 'pmem':
            result['ram_priority'] = metric.priority
            result['ram_threshold'] = metric.threshold
    return render(request, 'metric_info.html', result)


def get_update_page(request):
    return render(request, 'metric_info_upd.html')


@csrf_exempt
def put_metrics(request):
    metrics = {
        Metric(None, 'pcpu', request.POST['cpu_threshold'], request.POST['cpu_priority']),
        Metric(None, 'pmem', request.POST['ram_threshold'], request.POST['ram_priority'])
    }
    update_metrics_info(metrics)
    return redirect('/wm/metrics')


def workload_charts(request):
    return chart.workload()


def cpu_charts(request):
    return chart.cpu()


def ram_charts(request):
    return chart.ram()

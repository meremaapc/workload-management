from django.conf.urls import url

from . import views

app_name = 'wm'

urlpatterns = [
    url(r'^metrics', views.get_metrics),
    url(r'^upd_metrics', views.put_metrics),
    url(r'^update_metrics', views.get_update_page),
    url(r'^charts/workload.png$', views.workload_charts),
    url(r'^charts/cpu.png$', views.cpu_charts),
    url(r'^charts/ram.png$', views.ram_charts)
]
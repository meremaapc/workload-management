from django.conf.urls import url

from . import views

app_name = 'wm'

urlpatterns = [
    url(r'^metrics', views.get_metrics),
    url(r'^upd_metrics', views.put_metrics),
    url(r'^update_metrics', views.get_update_page)
    # url(r'^$', views.workload_chart, name = 'demo')
]
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^farmers$', views.create),
    url(r'^farmers/destroy/(?P<id>\d+)$', views.destroy)

]

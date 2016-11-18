from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.postanalysis, name='postanalysis'),
    url(r'^postajax', views.postanalysis, name='postajax'),
    
]

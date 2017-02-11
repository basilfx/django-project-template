from django.conf.urls import include, url

from my_project.my_app.views import index

urlpatterns = [
    url(r'^$', index),
]

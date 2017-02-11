from django.conf.urls import url, include

urlpatterns = [
    url(r'', include('my_project.my_app.urls')),
]

from django.urls import include, re_path

import debug_toolbar
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    re_path(r'', include('my_project.my_app.urls')),
    path('__debug__/', include(debug_toolbar.urls)),

]

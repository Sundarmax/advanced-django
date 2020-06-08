from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),

]

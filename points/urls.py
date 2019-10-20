from django.contrib import admin
from django.urls import path, include
import points.views
import points.urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('<slug:house_name>', points.views.housepage, name='housepage'),
]

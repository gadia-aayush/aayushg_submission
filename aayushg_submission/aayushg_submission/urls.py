from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from survey.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('survey/', Survey.as_view())
]

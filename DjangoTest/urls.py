from django.contrib import admin
from django.urls import path
from FormApp import views as appv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appv.index),
    path('/meds', appv.database),
]

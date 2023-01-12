"""APIStorage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from storage_sensors.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("get_all_types/", SensorsTypeAPIView.as_view()),
    path("get_sensors_name/", SensorsAPIView.as_view()),
    path("send_notification/", NotificationAPIView.as_view()),
    path("find_employee/", EmployeeAPIView.as_view()),
    path("positions/", PositionAPIView.as_view()),
    path("schedule/", ScheduleAPIView.as_view()),
    path("fullschedule/", FullScheduleAPIView.as_view()),
    path("machine_name/", MachineAPIView.as_view()),
    path("get_sensors_data_from_type/", SensorsDataAPIView.as_view()),
    path("get_sensors_data_from_machine/", SensorsDataMachineAPIView.as_view()),
    path("get_alert/", PredictionAPIView.as_view()),
]

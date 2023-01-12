from rest_framework import serializers
from .models import *
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "first_name", "last_name", "telegram_id", "position", "work_schedule", "vacation", "login")

class SensorsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorsData
        fields = ("value", "date")

class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = ("name", "type", "machine")

class SensorsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorsType
        fields = '__all__'

class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class MachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machines
        fields = '__all__'

class Area_of_ResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Area_of_Responsibility
        fields = '__all__'

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ("id", "type_alert", "description", "datetime", "detail")       
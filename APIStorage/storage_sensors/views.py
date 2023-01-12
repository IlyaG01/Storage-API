from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from .bot import send_message_to_employee
import json
import datetime
# from .handler_request import get_data
# Create your views here.

def correct_machine(request):
        all_machines = Machines.objects.all()
        types = []
        [types.append(j.name) for j in all_machines]
        try:
            if request.data["machine"] in types:
                response = True
            else:
                response = False
        except KeyError:
            response = False
        return response

def correct_type(request):
        all_types = SensorsType.objects.all()
        types = []
        [types.append(j.name) for j in all_types]
        try:
            if request.data["data_type"] in types:
                response = True
            else:
                response = False

        except KeyError:
            response = False
        return response

def correct_sensor_name(request):
        all_sensor_name = Sensors.objects.all()
        types = []
        [types.append(j.name) for j in all_sensor_name]
        try:
            if request.data["name"] in types:
                response = True
            else:
                response = False
        except KeyError:
            response = False
        return response

def correct_login(request):
        all_employees = Employee.objects.all()
        types = []
        [types.append(j.login) for j in all_employees]
        try:
            if request.data["login"] in types:
                response = True
            else:
                response = False
        except KeyError:
            response = False
        return response

def correct_employee_name(request):
        all_employees = Employee.objects.all()
        first_name = []
        last_name = []
        try:
            f_user = str(request.data["to_whom"]).split()[0]
            l_user = str(request.data["to_whom"]).split()[1]
            [first_name.append(j.first_name) for j in all_employees]
            [last_name.append(i.last_name) for i in all_employees]
            if f_user in first_name and l_user in last_name:
                response = True
        except KeyError:
            response = False
        return response




class SensorsDataAPIView(APIView):
   
    def post(self, request):
        if request.data and correct_type(request):
            result_time = datetime.datetime.strptime(request.data["date_from"][:-5], '%Y-%m-%dT%H:%M:%S')
            result_time_end = datetime.datetime.strptime(request.data["date_to"][:-5], '%Y-%m-%dT%H:%M:%S')
            sensors_id = SensorsType.objects.filter(name = request.data["data_type"])[0].id
            print(sensors_id)
            w =[]
            names = Sensors.objects.filter(type = sensors_id)
            for i in names:
                sensor_data = {}
                s1 = SensorsData.objects.filter(sensor = i.id, date__range = [result_time, result_time_end])
                w1 = SensorsDataSerializer(s1, many = True).data
                sensor_data["sensor_name"] = i.name
                sensor_data["values"] = w1
                w.append(sensor_data)
        else:
            w=[]
        return Response(w)

class SensorsDataMachineAPIView(APIView):
    def post(self, request):
        if request.data and correct_machine(request):
            result_time = datetime.datetime.strptime(request.data["date_from"][:-5], '%Y-%m-%dT%H:%M:%S')
            result_time_end = datetime.datetime.strptime(request.data["date_to"][:-5], '%Y-%m-%dT%H:%M:%S')
            machine_id = Machines.objects.filter(name = request.data["machine"])[0].id
            w =[]
            names = Sensors.objects.filter(machine = machine_id)
            for i in names:
                sensor_data = {}
                s1 = SensorsData.objects.filter(sensor = i.id, date__range = [result_time, result_time_end])
                w1 = SensorsDataSerializer(s1, many = True).data
                sensor_data["sensor_name"] = i.name
                sensor_data["values"] = w1
                w.append(sensor_data)
        else:
            w=[]
        return Response(w)

class SensorsTypeAPIView(APIView):
    def get(self, request):
        w = SensorsType.objects.all()
        types = []
        [types.append(j.name) for j in w]
        return Response(types)
    
    def post(self, request):
        serializer = SensorsTypeSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})



class SensorsAPIView(APIView):
    
    def get(self, request):
        array = []
        a = SensorsSerializer(Sensors.objects.all(), many = True).data
        for i in a:
            test = json.loads(json.dumps(i))
            test["type"] = str(SensorsType.objects.filter(id = test["type"])[0].name)
            test["machine"] = str(Machines.objects.filter(id = test["machine"])[0].name)
            array.append(test)
        return Response(array)
    
    def post(self, request):
        array = []
        a = SensorsSerializer(Sensors.objects.all(), many = True).data
        if correct_type(request):
            type_id = SensorsType.objects.filter(name = request.data["data_type"])[0].id
            w = Sensors.objects.filter(type = type_id)
            [array.append({"name_sensor": str(j.name), "machine": str(j.machine)}) for j in w]
            return Response(array)
        
        if correct_machine(request):
            machine_id = Machines.objects.filter(name = request.data["machine"])[0].id
            w = Sensors.objects.filter(machine = machine_id)
            [array.append({"name_sensor": str(j.name), "data_type": str(j.type)}) for j in w]
            return Response(array)
        
        if correct_sensor_name(request):
            j = Sensors.objects.filter(name = request.data["name"])[0]
            w = {}
            w["type"] = j.type.name
            w["machine"] = j.machine.name
            return Response(w)
        
        return Response(array)

        


class EmployeeAPIView(APIView):
    def get(self, request):
        if request.data:
            if correct_login(request):
                user = Employee.objects.filter(login = str(request.data["login"]))[0]
                position = user.position.name
                work_schedule = user.work_schedule.name
                w = EmployeeSerializer(Employee.objects.filter(id = user.id), many = True).data
                t1 = json.loads(json.dumps(w[0]))
                t1["position"] = position
                t1["work_schedule"] = work_schedule
                w = t1
            else:
                w=[]
        else:
            w = Employee.objects.all()
            all = []
            for j in w:
                w1 = EmployeeSerializer(j).data
                w1["position"] = j.position.name
                w1["work_schedule"] = j.work_schedule.name
                all.append(w1)

            w = all
        return Response(w)
    
    def post(self, request):
        serializer = EmployeeSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


class PositionAPIView(APIView):
    def get(self, request):
        w = Positions.objects.all()
        types = []
        [types.append(j.name) for j in w]
        return Response(types)
    
    def post(self, request):
        serializer = PositionsSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


class ScheduleAPIView(APIView):
    def get(self, request):
        w = Schedule.objects.all()
        types = []
        [types.append(j.name) for j in w]
        return Response(types)
    
    def post(self, request):
        serializer = ScheduleSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


class MachineAPIView(APIView):
    def get(self, request):
        w = Machines.objects.all()
        types = []
        [types.append(j.name) for j in w]
        return Response(types)
    
    def post(self, request):
        serializer = MachinesSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})



class NotificationAPIView(APIView):
    def get(self, request):
        w = Employee.objects.all()
        all = []
        for j in w:
            all.append(str(j.first_name + " " + j.last_name))
            print(all)
        w = all
        return Response(w)

    def post(self, request):
        if request.data and correct_employee_name(request):
            user_id = Employee.objects.filter(first_name = str(request.data["to_whom"]).split()[0], last_name = str(request.data["to_whom"]).split()[1])[0].telegram_id
            send_message_to_employee(user_id, request.data["from_whom"], request.data["text_message"])
            return Response({'post': 'successfully'})
        else:
            return Response({'post': 'unsuccessfully'})


class FullScheduleAPIView(APIView):
    def get(self, request):
        array = []
        a = Area_of_ResponsibilitySerializer(Area_of_Responsibility.objects.all(), many = True).data
        for i in a:
            w = {}
            w["id"] = i["id"]
            employee = Employee.objects.filter(id = i["employee_id"])[0]
            w["name"] = str(employee.first_name) + " " + str(employee.last_name)
            w["work_schedule"] = employee.work_schedule.name
            w["machine"] = Machines.objects.filter(id = i["machine_id"])[0].name
            array.append(w)
        return Response(array)
    
    def post(self, request):
        if correct_employee_name(request):
            w = {}
            user_id = Employee.objects.filter(first_name = str(request.data["name"]).split()[0], last_name = str(request.data["name"]).split()[1])[0]
            machine = Machines.objects.filter(id = Area_of_Responsibility.objects.filter(employee_id = user_id.id)[0].id)[0]
            w["name"] = str(user_id.first_name) + " " + str(user_id.last_name)
            w["work_schedule"] = user_id.work_schedule.name
            w["machine"] = machine.name
        else:
            w={}
        return Response(w)
        


class PredictionAPIView(APIView):
    def post(self, request):
        result_time = datetime.datetime.strptime(request.data["date_from"][:-5], '%Y-%m-%dT%H:%M:%S')
        result_time_end = datetime.datetime.strptime(request.data["date_to"][:-5], '%Y-%m-%dT%H:%M:%S')
        s1 = Prediction.objects.filter(datetime__range = [result_time, result_time_end])
        w1=[]
        for i in s1:
            print(i)
            # w1 = PredictionSerializer(i, many = True).data
            w1.append(i)
            print(w1)
        w = PredictionSerializer(w1, many = True).data
        print(len(w))
        return Response(w)
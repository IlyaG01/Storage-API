from django.db import models

# Create your models here.

class Area_of_Responsibility(models.Model):
    employee_id = models.ForeignKey('Employee', on_delete=models.PROTECT, null = True)
    machine_id = models.ForeignKey('Machines', on_delete=models.PROTECT, null = True)

    def __str__(self):
        return self.employee_id


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    telegram_id = models.CharField(max_length=20)
    position = models.ForeignKey('Positions', on_delete=models.PROTECT, null = True)
    work_schedule = models.ForeignKey('Schedule', on_delete=models.PROTECT, null = True)
    vacation = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name

class Positions(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class SensorsData(models.Model):
    value = models.FloatField()
    date = models.DateTimeField(auto_now_add = True)
    sensor = models.ForeignKey('Sensors', on_delete=models.PROTECT, null = True)

    def __str__(self):
        return self.value


class Sensors(models.Model):
    name = models.CharField(max_length=10)
    type = models.ForeignKey('SensorsType', on_delete=models.PROTECT, null=True)
    machine = models.ForeignKey('Machines', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

class SensorsType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Machines(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Prediction(models.Model):

    type_alert = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add = True)
    detail = models.TextField()

    def __str__(self):
        return self.description
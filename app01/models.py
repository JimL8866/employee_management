from django.db import models

# Create your models here.
class Department(models.Model):
    """
    department table
    """
    title = models.CharField(verbose_name="title of Dep", max_length=32)
    
    


class EmployeeInfo(models.Model):
    """
    employee table
    """
    f_name = models.CharField(verbose_name="first name", max_length=25)
    l_name = models.CharField(verbose_name="last name", max_length=25)
    password = models.CharField(verbose_name="password used", max_length=30)
    age = models.IntegerField(verbose_name="age of employee")
    account = models.DecimalField(verbose_name="salary balance", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="time for account created")
    dep = models. ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)
    gender_choices = (
        (1, "male"),
        (2, "female"),  
    )
    gender = models.SmallIntegerField(verbose_name="gender", choices=gender_choices)
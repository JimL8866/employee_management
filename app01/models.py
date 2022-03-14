from django.db import models

class Department(models.Model):
    """
    department table
    """
    name = models.CharField(verbose_name="title of Dep", max_length=32)
    
    def __str__(self): 
        return self.name
        
    
    


class EmployeeInfo(models.Model):
    """
    employee table
    """
    f_name = models.CharField(verbose_name="First Name", max_length=25)
    l_name = models.CharField(verbose_name="Last Name", max_length=25)
    password = models.CharField(verbose_name="Password", max_length=30)
    age = models.IntegerField(verbose_name="Age")
    account = models.DecimalField(verbose_name="Account", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="Date of Create")
    
    
    
    # constraint
    # to related to table
    # to_field realted to column
    # auto create dep_id
    dep = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Department")
    gender_choices = (
        (1, "male"),
        (2, "female"),  
    )
    gender = models.SmallIntegerField(verbose_name="Gender", choices=gender_choices)
from django import forms
from django.forms import ModelForm
from django.shortcuts import render, HttpResponse, redirect
from app01 import models

# Create your views here.
def dep_list(request):
    """
    department list
    """
    data_list = models.Department.objects.all()
    
    return render(request, "dep_list.html", {'data_list': data_list})

def dep_add(request):
    """
    add department
    """
    if request.method == "GET":
        return render(request, "dep_add.html")
    
    dep_name=request.POST.get("dep_name")
  
    models.Department.objects.create(name=dep_name)
    
    return redirect("/dep/list/")

def dep_delete(request):
    """
    delete department
    """
    
    n = request.GET.get("nid")

    models.Department.objects.filter(id=n).delete()
    return redirect("/dep/list/")

def dep_edit(request, nid):
    """
    edit department
    """
    if request.method == "GET":
        row_object = models.Department.objects.filter(id=nid).first()
        print(row_object.name, row_object.id)
        return render(request, "dep_edit.html", {"row_object": row_object})

    #obtain  user post data
    dep_name =request.POST.get("dep_name")

    dep_id =request.POST.get("dep_id")
   
    # update db according to nid/id
    models.Department.objects.filter(id=nid).update(name=dep_name)
    models.Department.objects.filter(name=dep_name).update(id=dep_id)
    return redirect("/dep/list/")

def user_list(request):
    
    #get all user_list
    
    queryset = models.EmployeeInfo.objects.all()
    
    return render(request, "user_list.html", {"queryset":queryset})


# def user_add(request):

#     if request.method == "GET":
        
#         context = {
           
#            "gender_choices" : models.EmployeeInfo.gender_choices,
           
#            "department" : models.Department.objects.all()
#        }
        
#         return render(request, "user_add.html", context)
   
#     #get user data
    
#     f_name = request.POST.get("f_name")
#     l_name = request.POST.get("l_name")
#     pwd = request.POST.get("pwd")
#     age= request.POST.get("age")
#     gender = request.POST.get("gender")
#     acc = request.POST.get("acc")
#     date = request.POST.get("date")
#     dep = request.POST.get("dep")
    
#     models.EmployeeInfo.objects.create(f_name=f_name, l_name=l_name,password=pwd, 
#                                        age=age,gender=gender,account=acc, 
#                                        create_time=date,dep_id=dep)
#     return redirect("/user/list")

class MyForm(ModelForm):
    class Meta:
        model = models.EmployeeInfo
        fields = ["f_name","l_name","password", "age", "account", "create_time", "dep", "gender"]
        # widgets ={
        #     "f_name":forms.TextInput(attrs={"class":"form-control", "placeholder":"Default"}),
        #     "l_name":forms.TextInput(attrs={"class":"form-control"}),
        #     "password":forms.PasswordInput(attrs={"class":"form-control"}),
        # }
        
    def __init__(self, *args, **kargs):
        super().__init__(*args,**kargs)
        
        for name, field in self.fields.items():
            print(name, field)
            field.widget.attrs = {"class":"form-control", "placeholder":field.label}
            


def user_add(request):
    
    if request.method == "GET":
        form = MyForm()
        
        return render(request, "user_add.html", {"form":form})
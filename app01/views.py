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
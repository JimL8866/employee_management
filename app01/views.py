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
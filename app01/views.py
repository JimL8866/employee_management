from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def dep_list(request):
    """
    department list
    """
    return render(request, "dep_list.html")
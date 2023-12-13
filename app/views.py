from django.shortcuts import render
from app.models import *
# Create your views here.
def dept(request):
    qslo=Dept.objects.all()
    d={'qslo':qslo}
    return render(request,'dept.html',d)
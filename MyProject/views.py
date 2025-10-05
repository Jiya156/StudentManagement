from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from students.models import Student

def home(request):
    data = Student.objects.all()
    namelist=[]

    for i in data:
        namelist.append(i.Name)

    stu={
        "names":namelist
    }

    return render(request,"index.html",stu)

def add(request):
    return render(request,"add.html")

def store(request):
    name = request.GET["Name"]
    email = request.GET["Email"]
    rollnum = request.GET["Roll_Number"]
    course = request.GET["Course"]
    sem = request.GET["Semester"]
    batch = request.GET["Batch"]

    result = Student(Name=name, Email=email, Roll_Number=rollnum, Course=course, Semester=sem, Batch=batch)
    result.save()

    return render(request,"form.html",{"msg":"created"})


def table(request):
    data = Student.objects.all()
    return render(request,"table.html",{"data":data})


def delete(request,id):
    myid = id
    Student.objects.filter(id=myid).delete()
    return render(request,"delete.html",{"msg":"deleted"})

def update(request,id):
    stu = get_object_or_404(Student, id=id)
    return render(request,"updateform.html",{"stu":stu})

def submitupdate(request, id):
    stu = get_object_or_404(Student, id=id)

    stu.Name = request.GET["Name"]
    stu.Email = request.GET["Email"]
    stu.Roll_Number = request.GET["Roll_Number"]
    stu.Course = request.GET["Course"]
    stu.Semester = request.GET["Semester"]
    stu.Batch = request.GET["Batch"]
    stu.save()

    return render(request,"updated.html")
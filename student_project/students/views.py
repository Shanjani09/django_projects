from django.shortcuts import render, HttpResponse
from .models import Student
from faker import Faker 
fake=Faker() 
def add_student(request): 
    student=Student( 
        name=fake.name(), 
        age=fake.random_int(min=18,max=30), 
        email=fake.email() 
    ) 
    student.save() 
    return HttpResponse("Student record added successfully")
def student_info(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})
def delete(request):
    Student.objects.all().delete()
    return HttpResponse("All products have been deleted.")

    

from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import SchoolForm, ProfessorForm, StudentForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def school(request):

    if request.method == "POST":
        form = SchoolForm(request.POST)

        print(form)

        if form.is_valid():
            information = form.cleaned_data
            school = School(name=information['name'],
                            address=information['address'],
                            phone=information['phone'],
                            gmail=information['gmail'])
            school.save()
            return render(request,'goodJob.html')
    
    else:
        form = SchoolForm()

    return render(request, 'school.html', {'form':form})

def professor(request):
    
    if request.method == "POST":
        form = ProfessorForm(request.POST)

        print(form)

        if form.is_valid():
            information = form.cleaned_data
            professor = Professor(name=information['name'],
                            occupation=information['occupation'],
                            age=information['age'],
                            phone=information['phone'],
                            gmail=information['gmail'])
            professor.save()
            return render(request,'goodJob.html')
    
    else:
        form = ProfessorForm()

    return render(request, 'professor.html', {'form':form})

def student(request):
    
    if request.method == "POST":
        form = StudentForm(request.POST)

        print(form)

        if form.is_valid():
            information = form.cleaned_data
            student = Student(name=information['name'],
                            surname=information['surname'],
                            grade=information['grade'],
                            age=information['age'],
                            phone=information['phone'],
                            gmail=information['gmail'])
            student.save()
            return render(request,'goodJob.html')
    
    else:
        form = StudentForm()

    return render(request, 'student.html', {'form':form})

def goodJob(request):
    return render(request, 'goodJob.html')

def searchStudent(request):
    return render(request, 'searchStudent.html')

def search(request):
    if 'name' in request.GET:
        name = request.GET['name']
        students = Student.objects.filter(name__icontains=name)

        return render(request,'searchResult.html',{'students':students})

    else:
        answer = 'No enviaste ningún dato.'
    

    return HttpResponse(answer)

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def Student(request):
    return render(request, 'Student.html')

def Subject(request):
    return render(request, 'subject.html')
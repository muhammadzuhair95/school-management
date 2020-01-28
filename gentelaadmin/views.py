from django.shortcuts import render

# Create your views here.
from students.models import *

from course.models import *

def home(request):
	students = Student.objects.all()
	male_std = Student.objects.filter(gender='M') 
	female_std = Student.objects.filter(gender='M') 
	no_of_std = students.count()
	no_male_std = male_std.count()
	no_female_std = male_std.count()
	print (no_male_std)
	context = {
		'no_of_std':no_of_std,
		'no_male_std':no_male_std,
		'no_female_std':no_female_std
	}
	return render(request, 'home.html', context)

def get_students(request):
	students = Student.objects.all()
	for student in students:
		print (student.first_name + " "+ student.last_name)
		print (student.gender)
	context = {
		"students":students
	}
	return render(request, 'students/student.html', context)

def get_course(request):
	courses = Course.objects.all()
	print (courses)
	# for student in students:
	# 	print (student.first_name + " "+ student.last_name)
	context = {
		"courses":courses
	}
	return render(request, 'course/course.html', context)	


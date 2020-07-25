from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic.detail import DetailView
from Regapp.models import Student
# Create your views here.

def studentinfo(request):
	all_details = Student.objects.all()
	#for data in all_details:
		#print(data.Name)
	return render(request, 'staff/studetails.html', {'Students': all_details})

def accept_view(request):
    if request.method == 'POST':
        i = request.POST["student_id"]
        id = int(i)
        print(type(id),id)
        #stu = get_object_or_404(Student, pk=id)
        stu = Student.objects.filter(id=id)
        if 'accept' in request.POST["decision"]:
            for stud in stu:
                stud.status='accepted'
                stud.save()
            return redirect('/first_approval/staff/')
        if 'reject' in request.POST["decision"]:
            for stud in stu:
                stud.status = 'rejected'
                stud.save()
            return redirect('/first_approval/staff/')
    selectedstu = Student.objects.filter(status='accepted')
    #selectedstu = Student.objects.all()
    #for data in selectedstu:
        #print(data.Name)
    return render(request, "staff/Selected_requests.html", {"selectedStudents": selectedstu})	
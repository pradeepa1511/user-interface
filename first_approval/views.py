from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic.detail import DetailView
from Regapp.models import Student
# Create your views here.

def studentinfo(request):
	all_details = Student.objects.all()
	return render(request, 'staff/studetails.html', {'Students': all_details})

def accept_view(request):
    if request.method == 'POST':
        id = request.POST["student_id"]
        stu = get_object_or_404(Student, pk=id)
        if 'accept' in request.POST["decision"]:
        # if request.POST["decision"]=='accept':
            stu.status='accepted'
            stu.save()
            return redirect('staff_view')
        if 'reject' in request.POST["decision"]:
        # if request.POST["decision"] == 'reject':
            stu.status = 'rejected'
            stu.save()
            return redirect('staff_view')
    selectedstu = Student.objects.filter(status='accepted')
    return render(request, "staff/Selected_requests.html", {"selectedStudents": selectedstu})	
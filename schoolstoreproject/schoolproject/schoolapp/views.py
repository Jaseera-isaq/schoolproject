from django.shortcuts import render, redirect
from .models import Department
# Create your views here.

def demo(request):
    departments = Department.objects.all()
    return render(request, "home.html", {'departments': departments})

# def department_list(request):
#     departments = Department.objects.all()
#     if request.method == 'POST':
#         department_id = request.POST.get('department')
#         department = Department.objects.get(pk=department_id)
#         return redirect(department.wikipedia_link)
#     return render(request, 'home.html', {'departments': departments})

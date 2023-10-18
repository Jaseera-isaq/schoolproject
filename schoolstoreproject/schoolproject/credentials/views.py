from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, "buttonclick.html")
        else:
            messages.info(request, "Invalid credentials")
            return render(request, "login.html")

    return render(request, "login.html")
def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is already existing")
                return render(request, "register.html")
            else:
                # user = User.objects.create_user(username=username, password=password)
                # user.save();
                return render(request, "login.html")
                print("user created")
        else:
            messages.info(request, "password is incorrect")
            return render(request, "register.html")

        return redirect('/')

    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def buttonclick(request):
    return render(request, "newform.html")

#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         dob = request.POST['dob']
#         age = request.POST['age']
#         gender = request.POST['gender']
#         phone_number = request.POST['phone_number']
#         address = request.POST['address']
#         department = request.POST['department']
#         course = request.POST['course']
#         purpose = request.POST['purpose']
#         materials = request.POST['materials']
#         usern = auth.authenticate(name=name, email=email, dob=dob, age=age, gender=gender, phone_number=phone_number, address=address, department=department, course=course, purpose=purpose, materials=materials)
#         if usern is not None:
#             messages.info(request, "Order confirmed")
#             return render(request, "home.html")
#         else:
#             messages.info(request, "Incomplete")
#             return redirect('buttonclick')
#
#     return render(request, "newform.html")

def submit(request):
    return render(request, "submit.html")

def newform(request):
    return render(request, "newform.html")
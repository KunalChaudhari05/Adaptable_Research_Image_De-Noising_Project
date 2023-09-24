from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.verify import authentication
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from datetime import datetime
from .form import *
from .utility import *
from .models import image_denoising, user_profile
from .ESRGAN.test import enhance_image
import cv2
import datetime

# Create your views here.
def index(request):
    # return HttpResponse("This is Home page")    
    return render(request, "index.html", {'navbar' : 'home'})

def log_in(request):
    context = {
        'form' : user_login_form()
    }
    if request.method == "POST":
        form = user_login_form(request.POST, request.FILES)
        if form.is_valid():
            # return HttpResponse("This is Home page")  
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            security_qus = form.cleaned_data['security_qus']
            ans = form.cleaned_data['ans']

            user = authenticate(username = username, password = password)
            if user is not None:
                profile_security = user_profile.objects.get(user=user)
                if profile_security.security_qus == security_qus and profile_security.ans == ans:
                    login(request, user)
                    messages.success(request, "Log In Successful...!")
                    return redirect("dashboard")
                else:
                    messages.error(request, "Security Question And Answer are Incorrect...!")
                    return redirect("log_in")
            else:
                messages.error(request, "Invalid User...!")
                return redirect("log_in")
        else:
            messages.error(request, "Invalid Form...!")
            return redirect("log_in")
    # return HttpResponse("This is Home page")    
    return render(request, "log_in.html", context)

def register(request):
    context = {
        'form' : user_profile_form()
    }
    if request.method == "POST":
        form = user_profile_form(request.POST, request.FILES)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            security_qus = form.cleaned_data['security_qus']
            ans = form.cleaned_data['ans']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password1 = form.cleaned_data['password1']
            # print(fname, contact_no, ussername)
            verify = authentication(fname, lname, password, password1, ans)
            if verify == "success":
                user = User.objects.create_user(username, password, password1)          #create_user
                profile =  user_profile(user = user, security_qus = security_qus, ans = ans)
                user.first_name = fname
                user.last_name = lname
                user.save()
                profile.save()
                messages.success(request, "Your Account has been Created.")
                return redirect("/")
                
            else:
                messages.error(request, verify)
                return redirect("register")
        else:
            messages.error(request, "Invalid Form Data.")
            return redirect("register")
    # return HttpResponse("This is Home page")    
    return render(request, "register.html", context)


@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def log_out(request):
    logout(request)
    messages.success(request, "Log out Successfuly...!")
    return redirect("/")


@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def dashboard(request):
    context = {
        'fname': request.user.first_name, 
        'form' : image_upload()
    }
    if request.method == "POST":
        form = image_upload(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            original_image = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
            nuce_img = NUCE(original_image)

            basename = "static/results/denoised_image"
            suffix = datetime.datetime.now().strftime("%y%m%d%H%M%S")
            file_name = "_".join([basename, suffix,".png"]) # e.g. 'mylogfile_120508_171442'

            output = enhance_image(nuce_img, file_name)
            img = image_denoising(image = image, denoised_image = file_name)
            img.date = datetime.datetime.today()
            img.save()
            messages.success(request, "Denoised Image is Automatically Downloaded in Result Folder!!!")
            return redirect("results")
    return render(request, "dashboard.html",context)

@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def results(request):
    img = image_denoising.objects.last()
    
    context = {
        'fname': request.user.first_name, 
        'img' : img
    }
    
    return render(request, "results.html",context)
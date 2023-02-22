from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import AbstractUser,User
from video.models import Video,VideoLesson,Member
from .models import Category,CategorySub
from .forms import EmailAuthenticationForm,SignUpForm,ProfileForm
from django.contrib import messages


def index(request):
    video = Video.objects.filter(published=True)
    context = {'video_list':video,}
    return render(request,'index.html',context)


def login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('app:index')
    else:
        form = EmailAuthenticationForm()
    return render(request,'account/login.html',{
            'form':form
        })


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('app:index')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.email = form.cleaned_data.get('email')
            user.save()
            m=Member()
            m.user_id = user.id
            m.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request,user)
            return redirect('app:login')
    else:
        form = SignUpForm()
    return render(request,'account/signup.html',{
            'form':form
        })


def profile_management(request):
    profile=Member.objects.filter(user_id=request.user.id).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            user = User.objects.get(pk=request.user.id)
            user.first_name = request.POST.get('firstname')
            user.last_name = request.POST.get('lastname')
            user.save()
            profile = form.save()
            profile.save()
            messages.success(request, 'แก้ไขสำเร็จ')
            return redirect('app:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request,'account/profile.html',{
            'form':form,
            'profile':profile
        })


def search_video(request):
    txt_search = request.POST.get('txtSearch')
    video_list = Video.objects.filter(name__contains=txt_search,published=True)
    return render(request, 'search.html', {'video_list': video_list})

def facebook_login(request):
    user = request.email
    if user.is_authenticated:
        return redirect('home')
    else:
        login(request, user)
        return redirect('home')

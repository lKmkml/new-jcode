from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import AbstractUser
from video.models import Video,VideoLesson
from .models import Category,CategorySub
from .forms import EmailAuthenticationForm
# Create your views here.
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
            return redirect('video:index')
    else:
        form = EmailAuthenticationForm()
        print(form)
    return render(request,'account/login.html',{
            'form':form
        })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('app:index')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('book:index')
    else:
        form = UserCreationForm()
    return render(request,'account/signup.html',{
            'form':form
        })

from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView, DetailView
from .models import Video,VideoLesson,VideoChapter
from .models import Category,CategorySub,Member
from .forms import VideoForm,VideochapterForm,VideolessonForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from slugify import slugify

# Create your views here.
def index(request):
    video = Video.objects.filter(published=True)
    context = {'video_list':video,}

    return render(request,'video/index.html',context)


def management_course(request):
    videos = Video.objects.filter(member__user=request.user.id)
    return render(request,'video/course.html',{"video_list":videos})


def management_chapter(request,id):
    chapters = VideoChapter.objects.filter(video__id=id)
    return render(request,'video/chapter.html',{"chapters_list":chapters,"ids":id})


def management_lesson(request,id):
    lesson = VideoLesson.objects.filter(chapter__id=id)
    return render(request,'video/lesson.html',{"lesson_list":lesson,"ids":id})


def video_add(request):
    form = VideoForm()

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.slug = slugify(video.name)
            video.member = Member.objects.filter(user_id=request.user.id).first() #จำเป็น
            video.published = True
            video.save()
            form.save_m2m()
            messages.success(request, 'Save success')
            return HttpResponseRedirect(reverse('video:index', kwargs={}))
        messages.error(request, 'Save Failed!')
    return render(request, 'video/add.html', {
        'form': form,
    })

class BookDetailView(DetailView):
    model = Video
    template_name = 'video/detail.html'
    slug_url_kwarg = 'slug'

def video_addchapter(request,id):
    form = VideochapterForm()
    if request.method == 'POST':
        form = VideochapterForm(request.POST, request.FILES)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.save()
            form.save_m2m()
            messages.success(request, 'Save success')
            return HttpResponseRedirect(reverse('video:index', kwargs={}))
        messages.error(request, 'Save Failed!')
    return render(request, 'video/add.html', {
        'form': form,
    })

def video_addlesson(request,id):
    form = VideolessonForm()

    if request.method == 'POST':
        form = VideolessonForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.save()
            form.save_m2m()
            messages.success(request, 'Save success')
            return HttpResponseRedirect(reverse('video:index', kwargs={}))
        messages.error(request, 'Save Failed!')
    return render(request, 'video/add.html', {
        'form': form,
    })

def video_delete(request, id):
    videos = Video.objects.get(id=id)
    if request.method == 'POST':
        videos.delete()
        url= reverse('video:management_course')
        return redirect(url)
    return render(request, 'video/video_confirm_delete.html', {'videos': videos,})

def chapter_delete(request, id):
    chaptervideo = VideoChapter.objects.get(id=id)
    if request.method == 'POST':
        chaptervideo.delete()
        url= reverse('video:management_chapter')
        return redirect(url)
    return render(request, 'video/chapter_confirm_delete.html', {'chapters':chaptervideo})

def lesson_delete(request, id):
    lessonvideo = VideoLesson.objects.get(id=id)
    if request.method == 'POST':
        lessonvideo.delete()
        url= reverse('video:management_lesson')
        return redirect(url)
    return render(request, 'video/lesson_confirm_delete.html', {'lessons':lessonvideo})

def update_video(request, id):
    videos= Video.objects.get(id=id)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=videos)
        if form.is_valid():
            form.save()
            return redirect('video:management_course')
    else:
        form = VideoForm(instance=videos)
    return render(request, 'video/update_video.html', {'form': form})

def update_chapter(request, id):
    chapters= VideoChapter.objects.get(id=id)
    if request.method == 'POST':
        form = VideochapterForm(request.POST,  instance=chapters)
        if form.is_valid():
            form.save()
            return redirect('video:management_course')
    else:
        form = VideochapterForm(instance=chapters)
    return render(request, 'video/update_chapter.html', {'form': form})

def update_lesson(request, id):
    lessons= VideoLesson.objects.get(id=id)

    if request.method == 'POST':
        form = VideolessonForm(request.POST,  instance=lessons)
        if form.is_valid():
            form.save()
            return redirect('video:management_course')
    else:
        form = VideolessonForm(instance=lessons)
    return render(request, 'video/update_lesson.html', {'form': form})

from django import forms
from .models import Video,VideoChapter,VideoLesson

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        exclude = ['id','member', 'slug', 'published', 'created', 'updated']
        labels ={
            'name':'ชื่อ',
            'description':'รายละเอียด',
            'image':'ภาพคอร์ส',
            'videoexample':'วิดีโอตัวอย่าง',
            'category':'ประเภทหลัก',
            'category_sub':'ประเภทย่อย',
            'price':'ราคา',
            'price_before':'ราคาเต็ม'
        }

class VideochapterForm(forms.ModelForm):
    class Meta:
        model = VideoChapter
        exclude = ['id','video', 'created', 'updated']
        labels ={
            'name':'ชื่อ',
            'ordered':'ลำดับ'
        }

class VideolessonForm(forms.ModelForm):
    class Meta:
        model = VideoLesson
        exclude = ['id','videos','chapter', 'created', 'updated']
        labels ={
            'name':'ชื่อ',
            'duration_time':'ระยะเวลา',
            'lessonvideo':'วิดีโอ',
            'video_url':'ลิงค์วิดีโอ',
            'is_locked':'ดูได้เฉพาะผู้ซื้อคอร์สแล้ว',
            'ordered':'ลำดับ',
        }

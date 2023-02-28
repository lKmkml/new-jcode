from django.db import models
from app.models import Category,CategorySub,Member
from star_ratings.models import Rating
from django.contrib.contenttypes.fields import GenericRelation

#------------------------------------------------------
#Model ของ Course
#------------------------------------------------------
class Video(models.Model):
    member = models.ForeignKey(Member,null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=450)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='video', null=True, blank=True)
    videoexample=models.FileField(upload_to='video/example', null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    category_sub = models.ForeignKey(CategorySub, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    price_before = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ratings = GenericRelation(Rating, )


    def get_chapter_set_with_ordered(self):
        return self.videolesson_set.order_by('chapter__ordered','ordered')


    def __str__(self):
        return self.name


    @classmethod
    def search(cls, query):
        return cls.objects.filter(title__icontains=query) | cls.objects.filter(content__icontains=query)


#------------------------------------------------------
#Model ของ Chapter
#------------------------------------------------------
class VideoChapter(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    ordered = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


#------------------------------------------------------
#Model ของ Lesson
#------------------------------------------------------
class VideoLesson(models.Model):
    videos = models.ForeignKey(Video, on_delete=models.CASCADE,default=1)
    chapter = models.ForeignKey(VideoChapter, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    duration_time = models.CharField(max_length=15, null=True, blank=True)
    lessonvideo = models.FileField(upload_to='video/lesson/video', null=True, blank=True)
    video_url = models.CharField(max_length=450, null=True, blank=True)
    is_locked = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ordered = models.IntegerField(default=0)


    def __str__(self):
        return self.name


class Payment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_by = models.CharField(max_length=450,default="Cash")
    payment_amount = models.FloatField()

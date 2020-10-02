from embed_video.fields import EmbedVideoField
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Student_Admission(models.Model):
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    number = models.IntegerField()
    email = models.EmailField(max_length=200)
    student_image = models.ImageField(upload_to="Student_admission")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def image_url(self):
        if self.student_image:
            return self.student_image.url
        else:
            return ""


"""
mobile_number = models.CharField(primary_key=True, max_length=10, validators=[
                                     RegexValidator(r'^\d{1,10}$'), MinLengthValidator(10)])
from django.core.validators import RegexValidator, MinLengthValidator
from django.utils.safestring import mark_safe


 def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.image.url))

    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return ""

"""


class Item(models.Model):
    video = EmbedVideoField()


class Mydata(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()

    def __str__(self):
        return self.title

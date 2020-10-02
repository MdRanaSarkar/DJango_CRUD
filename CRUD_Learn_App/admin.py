

from embed_video.admin import AdminVideoMixin
from django.contrib import admin
from .models import Student_Admission, Item, Mydata
# Register your models here.


admin.site.register(Student_Admission)


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Item, MyModelAdmin)


admin.site.register(Mydata)

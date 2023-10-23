from django.contrib import admin

from projectaccount.models import Semester, Subject

# Register your models here.



class SemesterAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Semester, SemesterAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name","semester")


admin.site.register(Subject, SubjectAdmin)

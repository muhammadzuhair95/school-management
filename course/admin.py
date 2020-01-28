from django.contrib import admin

from .models import Course


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Admin Display Options to display the Course data in admin panel"""

    list_display = (
        'subject_name',
        'subject_description'
    )

    search_fields = (
        'subject_name',
    )

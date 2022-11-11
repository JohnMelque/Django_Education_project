from django.contrib import admin
from .models import Language,Course,Chapters,Content_Type,Course_chapter_content

# Register your models here.
admin.site.register(Language)
admin.site.register(Course)
admin.site.register(Chapters)
admin.site.register(Content_Type)



@admin.register(Course_chapter_content)
class Course_chapter_contentAdmin(admin.ModelAdmin):
    radio_fields = {"is_open_for_free": admin.HORIZONTAL,"is_mandatory": admin.HORIZONTAL}
    
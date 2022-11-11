from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import *

routers=routers.DefaultRouter()


routers.register("staff",staffView)
routers.register("student",studentView)
routers.register("instructor",instructorView)
routers.register("enrollmentView",enrollmentView)
routers.register("learning_progress",learning_progressView)
routers.register("feedback",feedbackView)
routers.register("language",languageView)
routers.register("course",courseView)
routers.register("chapter",chaptersView)
routers.register("content_Type",content_TypeView)
routers.register("course_chapter_content",course_chapter_contentView)

urlpatterns = [
    path('api/',include(routers.urls)),
    
]
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import Staff,Student,Instructor
from Master.models import Enrollment,Learning_progress,Feedback
from Courses.models import Language,Course,Chapters,Content_Type,Course_chapter_content





class staffView(viewsets.ModelViewSet):
    queryset=Staff.objects.all()
    serializer_class=staffserializers
    
class studentView(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=studentserializers
    
class instructorView(viewsets.ModelViewSet):
    queryset=Instructor.objects.all()
    serializer_class=instructorserializers
    
#Master Models     
    
class enrollmentView(viewsets.ModelViewSet):
    queryset=Enrollment.objects.all()
    serializer_class=enrollmentializers
    
class learning_progressView(viewsets.ModelViewSet):
    queryset=Learning_progress.objects.all()
    serializer_class=learning_progressserializers
    
    
class feedbackView(viewsets.ModelViewSet):
    queryset=Feedback.objects.all()
    serializer_class=feedbackserializers
    
#Courses Models       
    
class languageView(viewsets.ModelViewSet):
    queryset=Language.objects.all()
    serializer_class=languageserializers
    
class courseView(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=courseserializers
    
class chaptersView(viewsets.ModelViewSet):
    queryset=Chapters.objects.all()
    serializer_class=chaptersserializers    
    
class content_TypeView(viewsets.ModelViewSet):
    queryset=Content_Type.objects.all()
    serializer_class=content_Typesserializers
    
class course_chapter_contentView(viewsets.ModelViewSet):
    queryset=Course_chapter_content.objects.all()
    serializer_class=course_chapter_contentserializers                                            


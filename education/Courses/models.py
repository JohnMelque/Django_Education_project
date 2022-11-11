from django.db import models
from Configuration .models import *

# Create your models here.
class Language(models.Model):
    language_name=models.CharField("Language Name",max_length=50,null=False,blank=False)
    
    def __str__(self):
        return self.language_name
    
class Course(models.Model):
    course_title=models.CharField("Course title",max_length=200,null=False,blank=False)    
    course_brief=models.CharField("Course brief",max_length=4000,null=False,blank=False)
    instructor_id=models.ForeignKey(Instructor, on_delete=models.CASCADE,null=False,blank=False)
    num_of_chapters=models.IntegerField("No of Chapters",null=True,blank=False)
    course_fee=models.IntegerField("Course Fee",null=True,blank=False)
    language_id=models.ManyToManyField(Language)
    
    def __str__(self):
        return self.course_title

class Chapters(models.Model):
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE,null=False,blank=False)
    chapter_title=models.CharField("Chapter title",max_length=100,null=False,blank=False)
    num_of_reading=models.IntegerField("Reading books",null=True,blank=False)
    num_of_video=models.IntegerField("No of Video",null=True,blank=False)
    num_of_assignment=models.IntegerField("No of Assignment",null=True,blank=False)
    
    def __str__(self):
        return self.chapter_title
    
    
class Content_Type(models.Model):
    content_type=models.CharField("Content Type",max_length=20,null=False,blank=False)    
    
    def __str__(self):
        return self.content_type
    
    
class Course_chapter_content(models.Model):
    course_chapter_id=models.ForeignKey(Chapters, on_delete=models.CASCADE,null=False,blank=False)
    content_type_id=models.ForeignKey(Content_Type, on_delete=models.CASCADE,null=False,blank=False) 
    is_mandatory=models.CharField("Is Mandatory",choices=[('yes','YES'),('no','NO')],max_length=20,null=False,blank=False) 
    time_required_in_sec=models.IntegerField("Time required in sec",null=True,blank=False)
    is_open_for_free=models.CharField("Is Free",choices=[('yes','YES'),('no','NO')],max_length=20,null=False,blank=False)    

    def __str__(self):
        return str(self.course_chapter_id)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      
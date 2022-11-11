from django.db import models
from Configuration.models import *
from Courses.models import *
from datetime import date

# Create your models here.
class Enrollment(models.Model):
    student_id=models.ForeignKey(Student, on_delete=models.CASCADE,null=False,blank=False)
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE,null=False,blank=False)
    enrollment_date=models.DateField("Enrollment Date",null=False,blank=False)
    is_paid_subscription=models.CharField("Paid",choices=[('yes','YES'),('no','NO')],max_length=20,null=False,blank=False)
    
    def clean(self):
        today = date.today()
        if self.enrollment_date and today == None:
            raise ValidationError("Enter a valide date ")
        return super().clean()
    
    def __str__(self):
        return str(self.student_id)
    
    
class Learning_progress(models.Model):
    enrollment_id=models.ForeignKey(Enrollment, on_delete=models.CASCADE,null=False,blank=False)
    course_chapter_content_id=models.ForeignKey(Course_chapter_content, on_delete=models.CASCADE,null=False,blank=False)
    begin_time=models.TimeField("Begin Time",null=False,blank=False)
    completion_time=models.TimeField("Completion Time",null=False,blank=False)
    status=models.CharField("Status",choices=[('pending','Pending'),('Finshed','Finshed')],max_length=20,null=False,blank=False)
    
    def __str__(self):
        return str(self.status)
    
class Feedback(models.Model):
    enrollment_id=models.ForeignKey(Enrollment, on_delete=models.CASCADE,null=False,blank=False)
    rating_score=models.IntegerField("Rating",null=True,blank=False)
    feedback_text=models.CharField("Feedback",max_length=250,null=False,blank=False) 
    submission_date=models.DateField("Submission-date",null=False,blank=False)
    
    
    def clean(self):
        today = date.today()
        if self.submission_date and today == None:
            raise ValidationError("Enter a valide date")
        return super().clean()
      
    def __str__(self):
        return str(self.rating_score)    
       
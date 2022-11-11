from django.db import models
import re
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser
from django.contrib.auth.models import Group
from django.forms import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


    
    
class Staff(models.Model):
    name=models.CharField("Name",max_length=50,null=False,blank=False)
    email=models.EmailField("Email",max_length=50,null=False,blank=False)
    dob=models.DateField("Date of Birth",null=False,blank=False)
    age=models.IntegerField("Age",null=True,blank=False)
    phone=models.CharField("Phone",max_length=10,null=True,blank=False)
    qualification=models.CharField("Qualification",max_length=200,null=False,blank=False)
    specialized=models.CharField("Specialized",max_length=50,null=False,blank=False)
    ctype = models.CharField(
        "Type", max_length=100, null=True, blank=True, default='Staff')
    
    def clean(self):
        a=re.match("[6-9]{1}[0-9]{9}",self.phone)
        if self.phone and a == None:
            raise ValidationError("Enter a valide number")    
        return super().clean()
    def __str__(self):
        return self.name
    
@receiver(post_save, sender=Staff)
def event_attender_create(sender, instance, *args, **kwargs):
    if instance and kwargs['created']:
        user = CustomUser.objects.create(email=instance.email, username=instance.name.lower(),
                                         staff=instance, role="Staff", is_staff=True)
        user.set_password(instance.phone)
        context = {'name': instance.name,
                   'username': user.email,
                   'password': instance.phone}

        message = EmailMultiAlternatives(
            subject="subject", from_email="john", reply_to=[instance.email], to=[instance.email])
        html_template = get_template(
            "email.html").render(context)
        message.attach_alternative(html_template, "text/html")
        message.send()
        if instance.ctype == "Staff":
            if Group.objects.filter(name='Staff').exists():
                user.groups.add(Group.objects.get(name='Staff'))
        user.save()
    return True    
       
class Instructor(models.Model):
    first_name=models.CharField("First Name",max_length=50,null=False,blank=False)
    last_name=models.CharField("Last Name",max_length=50,null=False,blank=False)
    email=models.EmailField("Email",max_length=50,null=False,blank=False)
    phone=models.CharField("Phone",max_length=10,null=True,blank=False)
    registration_date=models.DateField("Registration Date",null=False,blank=False)
    qualification=models.CharField("Qualification",max_length=200,null=False,blank=False)
    introduction_brief=models.CharField("Introduction brief",max_length=200,null=False,blank=False)
    image=models.ImageField(upload_to="picture",null=True,blank=True)
    num_of_published_course=models.IntegerField("Published course",null=True,blank=False)
    num_of_enrolled_student=models.IntegerField("Enrolled student",null=True,blank=False)
    average_review_rating=models.IntegerField("Rating",null=True,blank=True)
    num_of_reviews=models.IntegerField("Reviews",null=True,blank=True)
    ctype = models.CharField(
        "Type", max_length=100, null=True, blank=True, default='Instructor')
    def clean(self):
        a=re.match("[6-9]{1}[0-9]{9}",self.phone)
        if self.phone and a == None:
            raise ValidationError("Enter a valide number") 
        today = date.today()
        print("____________",today)
        if self.registration_date and today == None:
            raise ValidationError("Enter a valide date")
           
        return super().clean()
    def __str__(self):
        return self.first_name
    
@receiver(post_save, sender=Instructor)
def event_attender_create(sender, instance, *args, **kwargs):
    if instance and kwargs['created']:
        user = CustomUser.objects.create(email=instance.email, username=instance.first_name.lower(),
                                         instructor=instance, role="Instructor", is_staff=True)
        user.set_password(instance.phone)
        context = {'name': instance.first_name,
                   'username': user.email,
                   'password': instance.phone}

        message = EmailMultiAlternatives(
            subject="subject", from_email="john", reply_to=[instance.email], to=[instance.email])
        html_template = get_template(
            "instructor.html").render(context)
        message.attach_alternative(html_template, "text/html")
        message.send()
        if instance.ctype == "Instructor":
            if Group.objects.filter(name='Instructor').exists():
                user.groups.add(Group.objects.get(name='Instructor'))
        user.save()
    return True          
    
class Student(models.Model): 
    first_name=models.CharField("First Name",max_length=50,null=False,blank=False)
    last_name=models.CharField("Last Name",max_length=50,null=False,blank=False)
    email=models.EmailField("Email",max_length=50,null=False,blank=False)
    phone=models.CharField("Parent Phone",max_length=10,null=True,blank=False)
    registration_date=models.DateField("Registration Date",null=False,blank=False)        
    num_of_courses_enrolled=models.IntegerField("enrolled course",null=True,blank=False)
    num_of_courses_complete=models.IntegerField("complete course",null=True,blank=False)
    ctype = models.CharField(
        "Type", max_length=100, null=True, blank=True, default='Student')
    def clean(self):
        a=re.match("[6-9]{1}[0-9]{9}",self.phone)
        if self.phone and a == None:
            raise ValidationError("Enter a valide number")  
        
        today = date.today()
        if self.registration_date and today == None:
            raise ValidationError("Enter a valide date")
        return super().clean()
       
       
    def __str__(self):
        return (self.first_name)+(self.last_name)
@receiver(post_save, sender=Student)
def event_attender_create(sender, instance, *args, **kwargs):
    if instance and kwargs['created']:
        user = CustomUser.objects.create(email=instance.email, username=instance.first_name.lower(),
                                         student=instance, role="Student", is_staff=True)
        user.set_password(instance.phone)
        context = {'name': instance.first_name,
                   'username': user.email,
                   'password': instance.phone}

        message = EmailMultiAlternatives(
            subject="subject", from_email="john", reply_to=[instance.email], to=[instance.email])
        html_template = get_template(
            "email.html").render(context)
        message.attach_alternative(html_template, "text/html")
        message.send()
        if instance.ctype == "Student":
            if Group.objects.filter(name='Student').exists():
                user.groups.add(Group.objects.get(name='Student'))
        user.save()
    return True               
from rest_framework import serializers
from .models import Staff,Student,Instructor
from Master.models import Enrollment,Learning_progress,Feedback
from Courses.models import Language,Course,Chapters,Content_Type,Course_chapter_content
#Configuration Models


        
class staffserializers(serializers.ModelSerializer):
    class Meta:
        model=Staff
        fields='__all__'        

class studentserializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__' 
               
class instructorserializers(serializers.ModelSerializer):
    class Meta:
        model=Instructor
        fields='__all__' 
        
#Master Models               

class enrollmentializers(serializers.ModelSerializer):
    class Meta:
        model=Enrollment
        fields='__all__'  
    def to_representation(self, instance):
        res= super().to_representation(instance)
        res['student_id']=[instance.student_id.id] if instance.student_id else []
        res["course_id"]=[instance.course_id.id] if instance.course_id else []
        return res      

class learning_progressserializers(serializers.ModelSerializer):
    class Meta:
        model=Learning_progress
        fields='__all__'
    def to_representation(self, instance):
        res= super().to_representation(instance)
        res['enrollment_id']=[instance.enrollment_id.id] if instance.enrollment_id else []
        res["course_chapter_content_id"]=[instance.course_chapter_content_id.id] if instance.course_chapter_content_id else []
        return res        
     
                
class feedbackserializers(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields='__all__'
        
    def to_representation(self, instance):
        res= super().to_representation(instance)
        res['enrollment_id']=[instance.enrollment_id.id] if instance.enrollment_id else []
        return res         
    
        
#Courses Models        
        
class languageserializers(serializers.ModelSerializer):
    class Meta:
        model=Language
        fields='__all__'  

class courseserializers(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'
        
    def to_representation(self, instance):
        res= super().to_representation(instance)
        res['instructor_id']=[instance.instructor_id.id] 
        res["language_id"]=[instance.language_id.id] if instance.language_id else []
        return res     
        

class chaptersserializers(serializers.ModelSerializer):
    class Meta:
        model=Chapters
        fields='__all__' 
    
    def to_representation(self, instance):
        res= super().to_representation(instance)
        res['course_id']=[instance.course_id.id] if instance.course_id else []
        return res         
        
class content_Typesserializers(serializers.ModelSerializer):
    class Meta:
        model=Content_Type
        fields='__all__' 
        
class course_chapter_contentserializers(serializers.ModelSerializer):
    class Meta:
        model=Course_chapter_content
        fields='__all__'  
        
    def to_representation(self, instance):
        res= super().to_representation(instance)
        res['course_chapter_id']=[instance.course_chapter_id.id] if instance.course_chapter_id else []
        res['content_type_id']=[instance.content_type_id.id] if instance.content_type_id else []
        return res                                               
from rest_framework import serializers
from .models import course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = ["id","course_name"]

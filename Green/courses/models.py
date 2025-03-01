from django.db import models

# Create your models here.
class course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    duration = models.DurationField
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name
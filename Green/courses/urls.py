from django.urls import path
from . import views

urlpatterns = [
    path("course/", views.CourseAPIView.as_view(), name="Course-View-Create")
        # path("course/", views.CourseListCreate.as_view(), name="Course-View-Create")
]
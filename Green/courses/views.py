from django.shortcuts import render
from rest_framework import generics, status
from .models import course
from .serializers import CourseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# class CourseListCreate(generics.ListAPIView):
#     queryset = course.objects.all()
#     serializer_class = CourseSerializer

# class CourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = course.objects.all()
#     serializer_class = CourseSerializer
#     lookup_field = "pk"

class CourseAPIView(APIView):
    # Handle GET request
    def get(self, request, pk=None):
        if pk:
            try:
                _course = course.objects.get(pk=pk)
            except _course.DoesNotExist:
                return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = CourseSerializer(course)
            return Response(serializer.data)

        courses = course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    # Handle POST request
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # # Handle PUT request
    # def put(self, request, pk):
    #     try:
    #         _course = course.objects.get(pk=pk)
    #     except _course.DoesNotExist:
    #         return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

    #     serializer = CourseSerializer(course, data=request.data, partial=False)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # # Handle DELETE request
    # def delete(self, request, pk):
    #     try:
    #         _course = course.objects.get(pk=pk)
    #     except _course.DoesNotExist:
    #         return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

    #     course.delete()
    #     return Response({"message": "Course deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
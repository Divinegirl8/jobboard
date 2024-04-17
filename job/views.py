from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Job
from .serializer import JobSerializers
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(['GET', 'POST'])
def job_list(request):
    if request.method == 'GET':
        jobs = Job.objects.all()
        serializers = JobSerializers(jobs, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = JobSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def job_details(request, pk):
    job = get_object_or_404(Job, id=pk)
    if request.method == 'GET':
        serializers = JobSerializers(job)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = JobSerializers(job, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework import serializers
from .models import Job


class JobSerializers(serializers.Serializer):
    # title = serializers.CharField(max_length=100)
    # description = serializers.CharField(max_length=1000)
    # company_name = serializers.CharField(max_length=100)
    # requirements = serializers.CharField(max_length=1000)
    # salary = serializers.CharField(max_length=250)
    class Meta:
        model = Job
        fields = ['title', 'description', 'company_name', 'requirements,salary']

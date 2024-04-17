from django.urls import path
from . import views

urlpatterns = [
    path("jobs/", views.job_list, name="jobs"),
    path('jobs/<int:id>', views.job_details, name="job_detail")
]

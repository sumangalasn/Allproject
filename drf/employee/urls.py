
from django.urls import path
from .api import EmployeeCreateApi,EmployeeUpdateApi,EmployeeDeleteApi

urlpatterns = [
 path('api/create', EmployeeCreateApi.as_view()),
 path('api/update/<int:pk>', EmployeeUpdateApi.as_view()),
path('api/<int:pk>/delete',EmployeeDeleteApi.as_view()),

]
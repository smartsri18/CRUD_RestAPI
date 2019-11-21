from django.urls import path

from .views import EmpDetailView, EmpSearchView


app_name = "emp_details"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('empdetails/', EmpDetailView.as_view()),
    path('empdetails/<int:pk>', EmpDetailView.as_view()),
    path('empsearch/', EmpSearchView.as_view()),
]

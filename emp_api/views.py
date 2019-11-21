from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .models import EmpDetail
from .serializers import EmpDetailSerializer
# Create your views here.

class EmpDetailView(APIView):
    def get(self, request):
        emp_det = EmpDetail.objects.all()
        serializer = EmpDetailSerializer(emp_det, many=True)
        # permission_classes = (permissions.IsAuthenticated,)
        return Response({"emp_details": serializer.data})

    def post(self, request):
        emp_det = request.data.get('emp_details')

        # Create an article from the above data
        print(emp_det)
        serializer = EmpDetailSerializer(data=emp_det)
        if serializer.is_valid(raise_exception=True):
            emp_det_saved = serializer.save()
        return Response({"success": "Employee is '{}' created successfully".format(emp_det_saved.name)})

    def put(self, request, pk):
        saved_emp_det = get_object_or_404(EmpDetail.objects.all(), pk=pk)
        data = request.data.get('emp_details')
        serializer = EmpDetailSerializer(instance=saved_emp_det, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            emp_det_saved = serializer.save()
        return Response({"success": "Employee '{}' updated successfully".format(emp_det_saved.name)})

    def delete(self, request, pk):
        # Get object with this pk
        emp_det = get_object_or_404(EmpDetail.objects.all(), pk=pk)
        emp_det.delete()
        return Response({"message": "Employee with id `{}` has been deleted.".format(pk)},status=204)

class EmpSearchView(APIView):
    def get(self, request):
        email = request.data.get('email')
        emp_det = EmpDetail.objects.all().filter(email=email)
        serializer = EmpDetailSerializer(emp_det, many=True)
        return Response({"emp_details": serializer.data})

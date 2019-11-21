from rest_framework import serializers

from .models import EmpDetail

class EmpDetailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    department = serializers.CharField(max_length=255)
    mobile_no = serializers.IntegerField()
    salary = serializers.IntegerField()

    def create(self, validated_data):
        return EmpDetail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.department = validated_data.get('department', instance.department)
        instance.mobile_no = validated_data.get('mobile_no', instance.mobile_no)
        instance.salary = validated_data.get('salary', instance.salary)

        instance.save()
        return instance

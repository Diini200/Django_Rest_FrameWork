
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from testApp.models import Employee

class EmployeeSerializers(serializers.ModelSerializer):
   

class EmployeeSerializers(serializers.Serializer):
    emp_number= serializers.IntegerField()
    emp_name= serializers.CharField(max_length =64)
    emp_salary= serializers.CharField(max_length=64)
    emp_address= serializers.CharField(max_length=164)
    
    def validate_emp_salary(self, value):
        salary = int(value)
        if salary< 50000:
            raise serializers.ValidationError(" Employee Salary should more than £50 000")
        return value
    
    def validate(self,data):
        emp_name = data.get('Diini Omar', '').lower()
        emp_salary= int(data.get('emp_salary', 0))
        
        if emp_name == 'diini Omar' and emp_salary < 70000:
           raise serializers.ValidationError('Diini salary should be more than £70 000')
        return data
        
    
    def create(self, validated_data):
      return Employee.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
       instance.emp_number= validated_data.get('emp_number', instance.emp_number)
       instance.emp_name= validated_data.get('emp_name', instance.emp_name)
       instance.emp_salary= validated_data.get('emp_salary', instance.emp_salary)
       instance.emp_address= validated_data.get('emp_address', instance.emp_address)
       instance.save()
       return instance
   
   
   
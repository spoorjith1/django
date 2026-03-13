from rest_framework import serializers
from employees.models import Employee
from rest_framework.exceptions import ValidationError

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        
    def validate_email(self, value):
        if value.endswith("@xyz.com"):
            return value
        else:
            raise ValidationError("Email must end with '@xyz.com' domain")
    
    def validate_salary(self, value):
        if value > 0:
            return value
        else:
            raise ValidationError("Salary should be +ve")
        
    def validate_emp_id(self, value):
        if value.startswith("XYZ") and value[3:].isdigit():
            return value
        else:
            raise ValidationError("ID must start with XYZ and followed by numbers only")
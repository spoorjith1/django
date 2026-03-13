from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from employees.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status, mixins, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


#CLASS BASED VIEWS :

# class EmployeeView(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# class EmployeeDetailView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(Employee, pk=pk)
    
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



#MIXINS :

# class EmployeeView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    
#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
# class EmployeeDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    
#     def get(self, request, pk):
#         return self.retrieve(request, pk)
    
#     def put(self, request, pk):
#         return self.update(request, pk)
    
#     def delete(self, request, pk):
#         return self.destroy(request, pk)


#GENERICS :
# class EmployeeView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    
# class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer



#VIEWSETS :
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['designation']
    search_fields = ['name']
    
    def get_queryset(self):
        queryset = self.queryset
        
        emp_id_min = self.request.GET.get('emp_id_min')
        emp_id_max = self.request.GET.get('emp_id_max')
        salary_min = self.request.GET.get('salary_min')
        salary_max = self.request.GET.get('salary_max')
        
        if emp_id_min and emp_id_max:
            queryset = queryset.filter(emp_id__gte=emp_id_min, emp_id__lte=emp_id_max)
            
        if salary_min and salary_max:
            queryset = queryset.filter(salary__gte=salary_min, salary__lte=salary_max)
        
        return queryset
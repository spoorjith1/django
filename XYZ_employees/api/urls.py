from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet)

urlpatterns = [
    # path('employees/', views.EmployeeView.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetailView.as_view()),
    
    path('', include(router.urls)),
]
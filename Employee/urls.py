from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('employees',views.EmployeeView)
router.register('department',views.DepartmentView)

urlpatterns = [
    path('',include(router.urls))
]
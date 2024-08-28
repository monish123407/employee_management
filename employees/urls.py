from django.urls import path
from .views import EmployeeListCreate, EmployeeRetrieveUpdateDestroy,fetchAllEmployee
from . import views


from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
# from django.conf.urls import url
# schema_view = get_swagger_view(title='Pastebin API')
schema_view = get_schema_view(
    openapi.Info(
        title="Episyche Technologies",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('fetchAllEmployee/', views.fetchAllEmployee,name='fetchAllEmployee' ),
     path('DeleteEmployee/<int:pk>', views.delete,name='delete' ),
     path('addEmployee/', views.AddEmployee,name='add' ),
     path('employee/update/<int:pk>', views.UpdateEmployee, name='employee-update'),
]
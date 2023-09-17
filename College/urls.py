"""
URL configuration for College project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Student import views #as student
from Admin import views as Admin
from Staff import views as staff
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from College.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/login', views.LoginStudent, name="studentlogin" ),
    path('AdMinManager/access/lock/login', Admin.LoginAdmin, name="Adminlogin" ),
    path('staff/login', views.LoginStudent, name="Stafflogin" ),
    path('signup', views.signup, name="signup" ),
    path('../', Admin.log_outAdmin, name="Adminlogout" ),
    path('.../', staff.log_outStaff, name="Stafflogout" ),
    path('.../', views.log_outStudent, name="Studentlogout" ),
    path('dashboard/', views.Dashboard, name="dashboard" ),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)),name="graphql"),

]


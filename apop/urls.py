
from django.urls import path
from . import views
urlpatterns = [
  path('',views.home,name="home"),
  path('uppercase',views.uppercase,name="uppercase"),
  path('lowercase',views.lowercase,name="loweercase")
  ,path('isalphanumeric',views.isalphanumeric,name="isalphanumeric"),
  path('countwords',views.countwords,name="countwords"),
  path('calculator',views.calculator,name="calculator")
 
]
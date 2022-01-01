from django.contrib import admin
from django.urls import path,include
from .import views as v
from django.views.generic import TemplateView

urlpatterns = [
    path('', v.home.as_view()),
    path('mypage',TemplateView.as_view(template_name="mypage.html")),
    path('addEmp',v.addEmp.as_view()),
    path('InsertEmp',v.InsertEmp.as_view()),
    path('empList',v.empList.as_view()),
    path('deleteEmp/<int:pk>',v.deleteEmp.as_view()),
    path('eidtEmp/<int:pk>',v.eidtEmp.as_view()),


]

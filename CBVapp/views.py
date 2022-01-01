from django.shortcuts import render
from django.views.generic import TemplateView,UpdateView,DeleteView,FormView,CreateView,ListView
from .models import EmpForm,Emp

class home(TemplateView):
    template_name="home.html"

class addEmp(FormView):
    template_name="addEmp.html"
    form_class=EmpForm   

class InsertEmp(CreateView):
    model=Emp
    fields="__all__"
    success_url="/"

class empList(ListView):
    model=Emp
    template_name="empList.html"

class deleteEmp(DeleteView):
    template_name="delete_cnfrm.html"
    model=Emp
    success_url="/empList"

class eidtEmp(UpdateView):
    template_name="updateEmp.html"
    model=Emp
    success_url="/empList"
    fields="__all__"


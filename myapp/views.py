from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import View,FormView


# Create your views here.


from hr.forms import LoginForm

class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self, request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                login(request,user_object)
                print("success")
                return redirect("signin")
            print("failed")
            return render(request,"login.html",{"form":form})
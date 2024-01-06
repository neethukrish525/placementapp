from django.urls import path

from hr import views
urlpatterns =[
    path("signin",views,SignInView.as_views(),name="signin")
]
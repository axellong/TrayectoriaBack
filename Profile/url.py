from django.urls import path, re_path
from Profile import views


urlpatterns = [
    re_path(r'^profileModel_url', views.ProfileModelview.as_view()),
    re_path(r'^profileWeb_url', views.ProfileWebview.as_view()),
    
]
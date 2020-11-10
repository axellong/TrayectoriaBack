from django.urls import path, re_path
from Register import views

urlpatterns = [
    re_path(r'^', views.userModelWiev.as_view()),
]
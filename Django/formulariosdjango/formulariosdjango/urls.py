from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('form/', views.form, name="form"),
    path('goal/', views.goal, name='goal'),
    path('widget/', views.widget, name='widget')
]

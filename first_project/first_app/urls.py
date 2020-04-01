from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
]

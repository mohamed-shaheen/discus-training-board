from django.urls import path,include
from . import views




urlpatterns = [
    path('contact/', views.send_message,name='contactus' ),
]
from django.urls import path
from .views import register_view, logout_view, login_view, doctor_dashboard, nurse_dashboard, home
from typing import List
urlpatterns: List[path] = [
    path('', home, name='home'),  
    path('signup/', register_view, name='register'),
    path('login/', login_view, name='login'),  
    path('doctor/<int:doctor_id>/dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('nurse/<int:nurse_id>/dashboard/', nurse_dashboard, name='nurse_dashboard'),
    path('logout/', logout_view, name='logout'),
]

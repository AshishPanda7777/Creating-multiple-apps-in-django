from django.urls import path
from app1.views import*
app_name='app'
urlpatterns = [
    path('app/',app,name='app')
]

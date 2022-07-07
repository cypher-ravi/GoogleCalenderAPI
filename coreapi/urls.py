
from django.contrib import admin
from django.urls import path,include
from .views import *

appname = 'coreapi'

urlpatterns = [
    
    path('v1/calendar/init', GoogleCalendarInitView),
    path('v1/calendar/redirect', GoogleCalendarRedirectView),
]

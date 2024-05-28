from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mission_&_vision', views.mission, name='mission'),
    path('who-we-are', views.whoweare, name='who-we-are'),
    path('what-we-do', views.whatwedo, name='what-we-do'),
    path('who-we-work-with', views.whoweworkwith, name='who-we-work-with'),
    path('Jobs_&_Careers', views.careers, name='careers'),
    path('pblication', views.publication, name='publication'),
    path('contact', views.contact, name='contact'),
    path('apply', views.apply, name='apply'),
    
]
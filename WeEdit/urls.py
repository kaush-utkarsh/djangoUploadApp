"""WeEdit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from login import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signIn/', views.signIn),
    url(r'^signUp/', views.signUp),
    url(r'^signOut/', views.signOut),
    url(r'^checkout/', views.checkout),
    url(r'^portfolio/', views.portfolio),
    url(r'^refer/', views.refer),
    url(r'^dashboard/', views.dashboard),
    url(r'^new-project/', views.new_project),
    url(r'^create-project/', views.create_project),
    url(r'^upload-video-file/', views.upload_video_file),
    url(r'^upload-audio-file/', views.upload_audio_file),
    # url(r'^login/', views.home),
    url(r'^$', views.home),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
]

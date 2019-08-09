from alpha import views
from django.conf.urls import url
app_name='alpha'
urlpatterns=[
    url(r'^login/$', views.Login, name='login'),
    url(r'^logout/$', views.Logout, name='logout'),
    url(r'^home/$', views.Home, name='home'),
    url(r'^post/$', views.Post, name='post'),
    url(r'^message/$', views.Message, name='message'),
]

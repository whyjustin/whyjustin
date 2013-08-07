from django.conf.urls import patterns, url
from rest_framework import routers
from terminal import views

# restRouter = routers.DefaultRouter()
# restRouter.register(r'wpapi', views.ListPosts)

urlpatterns = patterns('',
	url(r'^/wpapi$', views.get_posts, name='getposts'),
	url(r'^/wpapi/(?P<id>\d+)$', views.get_post, name='getpost'),
	url(r'^$', views.index, name='index'),
	url(r'^/pacman$', views.pacman, name='pacman')
)
from datetime import datetime
from django.shortcuts import render
from json import loads
from os import path
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from terminal.serializers import PostSerializer
from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods.posts import GetPosts, GetPost

def index(request):
	wordpress_settings = get_wordpress_meta()
	first_post = get_first_post(wordpress_settings)
	return render(request, 'terminal/index.html', dict(post=first_post, wordpress=wordpress_settings["url"]))

def pacman(request):
	return render(request, 'terminal/pacman.html')

@api_view(['GET'])
def get_posts(request):
	wordpress_settings = get_wordpress_meta()
	wp = Client(wordpress_settings["rpc"], wordpress_settings["username"], wordpress_settings["password"])
	posts = wp.call(GetPosts({
			'order': 'DESC',
			'orderby': 'post_date_gmt'
		}));
	serializer = PostSerializer(posts)
	return Response(serializer.data)

@api_view(['GET'])
def get_post(request, id):
	wordpress_settings = get_wordpress_meta()
	wp = Client(wordpress_settings["rpc"], wordpress_settings["username"], wordpress_settings["password"])
	post = wp.call(GetPost({
		'post_id': id
		}));
	serializer = PostSerializer(post)
	return Response(serializer.data)

def get_wordpress_meta():
	loc = path.dirname(__file__);
	settings_loc = path.join(loc, '../conf/settings.json')
	settings_text = open(settings_loc, 'r').read()
	settings = loads(settings_text)
	return settings["wordpress"]

def get_first_post(wordpress_settings):
	wp = Client(wordpress_settings["rpc"], wordpress_settings["username"], wordpress_settings["password"])
	posts = wp.call(GetPosts({
			'number': 1,
			'order': 'DESC',
			'orderby': 'post_date_gmt'
		}));
	serializer = PostSerializer(posts)
	return serializer.data[0]
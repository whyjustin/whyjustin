from wordpress_xmlrpc import WordPressPost
from rest_framework import serializers

class PostSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	date = serializers.DateTimeField()
	title = serializers.CharField()
	content = serializers.CharField()
	excerpt = serializers.CharField()
	link = serializers.CharField()
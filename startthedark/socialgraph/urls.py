from django.conf.urls import include, url, patterns

urlpatterns = [
	url(r'^followers/(?P<username>[a-zA-Z0-9_-]+)/$',
		'friend_list',
		{'list_type': 'followers'},
		name = 'sg_followers'
	),
	url(r'^following/(?P<username>[a-zA-Z0-9_-]+)/$',
		'friend_list',
		{'list_type': 'following'},
		name = 'sg_followers'
	),
	url(r'^mutual/(?P<username>[a-zA-Z0-9_-]+)/$',
		'friend_list',
		{'list_type': 'mutual'},
		name = 'sg_followers'
	),
]

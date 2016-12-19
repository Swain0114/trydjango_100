from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', 'trydjango_100.hostsconf.urls', name='wildcard'),
)



'''
from trydjango_100.hostconf import urls as redirect_urls
host_patterns = patterns['',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', redirect_urls, name='wildcard'),
]
'''
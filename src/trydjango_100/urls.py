from django.conf.urls import url
from django.contrib import admin

from shortener.views import HomeView, shortCBView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+){6,15}/$', shortCBView.as_view()), #  trydjango_100/projects/ python regex
]

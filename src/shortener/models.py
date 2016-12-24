from django.conf import settings
from django.db import models

# from django.core.urlresolvers import reverse
from django_hosts.resolvers import reverse
# Create your models here.
from .utils import code_generator , create_shortcode
from .validators import validate_url, validate_dot_com

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class ShortenerManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(ShortenerManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs
    def refresh_shortcodes(self, items=None):
        # print(items)
        qs = shortener.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_code = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            print(q.id)
            new_code += 1
        return "New codes made: {i}".format(i=new_code)

class shortener(models.Model):
    url 	  = models.CharField(max_length=220, validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    update 	  = models.DateTimeField(auto_now=True)  # every time model is saved
    timestamp = models.DateTimeField(auto_now_add=True)  # when model was created
    active  = models.BooleanField(default=True)
    
    objects = ShortenerManager()
    

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        if 'http' not in self.url:
            self.url = 'http://' + self.url 
        super(shortener, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse("scode", kwargs={'shortcode':self.shortcode}, host='www', scheme='http')
        return url_path







    

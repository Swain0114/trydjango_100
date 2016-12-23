from django.db import models

# Create your models here.

from shortener.models import shortener

class ClickEventManager(models.Manager):
	def create_event(self, kitinstance):
		if isinstance(kitinstance, shortener):
			obj, created = self.get_or_create(kit_url=kitinstance)
			obj.count += 1
			obj.save()
			return obj.count
		return None

class ClickEvent(models.Model):
	kit_url   = models.OneToOneField(shortener) # asscociates two models
	count     = models.IntegerField(default=0)
	update 	  = models.DateTimeField(auto_now=True)  # every time model is saved
	timestamp = models.DateTimeField(auto_now_add=True)  # when model was created

	objects = ClickEventManager()

	def __str__(self):
		return "{i}".format(i=self.count)
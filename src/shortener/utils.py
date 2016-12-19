from django.conf import settings
import random
import string

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)
# from shortener.models import shortener  '''Can't import functions to eachother'''

def code_generator(size = SHORTCODE_MIN , chars = string.ascii_lowercase + string.digits):
	# new_code = ''
	# for _ in range(size):
	# 	new_code = new_code + random.choice(chars)
	# return new_code
	return ''.join(random.choice(chars) for _ in range(size)) # generator random char


def create_shortcode(instance, size = SHORTCODE_MIN):
	new_code = code_generator(size=size)
	# print(instance) 					# ex: http://google.com
	# print(instance.__class__)			# ex: <class 'shortener.models.shortener'>
	# print(instance.__class__.__name__)	# ex: shortener

	Sclass = instance.__class__
	qs_exists = Sclass.objects.filter(shortcode=new_code).exists()
	if qs_exists:
		return create_shortcode(size=size)
	return new_code


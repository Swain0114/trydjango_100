from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, Http404
from django.views import View

from analytics.models import ClickEvent

from .models import shortener
from .forms import SubmitUrlForm

# Create your views here.

# def home_view_fbv(request, *args, **kwargs):
# 	if request.method == "POST":
# 		print(request.POST)
# 	return render(request, "shortener/home.html", context)

class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {
			"title": "Kit.URL",
			"form": the_form
		}
		return render(request, "shortener/home.html", context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		context = {
			"title": "Kit.URL",
			"form": form
		}
		template = "shortener/home.html"
		if form.is_valid():
			new_url = form.cleaned_data.get("url")
			obj, created = shortener.objects.get_or_create(url=new_url)
			context = {
				"objects" : obj,
				"created" : created,
			}
			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/already-exists.html"
		return render(request, template , context)

class URLRedirectView(View): #  class based view
	def get(self, request, shortcode=None, *args, **kwargs):
		qs = shortener.objects.filter(shortcode__iexact=shortcode)
		if qs.count() != 1 and not qs.exists():
			raise Http404
		obj = qs.first()
		return HttpResponseRedirect(obj.url)




''' Function Based View '''
'''
def short_redirect_view(request, shortcode=None, *args, **kwargs): #  function based view
	# print(request.user)
	# print(request.user.is_authenticated())
	# objs = shortener.objects.get(shortcode = shortcode)
	print("Method is:\n")
	print(request.method)
	# GET THE 404 ERROR
	objs = get_object_or_404(shortener, shortcode=shortcode)
	# objs_url = objs.url
	# try:
	# 	objs = shortener.objects.get(shortcode=shortcode)
	# except:
	# 	objs = shortener.objects.all().first()

	# objs_url = None
	# qs = shortener.objects.filter(shortcode__iexact=shortcode.upper())
	# if qs.exists() and qs.count()==1:
	# 	objs = qs.first()
	# 	objs_url = objs.url
	return HttpResponse("Hello {sc}".format(sc=objs.url))
'''

from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .tasks import all_bucket_objects_task


class Home(View):
	def get(self, request):
		return render(request, 'core/home.html')


class BucketHome(LoginRequiredMixin, View):
	template_name = 'core/bucket.html'

	def get(self, request):
		objects = all_bucket_objects_task()
		return render(request, self.template_name, {'objects':objects})

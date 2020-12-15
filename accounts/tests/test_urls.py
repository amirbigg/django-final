from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import UserRegister, UserDashboard


class TestUrls(SimpleTestCase):
	def test_register(self):
		url = reverse('accounts:register') # /accounts/register
		self.assertEqual(resolve(url).func.view_class, UserRegister)

	def test_dashboard(self):
		url = reverse('accounts:dashboard', args=['amir',])
		self.assertEqual(resolve(url).func.view_class, UserDashboard)

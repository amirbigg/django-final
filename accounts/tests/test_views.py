from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.forms import UserRegistrationForm
from accounts.models import Profile


class TestView(TestCase):
	def setUp(self):
		self.client = Client()

	def test_user_register_GET(self):
		response = self.client.get(reverse('accounts:register'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'accounts/register.html')
		self.failUnless(response.context['form'], UserRegistrationForm)

	def test_user_register_POST_valid(self):
		response = self.client.post(reverse('accounts:register'), data={
			'username':'kevin',
			'email':'kevin@email.com',
			'password':'kevinpass'
		})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(User.objects.count(), 1)
		self.assertEqual(Profile.objects.count(), 1)

	def test_user_register_POST_invalid(self):
		response = self.client.post(reverse('accounts:register'), data={
			'username':'jack',
			'email':'invalid_email',
			'password':'jackpass',
		})
		self.assertEqual(response.status_code, 200)
		self.failIf(response.context['form'].is_valid())
		self.assertFormError(response, 'form', field='email', errors=['Enter a valid email address.'])

	def test_user_dashboard_GET(self):
		User.objects.create_user(username='jack', email='jack@email.com', password='jackpass')
		self.client.login(username='jack', password='jackpass')
		response = self.client.get(reverse('accounts:dashboard', args=['jack',]))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'accounts/dashboard.html')
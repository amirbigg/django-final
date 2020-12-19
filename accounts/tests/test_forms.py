from django.test import SimpleTestCase
from accounts.forms import UserRegistrationForm, ProfileImageForm
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile


class TestRegistrationFrom(SimpleTestCase):
	def test_valid_data(self):
		form = UserRegistrationForm(data={'username':'jack', 'email':'jack@email.com', 'password':'jackpass'})
		self.assertTrue(form.is_valid())

	def test_invalid_data(self):
		form = UserRegistrationForm(data={})
		self.assertFalse(form.is_valid())
		self.assertEqual(len(form.errors), 3)


# class TestProfileImageForm(SimpleTestCase):
# 	def test_valid_data(self):
# 		upload_file = open(f'{settings.AWS_LOCAL_STORAGE}/1.jpg', 'br')
# 		file_dict = {'file':SimpleUploadedFile(upload_file.name, upload_file.read())}
# 		form = ProfileImageForm(file_dict)
# 		self.assertTrue(form.is_valid())

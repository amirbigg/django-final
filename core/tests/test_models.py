from django.test import TestCase
from core.models import Question
from django.contrib.auth.models import User


class TestModel(TestCase):
	def setUp(self):
		user = User.objects.create_user(username='jack', email='jack@email.com', password='jackpass')
		self.question = Question.objects.create(
			user=user,
			title='This is test question',
			body='This is test question body'
		)

	def test_question_create(self):
		self.assertEqual(self.question.slug, 'this-is-test-question')

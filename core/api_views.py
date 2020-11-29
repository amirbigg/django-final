from rest_framework.views import APIView
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Question, Answer


class QuestionView(APIView):
	"""
		Retrieve, Create, Update, Delete question instances
	"""
	def get(self, request):
		questions = Question.objects.all()
		srz_data = QuestionSerializer(instance=questions, many=True).data
		return Response(srz_data, status=status.HTTP_200_OK)

	def post(self, request):
		pass

	def put(self, request, pk):
		pass

	def delete(self, request, pk):
		pass
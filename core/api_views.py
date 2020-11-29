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
		data = QuestionSerializer(data=request.data)
		if data.is_valid():
			data.save()
			return Response(data.data, status=status.HTTP_201_CREATED)
		return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk):
		question = Question.objects.get(pk=pk)
		srz_data = QuestionSerializer(instance=question, data=request.data, partial=True)
		if srz_data.is_valid():
			srz_data.save()
			return Response(srz_data.data, status=status.HTTP_200_OK)
		return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		question = Question.objects.get(pk=pk)
		question.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.game.models import Question, QuestionAnswer
from apps.game.serializers import QuestionSerializer, QuestionAnswerSerializer, UserAnswerCreateSerializer


class QuestionModelViewSet(ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ('get',)
    serializer_class = QuestionSerializer


class QuestionAnswersModelViewSet(ModelViewSet):
    queryset = QuestionAnswer.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ('get',)
    serializer_class = QuestionAnswerSerializer


class UserAnswerApiView(APIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'post')

    def post(self, request, format=None):
        serializer = UserAnswerCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

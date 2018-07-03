from rest_framework import serializers

from apps.game.models import Question, QuestionAnswer, UserAnswers
from apps.users.models import User


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = '__all__'


class UserAnswerCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        allow_null=False,
    )
    answer = serializers.PrimaryKeyRelatedField(
        queryset=QuestionAnswer.objects.all(),
        allow_null=False,
    )

    class Meta:
        model = UserAnswers
        fields = [
            'user',
            'answer',
        ]

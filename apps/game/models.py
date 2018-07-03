from django.db import models

from apps.users.models import User


class Question(models.Model):
    name = models.TextField(null=False, blank=False)

    def __str__(self):
        return 'Question: %s' % self.name

    class Meta:
        verbose_name_plural = 'Question'


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Question Answer'


class UserAnswers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    answer = models.ForeignKey(QuestionAnswer, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'User Answers'

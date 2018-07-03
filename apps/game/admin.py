from django.contrib import admin

from apps.game.models import Question, QuestionAnswer, UserAnswers


@admin.register(Question)
class QuestionModel(admin.ModelAdmin):
    list_display = [
        'id',
        'name'
    ]

    class Meta:
        model = Question


@admin.register(QuestionAnswer)
class QuestionAnswerModel(admin.ModelAdmin):
    list_display = [
        'question_name',
        'name',
        'is_correct',
    ]

    def question_name(self, obj):
        return obj.question.name

    class Meta:
        model = QuestionAnswer


@admin.register(UserAnswers)
class UserAnswersModel(admin.ModelAdmin):
    list_display = [
        'user_email',
        'answer_question',
        'answer_name',
        'answer_is_correct',
    ]

    def answer_is_correct(self, obj):
        return obj.answer.is_correct

    def answer_name(self, obj):
        return obj.answer.name

    def answer_question(self, obj):
        return obj.answer.question.name

    def user_email(self, obj):
        return obj.user.email

    class Meta:
        model = UserAnswers

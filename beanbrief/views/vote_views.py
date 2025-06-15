from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from ..models import Question, Answer
from ..services.question_service import QuestionService


@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    pybo 질문추천등록
    """
    question = Question.get_question_by_id(id=question_id)
    if QuestionService.check_author_permission(question, request.user):
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        QuestionService.add_voter(question, voter=request.user)
    return redirect('pybo:detail', question_id=question.id)


@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    """
    pybo 답글추천등록
    """
    answer = Answer.get_answer_by_id(id=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        answer.add_voter(voter=request.user)
    return redirect('pybo:detail', question_id=answer.question.id)

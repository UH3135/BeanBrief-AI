from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url

from ..forms import AnswerForm
from ..models import Question
from ..services.answer_service import AnswerService


@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    beanbrief 답변등록
    """
    question = Question.get_question_by_id(id=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = AnswerService.create_answer(
                author=request.user,
                question=question,
                content=form.cleaned_data['content']
            )
            return redirect('{}#answer_{}'.format(
                resolve_url('beanbrief:detail', question_id=question.id), answer.id))
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'beanbrief/question_detail.html', context)


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
    beanbrief 답변수정
    """
    answer = AnswerService.get_answer_by_id(id=answer_id)
    if not AnswerService.check_author_permission(answer, request.user):
        messages.error(request, '수정권한이 없습니다')
        return redirect('beanbrief:detail', question_id=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            AnswerService.update_answer(
                answer=answer,
                content=form.cleaned_data['content']
            )
            return redirect('{}#answer_{}'.format(
                resolve_url('beanbrief:detail', question_id=answer.question.id), answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'beanbrief/answer_form.html', context)


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """
    beanbrief 답변삭제
    """
    answer = AnswerService.get_answer_by_id(id=answer_id)
    if not AnswerService.check_author_permission(answer, request.user):
        messages.error(request, '삭제권한이 없습니다')
    else:
        AnswerService.delete_answer(answer)
    return redirect('beanbrief:detail', question_id=answer.question.id)

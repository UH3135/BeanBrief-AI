from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url

from ..forms import AnswerForm
from ..models import Question, Answer


@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = Question.get_question_by_id(id=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = Answer.create_answer(
                author=request.user,  # 추가한 속성 author 적용
                question=question,
                content=form.cleaned_data['content']
            )
            return redirect('{}#answer_{}'.format(
                resolve_url('pybo:detail', question_id=question.id), answer.id))
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
    pybo 답변수정
    """
    answer = Answer.get_answer_by_id(id=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer.update_answer(
                content=form.cleaned_data['content']
            )
            return redirect('{}#answer_{}'.format(
                resolve_url('pybo:detail', question_id=answer.question.id), answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """
    pybo 답변삭제
    """
    answer = Answer.get_answer_by_id(id=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete_answer()
    return redirect('pybo:detail', question_id=answer.question.id)

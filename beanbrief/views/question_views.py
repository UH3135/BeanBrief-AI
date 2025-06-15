from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import os

from ..forms import QuestionForm
from ..models import Question
from ..services.question_service import QuestionService


@login_required(login_url='common:login')
def question_create(request):
    """
    beanbrief 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            QuestionService.create_question(
                author=request.user,
                subject=form.cleaned_data['subject'],
                content=form.cleaned_data['content'],
                file=form.cleaned_data.get('file')
            )
            return redirect('beanbrief:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'beanbrief/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    beanbrief 질문수정
    """
    question = QuestionService.get_question_by_id(id=question_id)
    if not QuestionService.check_author_permission(question, request.user):
        messages.error(request, '수정권한이 없습니다')
        return redirect('beanbrief:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            if form.cleaned_data.get('delete_file') and question.file:
                # 실제 파일 삭제
                if os.path.exists(question.file.path):
                    os.remove(question.file.path)
                question.file = None
                
            QuestionService.update_question(
                question=question,
                subject = form.cleaned_data['subject'],
                content = form.cleaned_data['content'],
                file=form.cleaned_data.get('file')
            )
            return redirect('beanbrief:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'beanbrief/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    beanbrief 질문삭제
    """
    question = QuestionService.get_question_by_id(id=question_id)
    if not QuestionService.check_author_permission(question, request.user):
        messages.error(request, '삭제권한이 없습니다')
        return redirect('beanbrief:detail', question_id=question.id)
    QuestionService.delete_question(question)
    return redirect('beanbrief:index')

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url

from ..forms import CommentForm
from ..models import Question
from ..services.answer_service import AnswerService
from ..services.comment_service import CommentService


@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    """
    beanbrief 질문댓글등록
    """
    question = Question.get_question_by_id(id=question_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = CommentService.create_comment(
                author=request.user,
                content=form.cleaned_data['content'],
                question=question
            )
            return redirect('{}#comment_{}'.format(
                resolve_url('beanbrief:detail', question_id=comment.question.id), comment.id))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'beanbrief/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    """
    beanbrief 질문댓글수정
    """
    comment = CommentService.get_comment_by_id(id=comment_id)
    if not CommentService.check_author_permission(comment, request.user):
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('beanbrief:detail', question_id=comment.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            CommentService.update_comment(
                comment=comment, 
                author=request.user,
                content=form.cleaned_data['content']
            )
            return redirect('{}#comment_{}'.format(
                resolve_url('beanbrief:detail', question_id=comment.question.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'beanbrief/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    """
    beanbrief 질문댓글삭제
    """
    comment = CommentService.get_comment_by_id(id=comment_id)
    if not CommentService.check_author_permission(comment, request.user):
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('beanbrief:detail', question_id=comment.question_id)
    else:
        CommentService.delete_comment(comment)
    return redirect('beanbrief:detail', question_id=comment.question_id)


@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
    """
    beanbrief 답글댓글등록
    """
    answer = AnswerService.get_answer_by_id(id=answer_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = CommentService.create_comment(
                author=request.user,
                content=form.cleaned_data['content'],
                answer=answer
            )
            return redirect('{}#comment_{}'.format(
                resolve_url('beanbrief:detail', question_id=comment.answer.question.id), comment.id))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'beanbrief/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    """
    beanbrief 답글댓글수정
    """
    comment = CommentService.get_comment_by_id(id=comment_id)
    if not CommentService.check_author_permission(comment, request.user):
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('beanbrief:detail', question_id=comment.answer.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.update_comment(
                comment=comment,
                content=form.cleaned_data['content']
            )
            return redirect('{}#comment_{}'.format(
                resolve_url('beanbrief:detail', question_id=comment.answer.question.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'beanbrief/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    """
    beanbrief 답글댓글삭제
    """
    comment = CommentService.get_comment_by_id(id=comment_id)
    if not CommentService.check_author_permission(comment, request.user):
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('beanbrief:detail', question_id=comment.answer.question.id)
    else:
        CommentService.delete_comment(comment)
    return redirect('beanbrief:detail', question_id=comment.answer.question.id)

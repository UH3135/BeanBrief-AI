from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

from ..models import Question, Answer, Comment
from ..exceptions.comment import (
    CommentCreationError,
    CommentCallingError,
    CommentDeleteError,
    CommentUpdateError,
    CommentPermissionError
)


class CommentService:
    @classmethod
    def create_comment(cls, **kwargs) -> Comment:
        try:
            kwargs['create_date'] = timezone.now()
            return Comment.objects.create(**kwargs)
        except Exception as e:
            raise CommentCreationError(f"댓글 생성 중 오류가 발생했습니다. {str(e)}")
    
    @classmethod
    def get_comment_by_id(cls, id: int) -> Comment:
        try:
            return get_object_or_404(Comment, pk=id)
        except Exception as e:
            raise CommentCallingError(f"댓글 호출 중 오류가 발생했습니다. {str(e)}")        

    @classmethod
    def update_comment(cls, comment: Comment, **kwargs) -> Comment:
        try:
            kwargs['modify_date'] = timezone.now()
            for key, value in kwargs.items():
                setattr(Comment, key, value)
            comment.save()
            return comment
        except Exception as e:
            raise CommentUpdateError(f"댓글 수정 중 오류가 발생했습니다. {str(e)}")
    
    @classmethod
    def delete_comment(cls, comment: Comment) -> None:
        try:
            comment.delete()
        except Exception as e:
            raise CommentDeleteError(f"댓글 삭제 중 오류가 발생했습니다. {str(e)}")        

    @classmethod
    def check_author_permission(cls, comment: Comment, user: User) -> None:
        try:
            return comment.author == user
        except Exception as e:
            raise CommentPermissionError(f"댓글 권한 확인 중 오류가 발생했습니다. {str(e)}")        
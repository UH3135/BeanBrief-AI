from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone
from typing import List

from ..models import Question
from ..exceptions.question import (
    QuestionError,
    QuestionCreationError,
    QuestionUpdateError,
    QuestionDeleteError
)


class QuestionService:
    @staticmethod
    def create_question(author: User, subject: str, content: str, **kwargs) -> Question:
        try:
            return Question.objects.create(
                author=author,
                subject=subject,
                content=content,
                create_date=timezone.now(),
                **kwargs
            )
        except Exception as e:
            raise QuestionCreationError(f"질문 생성 중 오류가 발생했습니다. {str(e)}")
    
    @staticmethod
    def get_all_questions() -> List[Question]:
        try:
            return Question.objects.order_by('-create_date')
        except Exception as e:
            raise QuestionError(f"질문 호출 중 오류가 발생했습니다. {str(e)}")
    
    @staticmethod
    def get_question_by_id(id: int) -> Question:
        try:
            return get_object_or_404(Question, pk=id)
        except Exception as e:
            raise QuestionError(f"질문 {id} 호출 중 오류가 발생했습니다. {str(e)}")
    
    @staticmethod
    def update_question(question: Question, **kwargs) -> Question:
        try:
            for key, value in kwargs.items():
                setattr(question, key, value)
            question.modify_date = timezone.now()
            question.save()
            return question
        except Exception as e:
            raise QuestionUpdateError(f"질문 수정 중 오류가 발생했습니다. {str(e)}")
    
    @staticmethod
    def delete_question(question: Question) -> None:
        try:
            question.delete()
        except Exception as e:
            raise QuestionDeleteError(f"질문 삭제 중 오류가 발생했습니다. {str(e)}")
    
    @staticmethod
    def check_author_permission(question: Question, user: User) -> bool:
        try:
            return question.author == user
        except Exception as e:
            raise QuestionError(f"질문 수정 권한 확인 중 오류가 발생했습니다. {str(e)}")
    
    @staticmethod
    def add_voter(question: Question, voter: User):
        try:
            question.voter.add(voter)
        except Exception as e:
            raise QuestionError(f"투표 중 오류가 발생했습니다. {str(e)}")
    
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone
from typing import List

from ..models import Question, Answer
from ..exceptions.answer import (
    AnswerCreateError,
    AnswerCallingError, 
    AnswerUpdateError,
    AnswerDeleteError,
    AnswerPermissionError
)

class AnswerService:
    @classmethod
    def create_answer(cls, author: User, question: Question, content: str, **kwargs) -> Answer:
        try:
            return Answer.objects.create(
                author=author,
                question=question,
                content=content,
                create_date=timezone.now(),
                **kwargs
            )
        except Exception as e:
            raise AnswerCreateError(f"답변 생성 중 오류가 발생했습니다. {str(e)}")
    
    @classmethod
    def get_all_answers(cls) -> List[Answer]:
        try:
            return Answer.objects.order_by('-create_date')
        except Exception as e:
            raise AnswerCallingError(f"답변 호출 중 오류가 발생했습니다. {str(e)}")

    @classmethod
    def get_answer_by_id(cls, id: int) -> Answer:
        try:
            return get_object_or_404(Answer, pk=id)
        except Exception as e:
            raise AnswerCallingError(f"답변 호출 중 오류가 발생했습니다. Answer id: {id}  {str(e)}")

    @classmethod
    def update_answer(cls, answer: Answer, **kwargs) -> Answer:
        try:
            for key, value in kwargs.items():
                setattr(answer, key, value)
            answer.save()
            return answer
        except Exception as e:
            raise AnswerUpdateError(f"답변 수정 중 오류가 발생했습니다. {str(e)}")

    @classmethod
    def delete_answer(cls, answer: Answer) -> None:
        try:
            answer.delete()
        except Exception as e:
            raise AnswerDeleteError(f"답변 삭제 중 오류가 발생했습니다. {str(e)}")
    
    @classmethod
    def check_author_permission(cls, answer: Answer, user: User) -> bool:
        try:
            return answer.author == user
        except Exception as e:
            raise AnswerPermissionError(f"질문 수정 권한 확인 중 오류가 발생했습니다. {str(e)}")

    @classmethod
    def add_voter(cls, answer: Answer, voter: User):
        try:
            answer.voter.add(voter)
        except Exception as e:
            raise AnswerUpdateError(f"투표 중 오류가 발생했습니다. {str(e)}")
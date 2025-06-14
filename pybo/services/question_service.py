from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone
from typing import List

from ..models import Question
from ..exceptions.question import (
    QuestionCallingError,
    QuestionCreationError,
    QuestionUpdateError,
    QuestionDeleteError,
    QuestionPermissionError
)


class QuestionService:
    @classmethod
    def create_question(cls, author: User, subject: str, content: str, file=None,**kwargs) -> Question:
        try:
            return Question.objects.create(
                author=author,
                subject=subject,
                content=content,
                file=file,
                create_date=timezone.now(),
                **kwargs
            )
        except Exception as e:
            raise QuestionCreationError(f"질문 생성 중 오류가 발생했습니다. {str(e)}")
    
    @classmethod
    def get_all_questions(cls) -> List[Question]:
        try:
            return Question.objects.order_by('-create_date')
        except Exception as e:
            raise QuestionCallingError(f"질문 호출 중 오류가 발생했습니다. {str(e)}")
    
    @classmethod
    def get_question_by_id(cls, id: int) -> Question:
        try:
            return get_object_or_404(Question, pk=id)
        except Exception as e:
            raise QuestionCallingError(f"질문 호출 중 오류가 발생했습니다. id: {id} {str(e)}")
    
    @classmethod
    def update_question(cls, question: Question, **kwargs) -> Question:
        try:
            if 'file' in kwargs and not kwargs['file']: # 기존 파일 유지, None으로 덮어씌우는거 방지
                kwargs.pop('file')  
            
            for key, value in kwargs.items():
                setattr(question, key, value)
            question.modify_date = timezone.now()
            question.save()
            return question
        except Exception as e:
            raise QuestionUpdateError(f"질문 수정 중 오류가 발생했습니다. {str(e)}")
    
    @classmethod
    def delete_question(cls, question: Question) -> None:
        try:
            if question.file: # 질문에 파일 존재할 시, 파일도 삭제
                question.file.delete(save=False)
                
            question.delete()
        except Exception as e:
            raise QuestionDeleteError(f"질문 삭제 중 오류가 발생했습니다. {str(e)}")
    
    @classmethod
    def check_author_permission(cls, question: Question, user: User) -> bool:
        try:
            return question.author == user
        except Exception as e:
            raise QuestionPermissionError(f"질문 수정 권한 확인 중 오류가 발생했습니다. {str(e)}")
    
    @classmethod
    def add_voter(cls, question: Question, voter: User):
        try:
            question.voter.add(voter)
        except Exception as e:
            raise QuestionUpdateError(f"투표 중 오류가 발생했습니다. {str(e)}")
    
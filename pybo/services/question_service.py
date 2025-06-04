from django.contrib.auth.models import User

from ..models import Question
from ..exceptions.question import (
    QuestionError,
    QuestionCreationError,
    QuestionUpdateError,
    QuestionDeleteError
)


class QuestionService:
    @staticmethod
    def create_question(author: User, subject: str, content: str) -> Question:
        try:
            return Question.create_question(
                author=author,
                subject=subject,
                content=content
            )
        except Exception as e:
            raise QuestionCreationError(f"질문 생성 중 오류가 발생했습니다. {str(e)}")
    
    @staticmethod
    def get_question_by_id(id: int) -> Question:
        try:
            return Question.get_question_by_id(id=id)
        except Exception as e:
            raise QuestionError(f"질문 {id} 호출 중 오류가 발생했습니다. {str(e)}")
    
    @staticmethod
    def get_all_questions():
        try:
            return Question.get_all_questions()
        except Exception as e:
            raise QuestionError(f"질문 호출 중 오류가 발생했습니다. {str(e)}")
    
    @staticmethod
    def update_question(question: Question, subject: str, content: str) -> Question:
        try:
            return question.update_question(
                subject=subject,
                content=content
            )
        except Exception as e:
            raise QuestionUpdateError(f"질문 수정 중 오류가 발생했습니다. {str(e)}")
    
    @staticmethod
    def delete_question(question: Question) -> None:
        try:
            question.delete_question()
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
            question.add_voter(voter)
        except Exception as e:
            raise QuestionError(f"투표 중 오류가 발생했습니다. {str(e)}")
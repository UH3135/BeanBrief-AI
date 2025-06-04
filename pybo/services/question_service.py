from ..models import Question, User
from ..exceptions.question import QuestionCreationError


def create_question(author: 'User', subject: str, content: str, **kwargs):
    try:
        return Question.create_question(
            author=author,
            subject=subject,
            content=content,
            **kwargs
        )
    except Exception as e:
        raise QuestionCreationError(f"{str(e)}")
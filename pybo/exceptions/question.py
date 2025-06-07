from .base import PyboError

class QuestionError(PyboError):
    """질문 관련 기본 예외 클래스"""
    pass

class QuestionCreationError(QuestionError):
    """질문 생성 중 발생하는 오류"""
    pass

class QuestionUpdateError(QuestionError):
    """질문 수정 중 발생하는 오류"""
    pass

class QuestionDeleteError(QuestionError):
    """질문 삭제 중 발생하는 오류"""
    pass

class QuestionPermissionError(QuestionError):
    """권한 확인 중 발생하는 오류"""
    pass

class QuestionCallingError(QuestionError):
    """질문 호출 중 발생하는 오류"""
    pass

from .base import PyboError

class AnswerError(PyboError):
    """답변 관련 기본 예외 클래스"""
    pass

class AnswerCreateError(AnswerError):
    """답변 생성 중 발생하는 오류"""
    pass

class AnswerCallingError(AnswerError):
    """답변 조회 중 발생하는 오류"""
    pass

class AnswerUpdateError(AnswerError):
    """답변 수정 중 발생하는 오류"""
    pass

class AnswerDeleteError(AnswerError):
    """답변 삭제 중 발생하는 오류"""
    pass

class AnswerPermissionError(AnswerError):
    """답변 권한 확인 중 발생하는 오류"""
    pass
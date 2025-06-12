from .base import PyboError

class CommentError(PyboError):
    """댓글 관련 기본 예외 클래스"""
    pass

class CommentCreationError(CommentError):
    """댓글 생성 중 발생하는 오류"""
    pass

class CommentUpdateError(CommentError):
    """댓글 수정 중 발생하는 오류"""
    pass

class CommentDeleteError(CommentError):
    """댓글 삭제 중 발생하는 오류"""
    pass

class CommentPermissionError(CommentError):
    """권한 확인 중 발생하는 오류"""
    pass

class CommentCallingError(CommentError):
    """댓글 호출 중 발생하는 오류"""
    pass

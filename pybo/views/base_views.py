from django.core.paginator import Paginator
from django.shortcuts import render

from ..models import Question
from ..services.question_service import QuestionService


def index(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    question_list = QuestionService.get_all_questions()

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = QuestionService.get_question_by_id(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

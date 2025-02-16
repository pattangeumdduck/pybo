from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question

def index(request):
    """
    pybo 목록 출력 (주석으로 이 함수의 역할을 나타냄)
    """
    # 입력 인자
    page = request.GET.get('page', '1') #페이지
    kw = request.GET.get('kw', '')#검색어어

    #조회
    question_list = Question.objects.order_by('-create_date') 
    if kw:
        question_list - question_list.filter(
            Q(subject__icontails=kw)| # 제목 검색
            Q(content__icontains=kw)| # 내용 검색
            Q(author__username__icontailns=kw)| #질문 글쓴이 검색
            Q(answer__author__username__icontains=kw) #답변 글쓴이 검색색
        ).distinct()

    #페이징 처리 
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    
    #order_by 함수는 조회한 데이터를 특정 속성으로 정렬하며,'-create date'는 -기호가 붙어 작성일시의 역순을 의미함
    context = {'question_list': page_obj, 'page': page, 'kw':kw}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
from datetime import datetime

from django.shortcuts import render
from .models import Exhibition
from django.core.paginator import Paginator

def exhibition_list(request):
    # 정렬 방식
    order = request.GET.get("order")
    # default 정렬 방식, 마감이 임박한 순으로 정렬
    if order == "endDate" or order is None:
        exhibition_list = Exhibition.objects.all().order_by('ex_endDate')
    # 제목을 기준으로 사전순 정렬
    elif order == "title":
        exhibition_list = Exhibition.objects.all().order_by('ex_title')
    # 최근에 업데이트 된 순서로 정렬
    else:  # order == "recent_added":
        exhibition_list = Exhibition.objects.all().order_by('-pk')

    # 검색어 필터
    word = request.GET.get("word")
    # title이 word를 포함하고 있는 전시들을 반환
    if word is not None:
        exhibition_list = exhibition_list.filter(ex_title__contains=word)

    date_format = "%Y.%m.%d"

    # 시작일 필터
    start_date_string = request.GET.get("startDate")
    # 검색한 시작일 이후에 시작하는 전시들을 반환
    if start_date_string is not None:
        startDate = datetime.strptime(start_date_string, date_format).date()
        # gte는 greater than or equal, 크거나 같은 조건입니다.
        exhibition_list = exhibition_list.filter(ex_startDate__gte=startDate)

    # 종료일 필터
    end_date_string = request.GET.get("endDate")
    # 검색한 종료일 이전에 끝나는 전시들을 반환
    if end_date_string is not None:
        endDate = datetime.strptime(end_date_string, date_format).date()
        # lte는 less than or equal, 작거나 같은 조건입니다.
        exhibition_list = exhibition_list.filter(ex_startDate__lte=endDate)

    #페이지네이션, url에 page key를 넘기지 않았을 때는 자동으로 1페이지를 보여줍니다.
    paginator = Paginator(exhibition_list, 12)
    page = request.GET.get("page")
    exhibition_list = paginator.get_page(page)

    return render(request, "exhibitionList_sample.html",
                  {"exhibition_list": exhibition_list, "page": page})


# Create your views here.

from datetime import datetime

from django.shortcuts import render
from .models import Festival
from django.core.paginator import Paginator


def festival_list(request):
    # 정렬 방식
    order = request.GET.get("order")
    # default 정렬 방식, 마감이 임박한 순으로 정렬
    if order == "recent":
        festival_list = Festival.objects.all().order_by('-pk')
    # 제목을 기준으로 사전 순서로 정렬
    elif order == "title":
        festival_list = Festival.objects.all().order_by('fe_title')
    # 최근에 업데이트 된 순서로 정렬
    else:  # order == "endDate" or order is None:
        festival_list = Festival.objects.all().order_by('fe_endDate')

    # 검색어 필터
    title = request.GET.get("title")
    # title이 word를 포함하고 있는 축제들을 반환
    if title is not None:
        festival_list = festival_list.filter(fe_title__contains=title)

    date_format = "%Y.%m.%d"

    # 시작일 필터
    start_date_string = request.GET.get("startDate")
    # 검색한 시작일 이후에 시작하는 축제들을 반환
    if start_date_string is not None:
        startDate = datetime.strptime(start_date_string, date_format).date()
        # gte는 greater than or equal, 크거나 같은 조건입니다.
        festival_list = festival_list.filter(fe_startDate__gte=startDate)

    # 종료일 필터
    end_date_string = request.GET.get("endDate")
    # 검색한 종료일 이전에 끝나는 축제들을 반환
    if end_date_string is not None:
        endDate = datetime.strptime(end_date_string, date_format).date()
        # lte는 less than or equal, 작거나 같은 조건입니다.
        festival_list = festival_list.filter(fe_startDate__lte=endDate)

    #페이지네이션, url에 page key를 넘기지 않았을 때는 자동으로 1페이지를 보여줍니다.
    paginator = Paginator(festival_list, 12)
    page = request.GET.get("page")
    festival_list = paginator.get_page(page)

    return render(request, "festivals/festivalList.html",
                  {"festival_list": festival_list, "page": page, "order": order, "title": title})

# Create your views here.

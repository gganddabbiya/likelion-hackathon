from datetime import datetime

from django.shortcuts import render
from .models import Exhibition
from django.core.paginator import Paginator

def exhibition_list(request):
    # 정렬 방식
    order = request.GET.get("order")
    # 최근에 업데이트 된 순서로 정렬
    if order == "recent":
        exhibition_list = Exhibition.objects.all().order_by('-pk')
    #제목을 기준으로 사전 순서대로 정렬
    elif order == "title":
        exhibition_list = Exhibition.objects.all().order_by('ex_title')
    # default 정렬 방식, 마감이 임박한 순으로 정렬
    else:  #order == "endDate" or order is None or except...
        exhibition_list = Exhibition.objects.all().order_by('ex_endDate')

    # 검색어 필터
    title = request.GET.get("title")
    # title이 title을 포함하고 있는 전시들을 반환
    if title is not None:
        exhibition_list = exhibition_list.filter(ex_title__contains=title)

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

    return render(request, "exhibitions/exhibitionList_sample.html",
                  {"exhibition_list": exhibition_list, "page": page})


# Create your views here.
from django.shortcuts import get_object_or_404

def exhibition_detail(request, pk):
    # 특정 pk값을 가진 exhibiton 객체 가져오기
    # exhibition_detail = get_object_or_404(Exhibition, pk=pk)
    exhibition_detail = Exhibition.objects.get(pk=pk)
    print(exhibition_detail)

    return render(request, "exhibitions/exhibitionDetail.html", {'exhibition_detail': exhibition_detail})
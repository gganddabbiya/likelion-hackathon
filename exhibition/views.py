from datetime import datetime

from django.shortcuts import render
from .models import Exhibition
from django.core.paginator import Paginator

def exhibition_list(request):
    order = request.GET.get("order")
    if order == "endDate" or order is None :
        exhibition_list = Exhibition.objects.all().order_by('-ex_endDate')
    elif order == "title":
        exhibition_list = Exhibition.objects.all().order_by('ex_title')
    else:  # order == "recent":
        exhibition_list = Exhibition.objects.all().order_by('-pk')

    word = request.GET.get("word")
    if word is not None:
        print(word)
        exhibition_list = exhibition_list.filter(ex_title__contains=word)

    date_format = "%Y.%m.%d"
    start_date_string = request.GET.get("startDate")
    if start_date_string is not None:
        startDate = datetime.strptime(start_date_string, date_format).date()
        exhibition_list = exhibition_list.filter(ex_startDate__gte=startDate)

    end_date_string = request.GET.get("endDate")
    if end_date_string is not None:
        endDate = datetime.strptime(end_date_string, date_format).date()
        exhibition_list = exhibition_list.filter(ex_startDate__lte=endDate)


    paginator = Paginator(exhibition_list, 12)

    page = request.GET.get("page")

    exhibition_list = paginator.get_page(page)

    return render(request, "exhibitionList_sample.html",
                  {"exhibition_list": exhibition_list, "page": page})


# Create your views here.

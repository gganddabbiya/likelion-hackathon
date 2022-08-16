from datetime import datetime
from difflib import SequenceMatcher

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "woa_prj.settings")
django.setup()

from festival.models import Festival
from exhibition.models import Exhibition


def parse_date(string_date, dict, split):
    string_list =string_date.split(split)
    date_format = "%Y.%m.%d"
    start_date = datetime.strptime(string_list[0].strip(), date_format).date()
    if len(string_list) == 1:
        end_date = start_date
    elif len(string_list) == 2:
        if "오픈런" in string_list[1]:
            end_date = datetime.strptime("2099.12.31".strip(), date_format).date()
        else:
            end_date = datetime.strptime(string_list[1].strip(), date_format).date()
    dict["startDate"] = start_date
    dict["endDate"] = end_date


def festival_setdefault():
    dict = {}
    dict.setdefault("title")
    dict.setdefault("startDate")
    dict.setdefault("endDate")
    dict.setdefault("image")
    dict.setdefault("place")
    dict.setdefault("timeinfo", "제한 없음")
    dict.setdefault("link")
    dict.setdefault("age", "제한 없음")
    dict.setdefault("detail_img")
    return dict


def exhibition_setdefault():
    dict = {}
    dict.setdefault("title")
    dict.setdefault("startDate")
    dict.setdefault("endDate")
    dict.setdefault("image")
    dict.setdefault("place")
    dict.setdefault("timeinfo","제한 없음")
    dict.setdefault("link")
    dict.setdefault("age","제한 없음")
    dict.setdefault("detail_img")
    return dict


def duplicateCheck(dictList, type):
    print("중복 확인")
    if(type == "fe"):
        event = Festival.objects.all()
        for dict in dictList[:]:
            for comp in event:
                ratio = SequenceMatcher(None, dict['title'], comp.fe_title).ratio()
                if ratio > 0.8 and dict['startDate'] == comp.fe_startDate and dict['endDate'] == comp.fe_endDate:
                    print("중복 제외 :", dict['title'])
                    dictList.remove(dict)
                    break
    else:
        event = Exhibition.objects.all()
        for dict in dictList[:]:
            for comp in event:
                ratio = SequenceMatcher(None, dict['title'], comp.ex_title).ratio()
                if ratio > 0.8 and dict['startDate'] == comp.ex_startDate and dict['endDate'] == comp.ex_endDate:
                    print("중복 제외 :", dict['title'])
                    dictList.remove(dict)
                    break


def festival_save(dictList):
    for dict in dictList:
        Festival(fe_title=dict['title'],
                 fe_image=dict['image'],
                 fe_startDate=dict['startDate'],
                 fe_endDate=dict['endDate'],
                 fe_age=dict["age"],
                 fe_place=dict['place'],
                 fe_link=dict['link'],
                 fe_timeinfo=dict['timeinfo'],
                 fe_detail_img=dict["detail_img"]).save()
    print("저장 완료")


def exhibition_save(dictList):
    for dict in dictList:
        Exhibition(ex_title=dict['title'],
                   ex_startDate=dict['startDate'],
                   ex_endDate=dict['endDate'],
                   ex_image=dict['image'],
                   ex_place=dict['place'],
                   ex_timeinfo=dict['timeinfo'],
                   ex_age=dict["age"],
                   ex_link=dict['link'],
                   ex_detail_img=dict["detail_img"]).save()
    print("저장 완료")

#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.

def news_list(request):
    return JsonResponse({"state": "这是来自精英队的后台的回复！"})

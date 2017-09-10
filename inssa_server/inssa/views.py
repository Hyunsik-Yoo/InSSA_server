from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from inssa.models import *
from inssa.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
import operator


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET'])
def get_ranking(request):
    try:
        parm_score = request.GET['score']
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # DB에 저장한 뒤 랭킹계산
    if request.method == 'GET':
        score = MyScore(score=int(parm_score))
        score.save()


    # 순위와 상위 퍼센트 구하기
    list_score = list(MyScore.objects.all())
    list_score = sorted(list_score, key=operator.attrgetter('score'))
    list_score = [item.score for item in list_score]
    list_score.reverse()
    print(list_score)
    ranking = list_score.index(int(parm_score)) + 1
    percentage = ranking/len(list_score) * 100
    result = {'score':parm_score, 'ranking':ranking, 'percentage':percentage}

    return Response(result, status=status.HTTP_201_CREATED)

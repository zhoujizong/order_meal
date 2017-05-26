from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import MySQLdb
from .models import Question

conn = MySQLdb.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = 'zjz19931025',
        db = 'test',
        charset='utf8'
        )
cur = conn.cursor()
result = cur.execute("select * from test_table limit 10")
result_out = cur.fetchmany(result)

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
            'cate':['nvzhuang','meizhuang','nanzhuang'],
            'gmv':[100,200,30]
                    }
    return render(request, 'polls/index.html', context)
def detail(request, question_id):
        return HttpResponse("You're looking at question %s." % question_id)

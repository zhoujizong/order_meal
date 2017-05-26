from django.shortcuts import render
from django.http import HttpResponse
from ccj_dinner.models import staff_base_info,ordered_list,staff_action_log
import time
from django.db.models import Count, Min, Max, Sum

# Create your views here.

'''
from .forms import orderform
def order(request):
    if request.method == 'POST':
        form = orderform(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/order/')
    else:
        form = orderform()
    return render(request,'order.html',{'form':form})
'''

def get_curts():
    cur_time = time.time()
    cur_time_s = time.localtime(cur_time)
    cur_time_f = time.strftime('%Y%m%d',cur_time_s)
    cur_date_s = time.strptime(cur_time_f,'%Y%m%d')
    cur_date_ts = int(time.mktime(cur_date_s))
    return cur_date_ts

def order(request):
    if 'user_name' in request.POST:
        uname = request.POST['user_name']
        base_info = staff_base_info.objects.filter(staff_name=uname).values_list()
        if len(base_info)>0:
            staff_id_w = base_info[0][1]
            staff_name_w = base_info[0][2]
            group_name_w = base_info[0][3]
            create_time_w  = int(time.time())
            if 'od' in request.POST:
                type_w = 1
                staff_action_log.objects.create(staff_id = staff_id_w,staff_name = staff_name_w,group_name = group_name_w,create_time = create_time_w,type = type_w).save()
            if 'ca' in request.POST:
                type_w = 2
                staff_action_log.objects.create(staff_id = staff_id_w,staff_name = staff_name_w,group_name = group_name_w,create_time = create_time_w,type = type_w).save()
        table_content = staff_action_log.objects.filter(create_time__gte=get_curts()).values('group_name').annotate(count=Count('staff_id'))
        print table_content
        return render(request,'order.html',{'table_content':table_content})
    else:
        table_content = staff_action_log.objects.filter(create_time__gte=get_curts()).values('group_name').annotate(count=Count('staff_id'))
        print table_content
        return render(request,'order.html',{'table_content':table_content})



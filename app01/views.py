from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.

# def index(request):
#     if request.method == 'POST':
#         i1 = request.POST.get('i1')
#         i2 = request.POST.get('i2')
#         i3 = eval(f'{i1}+{i2}')
#         print(locals())
#     return render(request,'index.html',locals())

import time
@ensure_csrf_cookie
def index(request):
    return render(request,'index.html')
def calc1(request):
    if request.method == 'POST':
        i1 = request.POST.get('i1')
        i2 = request.POST.get('i2')
        i3 = eval(f'{i1}+{i2}')
        time.sleep(3)
        return HttpResponse(i3) #返回响应体让ajax接收
def calc2(request):
    if request.method == 'POST':
        i1 = request.POST.get('i1')
        i2 = request.POST.get('i2')
        i3 = eval(f'{i1}+{i2}')
        return HttpResponse(i3)

import json
def ajax_test(request):
    print(request.POST)
    #ajax直接传一个列表的情况下
    #<QueryDict: {'hobby[]': ['篮球', '足球', '排球']}>
    print(request.POST.getlist('hobby[]'))
    #['篮球', '足球', '排球']
    hobby= request.POST.get('hobby')
    print(hobby,type(hobby))
    #["篮球","足球","排球"] <class 'str'>
    hobby_json = json.loads(hobby)
    print(type(hobby_json))
    #<class 'list'>
    print(hobby_json)
    #['篮球', '足球', '排球']
    return HttpResponse('ok')

def upload(request):
    if request.is_ajax():
        print(request.FILES)
        #<MultiValueDict: {'f1': [<InMemoryUploadedFile: 55.jpg (image/jpeg)>]}>
        f1 = request.FILES.get('f1')
        print(f1)
        #55.jpg
        with open(f1.name,'wb') as f:
            for i in f1.chunks():
                f.write(i)
        # return HttpResponse('ok')
        return JsonResponse({'status':0,'msg':'上传成功'})
import json
def test_json(request):
    data = {'name':'alex','age':73}
    # return JsonResponse(data)
    return HttpResponse(json.dumps(data))
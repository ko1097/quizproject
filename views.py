from django.shortcuts import render
from .models import Socialquestion,Mathsquestion
from django.core.paginator import Paginator

# Create your views here.
lst =[]
anslist =[]
answers =Socialquestion.objects.all()

ls =[]
anlist =[]
answ =Mathsquestion.objects.all()

for i in answers:
    anslist.append(i.answer)

for i in answ:
    anlist.append(i.answer)
def home(request):
    lst.clear()

    return render(request,'home.html')

def main(request):
    obj = Socialquestion.objects.all()
    paginator = Paginator(obj,1)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page=1

    try:
        qu  = paginator.page(page)
    except(EmptyPage,InvaildPage):
        qu = paginator.page(page.num_pages)
    return render(request,'quiz1.html',{'obj':obj ,'qu':qu})



def quiz2(request):
    object = Mathsquestion.objects.all()
    paginator = Paginator(object,1)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page=1

    try:
        qu  = paginator.page(page)
    except(EmptyPage,InvaildPage):
        qu = paginator.page(page.num_pages)
    return render(request,'quiz2.html',{'object':object ,'qu':qu})

def result(request):

    score = 0
    for i in range(len(lst)):

        if lst[i]==anslist[i]:
            score +=1

    return render(request,'result.html',{'score':score})

def saveans(request):
    ans = request.GET['ans']
    lst.append(ans)

def resul(request):

    score = 0
    for i in range(len(ls)):

        if ls[i]==anlist[i]:
            score +=1

    return render(request,'result.html',{'scor':scor})

def saveas(request):
    an = request.GET['ans']
    ls.append(an)

from django.shortcuts import render, get_object_or_404
from .models import Bulletin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

# Create your views here.

# MVC의  controller 같은 기능
# .html 은 MVC의 view 같은 기능

def index(request):
    bulletin_list = Bulletin.objects.all().order_by('-writeDate')  # -: descending(최근일 위로)
    context = {'bulletin_list': bulletin_list}
    return render(request, 'bulletin/index.html', context)

def create_bulletin(request):
    return render(request, 'bulletin/create_bulletin.html')

def add_bulletin(request):
    bulletin = Bulletin()
    bulletin.title = request.POST['title']
    bulletin.content = request.POST['content']
    bulletin.name = request.POST['name']
    bulletin.passwd = request.POST['pincode']
    bulletin.save()

    return HttpResponseRedirect(reverse('bulletin_board:index'))

def view_bulletin(request, bulletin_id):
    bulletin = get_object_or_404(Bulletin, pk=bulletin_id)   # 해당 id로 data를 받아올 것인데 저 id가 없으면 404page를 띄워라
    return render(request, 'bulletin/detail.html', {'bulletin':bulletin})

def update_bulletin(request, bulletin_id):
    bulletin = Bulletin.objects.get(id=bulletin_id)

    if request.method == 'POST':
        bulletin.title = request.POST['title']
        bulletin.content = request.POST['content']
        bulletin.writeDate = timezone.datetime.now()
        bulletin.save()
        return HttpResponseRedirect(reverse('bulletin_board:view', args=(bulletin_id,)))
        # args=(bulletin_id,) : tuple은 리스트와 다르게 내용 수정 불가
        # tuple로 정수를 넘길 때는 (1,) 로 넘겨주기

    else:
        return render(request, 'bulletin/detail.html', {'bulletin':bulletin})

def delete_bulletin(request, bulletin_id):
    bulletin = Bulletin.objects.get(id=bulletin_id)
    bulletin.delete()
    return HttpResponseRedirect(reverse('bulletin_board:index'))
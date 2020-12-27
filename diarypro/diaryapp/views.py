from django.shortcuts import render,redirect
from .forms import DiaryForm
from .models import DiaryData
#from django.http.response import HttpResponse
import datetime

date1 = datetime.datetime.now()


def home_view(request):
    diary = DiaryData.objects.all()
    context = {'diary': diary}
    return render(request, 'diary/homepage.html', context)


def diary_view(request):
    if request.method == 'POST':
        dform = DiaryForm(request.POST, request.FILES)
        if dform.is_valid():
            title = dform.cleaned_data.get('title')
            body = dform.cleaned_data.get('body')
            img = dform.cleaned_data.get('img')
            img1 = dform.cleaned_data.get('img1')
            img2 = dform.cleaned_data.get('img2')
            img3 = dform.cleaned_data.get('img3')

            data = DiaryData(
                title=title,
                body=body,
                img=img,
                img1=img1,
                img2=img2,
                img3=img3,
                date=date1
            )
            data.save()
            dform = DiaryForm()
            context = {'dform': dform}
            return render(request, 'diary/diary.html', context)
    else:
        dform = DiaryForm()
        context = {'dform': dform}
        return render(request, 'diary/diary.html', context)


def update_diary(request, pk):
    diaryu = DiaryData.objects.get(id=pk)
    dform = DiaryForm(instance=diaryu)
    if request.method == 'POST':
        dform = DiaryForm(request.POST, request.FILES, instance=diaryu)
        if dform.is_valid():
            dform.save()
            return redirect('/')
    context = {'dform': dform}
    return render(request, 'diary/update_diary.html', context)


def delete_diary(request, pk):
    diaryd = DiaryData.objects.get(id=pk)
    diaryd.delete()
    return redirect('/')

from django.shortcuts import render


def mypage(request):
    return render(request, 'home.html')

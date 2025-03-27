from django.shortcuts import render


def index(request):
    return render(request, 'index_1_1.html')

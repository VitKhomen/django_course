from django.shortcuts import render
from django.http import HttpResponse
from http import HTTPStatus


def index(request):
    return render(request, 'index.html')


def bio(request, username):
    print(username)
    return render(request, 'index.html')


def year_archive(request, year):
    print(year)
    print(request)
    if year == 2003:
        return HttpResponse('special_case_2003')
    return HttpResponse(f'{year}')


def book(request, title):
    print(title)
    print(request)
    return HttpResponse(f'Book title is {title}')


def home(request):
    return render(request, 'train.html')


def bat_response(request, exception):
    response = HttpResponse(
        'NICE TRY\n\nGOOD LUCK NEXT TIME',
        content_type='text/plain',
    )
    response.status_code = HTTPStatus.NOT_FOUND
    return response

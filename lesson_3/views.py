import os
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, \
    HttpResponseNotAllowed, HttpResponseRedirect, JsonResponse
from django.conf import settings
from django.views import View
from django.template import loader


class MyView(View):

    def get(self, request):
        request_type = request.GET.get('type')
        if request_type == 'file':
            path_pic = os.path.join(settings.BASE_DIR, 'lesson_3',
                                    'static', 'img', '001.jpg')
            return FileResponse(open(path_pic, 'rb'))
        elif request_type == 'text':
            return HttpResponse("This is text from backend to user interface")
        elif request_type == 'redirect':
            return HttpResponseRedirect('http://www.twitch.tv')
        elif request_type == 'json':
            return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)
        elif request_type == 'json_homework':
            lets_do_it = [
                {'priority': 100, 'task': 'Составить список дел'},
                {'priority': 150, 'task': 'Изучать Django'},
                {'priority': 1, 'task': 'Подумать о смысле жизни'}
            ]
            return JsonResponse(lets_do_it, safe=False, json_dumps_params={'ensure_ascii': False})
        else:
            return HttpResponseNotAllowed('You shell not pass!!!')

    def post(self, request):
        print(request.POST)
        return HttpResponse('This is Post')


def main(request):
    test_template = loader.render_to_string('main.html',
                                            context={'lol': 'LOL', 'int': 1})
    return HttpResponse(test_template)


# def text(request):
#     return HttpResponse("This is text from backend to user interface")


# def file(request):
#     path_pic = os.path.join(settings.BASE_DIR, 'lesson_3',
#                             'static', 'img', '001.jpg')
#     return FileResponse(open(path_pic, 'rb'))


# def not_allowed(request):
#     return HttpResponseNotAllowed('You shell not pass!!!')


# def redirect(request):
#     return HttpResponseRedirect('http://www.google.com')


# def json(request):
#     return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)

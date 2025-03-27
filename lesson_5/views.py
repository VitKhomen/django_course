from django.http import HttpResponse

from uuid import uuid4
from decimal import Decimal
from django.core.files import File
from django.contrib.auth.models import User
from django.views.generic import ListView

from lesson_5.models import Flower, Bouquet, Client


def create_flower(request):
    flower = Flower()
    flower.count = 10
    # flower.description = "Роза является представителем семейства Разноцветных," \
    #     " рода Шиповник. Растение в большинстве случаев " \
    #     "представляет собой разветвленный кустарник, стебли" \
    #     " которого покрыты шипами, роза имеет зеленые листья" \
    #     " и большие ароматные цветы самого разного окраса"
    # flower.could_use_in_bouquet = True
    flower.wiki_page = "wiki page"
    flower.name = "Роза белая"
    flower.save()
    return HttpResponse('Created!!!')


def get_flower(request):
    price = Bouquet.shop.get(id=1).price
    return HttpResponse(price)


def create_client(request):

    Client.objects.create(**{
        'user': User.objects.get(pk=1),
        'second_email': 'admin@admin1.com',
        'name': 'MyName',
        'invoice': File(open('requirements.txt')),
        'user_uuid': uuid4(),
        'discount_size': Decimal("0.0052"),
        'client_ip': "192.0.2.1",
    }
    )
    return HttpResponse('client create')


class FlowerListViews(ListView):
    model = Flower
    template_name = 'flowers_list.html'
    context_object_name = 'flowers'
    queryset = Flower.objects.all()


class SearchFlowerViews(ListView):
    model = Flower
    template_name = 'flowers_list.html'
    context_object_name = 'flowers'

    def get_queryset(self):
        query = self.request.GET.get("q")  # Получаем значение из URL (?q=розы)
        queryset = Flower.objects.all()  # Загружаем все цветы

        if query:
            # Фильтрация по названию
            queryset = queryset.filter(name__icontains=query)

        return queryset

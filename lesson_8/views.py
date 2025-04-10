import csv
import datetime

from django.views.generic import ListView
from django.http import HttpResponse
from django.db.models import Q

from lesson_8.models import GameModel, GamerLibraryModel, GamerModel


def upload_data(request):
    with open('vgsales.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            try:
                _, created = GameModel.objects.get_or_create(
                    name=row[1],
                    platform=row[2],
                    year=datetime.date(int(row[3]), 1, 1),
                    genre=row[4],
                    publisher=row[5],
                    na_sales=row[6],
                    eu_sales=row[7],
                    jp_sales=row[8],
                    other_sales=row[9],
                    global_sales=row[10],
                )
            except:
                pass
    return HttpResponse("Done!")


class FilterView(ListView):
    template_name = 'gamemodel_list.html'
    # queryset = GameModel.objects.filter(na_sales__gt=30.0)
    queryset = GameModel.objects.filter(
        Q(name__startswith="A") & Q(name__endswith="a") & Q(
            name__contains="ma"))

    # queryset = GameModel.objects.filter(Q(name__endswith="a"),
    #                                     name__startswith="A")

    # queryset = GameModel.objects.filter(
    #     Q(name__startswith="Ab") | Q(name__startswith="Ad") | Q(
    #         name__startswith="Mat"))

    # queryset = GameModel.objects.filter(
    #     Q(name__startswith="Ab") | Q(name__startswith="Ad") | Q(
    #         name__startswith="Mat"))


def relation_filter_view(request):
    data = GamerLibraryModel.objects.filter(gamer__nickname__contains="My")
    print(data[0].gamer.email)
    # return HttpResponse(data)
    return HttpResponse(data.order_by())


class ExcludeView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(name__contains="Hitman")


class OrderByView(ListView):
    template_name = 'gamemodel_list.html'
    # TODO add reverse
    queryset = GameModel.objects.exclude(name__contains="Hitman").order_by(
        'year')


class AllView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.all()


class UnionView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name="Hitman (2016)").union(
        GameModel.objects.filter(name="Tetris"))


class NoneView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.none()


class ValuesView(ListView):
    template_name = 'gamemodel_list.html'

    queryset = GameModel.objects.filter(name__contains="Hitman").values("name",
                                                                        "platform",
                                                                        "year",
                                                                        "eu_sales")

    # def get(self, request, *args, **kwargs):
    #     print(GameModel.objects.filter(name="Hitman (2016)").values("name",
    #                                                                 "platform",
    #                                                                 "year"))
    #     print(list(
    #         GameModel.objects.all().values_list("name", 'year')))
    #     return super().get(request, *args, **kwargs)


def date_view(request):
    data = GameModel.objects.dates(field_name='year', kind='year')
    print(data)
    return HttpResponse(data)


def get_view(request):
    # TODO try error
    data = GameModel.objects.get(id=27)
    print(data)
    return HttpResponse(data)


def create_view(request):
    # myself = GamerModel()
    # myself.email = "admin@admin.com"
    # myself.nickname = "SomeRandomNicknameSave"
    # myself.save()

    # myself = GamerModel(email="admin@admin2.com",
    #                     nickname="SomeRandomNicknameSave2")
    # myself.save()
    #
    # myself = GamerModel(**{"email": "admin@admin3.com",
    #                        "nickname": "SomeRandomNicknameSave3"})
    # myself.save()

    # myself = GamerModel.objects.create(**{"email": "admin@admin4.com",
    #                                       "nickname": "SomeRandomNicknameCreate4"})

    # myself = GamerModel.objects.create(email="admin@admin.com",
    #                                    nickname="SomeRandomNicknameCreate")
    # myself = GamerModel.objects.bulk_create([
    #     GamerModel(
    #         email="admin@admin1.com", nickname="SomeRandomNicknameBulkCreate1"),
    #     GamerModel(
    #         email="admin@admin2.com", nickname="SomeRandomNicknameBulkCreate2"),
    #     GamerModel(
    #         email="admin@admin3.com", nickname="SomeRandomNicknameBulkCreate3"),
    #     GamerModel(
    #         email="admin@admin4.com", nickname="SomeRandomNicknameBulkCreate4")
    # ])

    # my_library = GamerLibraryModel(gamer=GamerModel.objects.get(pk=4),
    #                                size=1)
    # my_library.save()
    # my_library.game.set([GameModel.objects.get(pk=3),
    #                      GameModel.objects.get(pk=5)])

    # my_library = GamerLibraryModel.objects.create(
    #     gamer=GamerModel.objects.get(pk=10),
    #     size=10)
    # my_library.game.set([GameModel.objects.get(pk=1),
    #                      GameModel.objects.get(pk=2)])

    # my_library = GamerLibraryModel.objects.bulk_create(
    #     [GamerLibraryModel(gamer=GamerModel.objects.get(pk=10),
    #                        size=10),
    #      GamerLibraryModel(gamer=GamerModel.objects.get(pk=10),
    #                        size=10)
    #      ])
    GamerModel.objects.filter(
        pk=5).update(nickname="MySecondNickname")

    return HttpResponse("DONE!")

from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'homework.html'


class CharacterTemplateView(TemplateView):
    template_name = 'character_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = kwargs.get("name")
        characters = {
            'Luk': {
                'name': 'Люк Скайуокер',
                'description': 'Один из главных персонажей вселенной «Звёздных войн», джедай, сын сенатора с Набу Падме Амидалы Наберри и рыцаря-джедая Энакина Скайуокера.'
            },
            'Лея': {
                'name': 'Лея Органа',
                'description': 'Дочь рыцаря-джедая Энакина Скайуокера и сенатора Падме Амидалы Наберри.'
            },
            'Хан': {
                'name': 'Хан Соло',
                'description': 'Пилот космического корабля «Тысячелетний сокол», его бортмехаником и вторым пилотом является вуки по имени Чубакка.'
            },
        }
        context["character"] = characters.get(name, None)
        return context


class TaskThreeView(TemplateView):
    template_name = 'character_home.html'

    def get_context_data(self, **kwargs):
        return {
            'name_list': [
                {'name': 'Шаддам IV', 'surname': 'Коррино'},
                {'name': 'Пол', 'surname': 'Атрейдес'},
                {'name': 'Франклин', 'surname': 'Герберт'}
            ]
        }

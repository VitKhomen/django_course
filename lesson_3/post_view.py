from django.http import HttpResponse
# from django.template import loader

from django.views.generic import TemplateView


class MyTemplateView(TemplateView):
    template_name = 'post_page.html'

    def get_context_data(self, **kwargs):
        return {'questions_list':
                [
                    {'id': 5, 'question_text': 'look at my horse?'},
                    {'id': 1, 'question_text': 'В чем смысл жзн?'},
                    {'id': 2, 'question_text': 'Что первично, дух или материя?'},
                    {'id': 3, 'question_text': 'Существует ли свобода воли?'},
                    {'id': 7, 'question_text': ''},
                ]
                }


# def index_post(request):
#     questions_list = [
#         {'id': 5, 'question_text': 'look at my horse?'},
#         {'id': 1, 'question_text': 'В чем смысл жзн?'},
#         {'id': 2, 'question_text': 'Что первично, дух или материя?'},
#         {'id': 3, 'question_text': 'Существует ли свобода воли?'},
#         {'id': 7, 'question_text': ''},
#     ]
#     template = loader.get_template('post_page.html')
#     context = {'questions_list': questions_list}
#     return HttpResponse(template.render(context, request))


def post_page(request, number):
    if number == 1:
        return HttpResponse(
            "Кто-то или что-то на славу потрудилось, "
            "придумав нас настолько непохожими друг на друга,"
            " но в одном это что-то явно загналось несильно,"
            " а именно в человеческой необходимости стремиться"
            " к чему-либо. Да, каждый человек уникален,"
            " но не существует ни одной жизни, в которой не"
            " было бы мечт, желаний, и целей, ведь все мы куда-то"
            " движемся в нашем существовании, нам важно чего-то достичь,"
            " никто из нас не хочет прожить зря.")
    elif number == 2:
        return HttpResponse(
            "Обычно проблематизируется в форме вопроса:"
            " «Что первично, дух или материя?»."
            " Марксизм выделяет два основных варианта"
            " решения основного вопроса философии:"
            " материализм, при котором материя обладает"
            " преимуществом по отношению к сознанию,"
            " и идеализм, при котором идея первична к материи.")
    elif number == 5:
        return HttpResponse("My horse is amazing\n"
                            " give it a lick\n"
                            " It tastes just like raisins")
    elif number == 3:
        return HttpResponse(
            "В наше время любят говорить: "
            "свободы воли не существует (речь идет о"
            " свободе человека как мыслящего и действующего"
            " существа). В современной философии подобные идеи можно"
            " подвести под рубрику «физикализм». В простейшем"
            " обобщении физикализм утверждает, что представление о "
            "свободе воли (или, иначе, возможности выбора) есть чистейшая"
            " иллюзия, мы функционируем по программе, «встроенной» в нас"
            " природой, и свободы у нас не больше, чем у растения или"
            " животного.")
    else:
        return HttpResponse("Другой вопрос")

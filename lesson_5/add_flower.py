from lesson_5.models import Flower

flowers = [
    {"name": "Ирис", "count": 5, "description": "Ирис японский"},
    {"name": "Тюльпан", "count": 15, "description": "Желтый тюльпан"},
    {"name": "Лилия", "count": 10, "description": "Белаялилия"},
]

for flower in flowers:
    Flower.objects.create(**flower)


# exec(open("lesson_5/add_flower.py", encoding="utf-8").read())

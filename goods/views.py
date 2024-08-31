from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Меню",
        "goods_1": [
            {
                "image": "deps/images/goods/california.jpg",
                "name": "Роллы «Калифорния»",
                "description": "Классические роллы с крабовыми палочками, авокадо и огурцом, завернутые в рис и нори, подаются с кунжутом.",
                "price": 400.00,
            },
            {
                "image": "deps/images/goods/sushi ugor.jpg",
                "name": "Суши с угрём",
                "description": "Нежные кусочки свежего угря, маринованного в соевом соусе и сахаре, подаются на рисе, украшенном васаби и маринованным имбирем.",
                "price": 500.00,
            },
            {
                "image": "deps/images/goods/krevetki tempura.jpg",
                "name": "Темпура с креветками",
                "description": "Сочные креветки, обжаренные в хрустящем кляре, подаются с соусом для темпуры.",
                "price": 500.00,
            },
            {
                "image": "deps/images/goods/miso soup chicken.jpg",
                "name": "Суп мисо с курицей",
                "description": "Традиционный японский суп на основе мисо-пасты с добавлением курицы, водорослей нори, тофу и зеленого лука.",
                "price": 350.00,
            },
        ],
        "goods_2": [
            {
                "image": "deps/images/goods/cheesecake tea.jpg",
                "name": "Чизкейк с зелёным чаем",
                "description": "Воздушный чизкейк с нежным вкусом зеленого чая, подается с соусом из зеленого чая.",
                "price": 300.00,
            },
            {
                "image": "deps/images/goods/drakon.jpg",
                "name": "Роллы «Дракон»",
                "description": "Классические роллы с нежным угрем, хрустящим огурцом и кремовым авокадо. Икра тобико придает пикантность и праздничный вид.",
                "price": 400.00,
            },
            {
                "image": "deps/images/goods/ceaser.jpg",
                "name": "Роллы «Цезарь»",
                "description": "Необычное сочетание японских и европейских вкусов: сочная курица, пикантный сыр Пармезан и свежие овощи.",
                "price": 350.00,
            },
            {
                "image": "deps/images/goods/nigiri krevetka.jpg",
                "name": "Нигири с креветкой",
                "description": "Нежное и сочное нигири с креветкой на подушке из риса. ",
                "price": 160.00,
            },
        ],
        "goods_3": [
            {
                "image": "deps/images/goods/edamame.jpg",
                "name": "Салат «Эдамаме»",
                "description": "Простой и полезный салат из вареной сои, дополненный кунжутом и соевым соусом.",
                "price": 200.00,
            },
            {
                "image": "deps/images/goods/black kunzhut.jpg",
                "name": "Салат «Чёрный кунжут»",
                "description": "Легкий и освежающий салат с листьями салата, огурцом, помидором, кунжутом и соусом.",
                "price": 220.00,
            },
            {
                "image": "deps/images/goods/chicken_yakisoba.jpg",
                "name": "Якисоба с курицей",
                "description": "Вкусная лапша со специями, курицей и овощами.",
                "price": 300.00,
            },
            {
                "image": "deps/images/goods/yakitori.jpg",
                "name": "Якитори",
                "description": "Сочные куриные шашлычки на шпажках, приготовленные в сладком и соевом соусе терияки.",
                "price": 250.00,
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")

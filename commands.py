# from news.models import *
#
#
# 1. Создать двух пользователей (с помощью метода User.objects.create_user('username')).
# u1 = User.objects.create_user('Никита')
# u2 = User.objects.create_user('Карина')
#
# 2. Создать два объекта модели Author, связанные с пользователями.
# Author.objects.create(nickname = u1)
# Author.objects.create(nickname = u2)
# author = Author.objects.get(id=1)
# author2 = Author.objects.get(id=2)
#
# 3. Добавить 4 категории в модель Category.
# Category.objects.create(title = 'Погода')
# Category.objects.create(title = 'Спорт')
# Category.objects.create(title = 'Политика')
# Category.objects.create(title = 'Криминал')
#
# 4. Добавить 2 статьи и 1 новость.
# Post.objects.create(author=author, categoryType = 'NW', title = 'Прогноз аномалий на сентябрь в России', text='Наиболее крупные аномалии (до 2–3 градусов) традиционно придутся на высокие широты (Русский Север, Ямал, Таймыр, Эвенкию, субарктическую Якутию и Чукотку). Умеренно тепло (аномалии 1–2 градуса) следует ожидать на Северном Кавказе, Урале, в Сибири и Приморье и на Сахалине. По осадкам существенных аномалий не прогнозируется, за исключением юга Дальнего Востока. В Приморье и Хабаровском крае вероятно превышение нормы на 20–40 %.')
# Post.objects.create(author=author, categoryType = 'AR', title = 'Допинг в спорте', text='Допинги – это специальные лекарственные препараты, употребляемые спортсменами для принудительного повышения работоспособности организма во время соревновательной деятельности или же в период учебно-тренировочного процесса. На то, какими свойствами обладает тот или иной допинг влияет вид спорта, для которого он предназначен. В общем, фармакологические действия данных лекарственных препаратов могут быть совершенно противоположными. Как правило, назначение допинга происходит курсом, но зачастую встречаются случаи однократного употребления. Всё зависит от поставленных задач, а также механизма действия определённого лекарственного вещества.')
# Post.objects.create(author=author2, categoryType = 'AR', title = 'Политика и спорт', text='В XXI в. спорт стал неотъемлемой частью политики, инструментом формирования позитивного имиджа страны. Статья посвящена исследованию спорта в качестве одного из основных ресурсов политики «мягкой силы» государства. В работе исследуется опыт применения подобного инструмента как в зарубежных странах - Южной Корее, Китае, США, так и в России, анализируются методы реализации странами политики «мягкой силы» в сфере спорта.')
#
# 5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
# Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
# Post.objects.get(id=2).postCategory.add(Category.objects.get(id=2))
# Post.objects.get(id=3).postCategory.add(Category.objects.get(id=2))
# Post.objects.get(id=3).postCategory.add(Category.objects.get(id=3))
#
# 6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
# Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).nickname, text='Необыкновенно интересно.')
# Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=1).nickname, text='Допинг - дело добровольное.')
# Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=2).nickname, text='Политике в спорте не место!')
# Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=2).nickname, text='Спорт всему голова!')
# Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).nickname, text='Страшная аномалия.')
# Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=2).nickname, text='Уф какой кошмар!')
#
# 7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
# for i in range(30):
#     Post.objects.get(id=1).like()
# for i in range(17):
#     Post.objects.get(id=2).like()
# for i in range(37):
#     Post.objects.get(id=3).like()
#
# for i in range(7):
#     Comment.objects.get(id=1).like()
# for i in range(5):
#     Comment.objects.get(id=2).like()
# for i in range(9):
#     Comment.objects.get(id=3).like()
# for i in range(12):
#     Comment.objects.get(id=4).like()
#
# Comment.objects.get(id=2).dislike()
#
# 8. Обновить рейтинги пользователей.
# a = Author.objects.get(id=1)
# b = Author.objects.get(id=2)
# a.update_rating()
# b.update_rating()
# a.ratingAuthor
# b.ratingAuthor
#
# 9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
# Author.objects.all().order_by('-ratingAuthor').values('nickname__username', 'ratingAuthor')[0]
#
# 10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дизлайках к этой статье.
# print(Post.objects.all().order_by('-rating').values('dataCreation', 'author__nickname__username', 'rating', 'title')[0],
#       Post.objects.all().order_by('-rating')[0].preview())
#
# 11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
# print(Post.objects.all().order_by('-rating')[0].comment_set.all().values('dateCreation', 'commentUser__username', 'text'))
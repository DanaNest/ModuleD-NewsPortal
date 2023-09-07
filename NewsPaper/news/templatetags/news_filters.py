from django import template

register = template.Library()

CENSOR_LIST = [
    'сентябрь',
    'Допинг',
    'спорт',
    'гимназии',
]


@register.filter(name='censor')
def news_filter(text: str):
    text_split = text.split()  # разбиваем текст на слова

    for i, word in enumerate(text_split):
        if word[0].lower() + word[1:] in CENSOR_LIST:
            text_split[i] = word[0] + (len(word) - 1) * '*'
    return ' '.join(text_split)  # соединяем слова в текст

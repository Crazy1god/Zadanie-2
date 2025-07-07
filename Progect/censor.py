from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    bad_words = ['редиска', 'огурец'] # Список нежелательных слов
    for word in bad_words:
        value = value.replace(word, '*' * len(word))
    return value

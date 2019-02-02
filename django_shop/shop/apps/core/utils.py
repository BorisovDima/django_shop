from django.utils.text import slugify

def my_slugify(string):
    return slugify(string, allow_unicode=True)[:64]
import random
import os
from django import template
from shopping.settings import BASE_DIR

register = template.Library()

@register.filter
def get_first_image(category,title):
    try:
        path = os.path.join(BASE_DIR,'media',category,title)
        list_images = os.listdir(path=path)
        return list_images[0].replace(" ","%20")
    except:
        return "ggghghf"

@register.filter
def encode_space(title):
    return title.replace(" ","%20")

@register.filter
def get_categories(title):
    path = os.path.join(BASE_DIR, 'media')
    return os.listdir(path=path)

@register.filter
def get_image_list(category,title):
    path = os.path.join(BASE_DIR, 'media', category, title)
    list_images = os.listdir(path=path)
    return list_images

@register.filter
def get_rand(num):
    return random.randint(10,num)
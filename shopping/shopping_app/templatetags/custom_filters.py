import random
import os
from django import template
from shopping.settings import BASE_DIR

register = template.Library()

@register.filter
def get_first_image(category,title):
        path = os.path.join(BASE_DIR,'media',category,title)
        list_images = os.listdir(path=path)
        return list_images[0].replace(" ","%20")

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
def get_cat_items(category):
    path = os.path.join(BASE_DIR, 'media', category)
    list_items = os.listdir(path=path)
    title =  random.choice(list_items).replace(" ","%20")
    path = os.path.join(BASE_DIR, 'media', category, title)
    list_images = os.listdir(path=path)
    return title+"/"+list_images[0].replace(" ", "%20")

@register.filter
def get_rand(num):
    return random.randint(10,num)

@register.filter
def getrandcategory(num):
    cat_list = ["latest","trends","newest"]
    return random.choice(cat_list)
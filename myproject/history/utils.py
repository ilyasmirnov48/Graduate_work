from django.db.models import Count

from .models import *


menu = [
    {'title': "Истории", 'url_name': 'stories'},
    {'title': "Видео", 'url_name': 'video'},
    {'title': "Фотографии", 'url_name': 'photo'},
]


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('stories'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

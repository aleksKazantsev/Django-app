from blog.models import *

menu = [
    {'title': 'Добавить пост', 'url_name': 'add_post'},
    {'title': 'Регистрация', 'url_name': 'register'},
    {'title': 'Войти', 'url_name': 'login'},
    {'title': 'Выход', 'url_name': 'logout'}
]

class DataMixin:
    paginate_by = 2
    
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            #delit private item menu 
            user_menu.pop(0)
            user_menu.pop(2)
        else:
            user_menu.pop(1)
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
            
        return context


    
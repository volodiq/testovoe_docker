from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Главная страница сайта"""
    template_name = "index/index.html"

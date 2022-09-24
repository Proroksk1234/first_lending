from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60)(views.Home), name='home'),
    path('done', (views.Done.as_view())),
]
# cache_page(60)
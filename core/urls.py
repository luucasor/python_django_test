from django.conf.urls import url
from core.views import home, lista, novo, atualiza, deleta

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^lista-todos/$', lista, name='lista_todos'),
    url(r'^novo/$', novo, name='novo'),
    url(r'^atualizar/(?P<id>\d+)/$', atualiza, name='atualizar'),
    url(r'^deletar/(?P<id>\d+)/$', deleta, name='deletar'),
]

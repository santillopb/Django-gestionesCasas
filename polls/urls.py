from django.conf.urls import url

from . import views
from . import month_cal

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    #url(r'^$', views.index, name='index'),
    url(r'^cases/$', views.CasesView.as_view(), name='cases'),
    # ex: /polls/5/
    #the 'name' value as called by the {% url %} template tag
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^cases/(?P<cases_id>[0-9]+)/persona$', views.casesDetail, name='detail'),
    url(r'^persona/(?P<persona_id>[0-9]+)/factura$', views.factura, name='detail_persona'),
    url(r'^factura/(?P<persona_id>[0-9]+)/insercio$', views.save_factura, name='factura_nova'),
    url(r'^nota/(?P<persona_id>[0-9]+)/insercio$', views.anade_nota, name='insercio_nota'),
    #url(r'^cases/(?P<pk>[0-9]+/))
    # added the word 'specifics'
    #url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<cases_id>[0-9]+)/vote/$', views.vote, name='vote'),
    #url(r'^calendar/$', views.CalendarView.as_view(), name='calendar')
    url(r'^users/$', views.UsersView.as_view(), name='users'),
    #url(r'^xat/$', views.XatView.as_view(), name='xat'),
    url(r'^xat/$', views.xat, name='xat'),
    url(r'^users/(?P<pk>[0-9]+)/user_detail/$', views.UserDetailView.as_view(), name='user_detail'),
    #url(r'^nota/$', views.NotaView.as_view(), name='nota'),
    #url(r'^nota2/(?P<year>\d{4})/$', views.nota, name='nota2'),
    url(r'^calendario2/$', views.calendar2, name='calendar2'),
    url(r'^calendario/$', views.calendario, name='calendar'),
    #url(r'^calendar_month/$', views.calendar_month, name='calendar_month'),
    #url(r'^calendar_month/(?P<year>[0-9]{4})/(?P<month>[01]*[0-9]+)/$', views.calendar_month_day, name='calendar_month_day'),
    #url(r'^blog/(?P<year>\d{4})/(?P<month>[01]*[0-9]+)/(?P<day>[0-3]*[0-9]+)$',views.EntradasDia.as_view(), name='entradas'),
    #url(r'^blog/(?P<year>\d{4})/(?P<month>[01]*[0-9]+)/$',views.EntradasMes.as_view(), name='entradas'),
    #url(r'^blog/(?P<year>\d{4})/$',
    #views.EntradasYear.as_view(), name='entradas_year'),
    #url(r'^blog/(?P<year>\d{4})/$',
    #views.year, name='entradas_year'),
    #url(r'^blog/$', views.BlogView.as_view(), name='blog'),
    url(r'^persona/(?P<persona_id>[0-9]+)/blog/$', views.blog, name='blog'),
    url(r'^iframe/$', views.iframe, name='iframe'),
    url(r'^persona/(?P<persona_id>[0-9]+)/btc_address/$', views.btc_address, name='bit_address'),

]


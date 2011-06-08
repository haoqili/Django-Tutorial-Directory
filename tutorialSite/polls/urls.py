from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from polls.models import Poll

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='polls/index.html')),

    # pk = primary key for DetailView = poll_id below
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/detail.html')),

    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/results.html'),
        name='poll_results'),

    (r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)

#1  from django.conf.urls.defaults import patterns, include, url
#1 
#1  urlpatterns = patterns('polls.views',
#1      (r'^$', 'index'),
#1      (r'^(?P<poll_id>\d+)/$', 'detail'),
#1      (r'^(?P<poll_id>\d+)/results/$', 'results'),
#1      (r'^(?P<poll_id>\d+)/vote/$', 'vote'),
#1  )

    # Examples:
    # url(r'^$', 'tutorialSite.views.home', name='home'),
    # url(r'^tutorialSite/', include('tutorialSite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),

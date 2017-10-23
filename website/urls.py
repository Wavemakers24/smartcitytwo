from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from website.views import HomeView

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'website/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'website/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    # url(r'^link/$', views.link, name='link'),
    url(r'^detail/$', HomeView.as_view(), name='detail'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    #url(r'^/$', views., name=''),
    url(r'^search/$', views.search, name='search'),
    url(r'^statelibraryofqueensland$', views.statelibraryofqueensland, name='statelibraryofqueensland'),
    url(r'^qutgardenspointlibrary$', views.qutgardenspointlibrary, name='qutgardenspointlibrary'),
    url(r'^brisbanesquarelibrary$', views.brisbanesquarelibrary, name='brisbanesquarelibrary'),
    url(r'^citybotanicgardens$', views.citybotanicgardens, name='citybotanicgardens'),
    url(r'^kangaroopointcliffspark$', views.kangaroopointcliffspark, name='kangaroopointcliffspark'),
    url(r'^romastreetparkland$', views.romastreetparkland, name='romastreetparkland'),
    url(r'^storybridge$', views.storybridge, name='storybridge'),
    url(r'^victoriabridge$', views.victoriabridge, name='victoriabridge'),
    url(r'^kurilpabridge$', views.kurilpabridge, name='kurilpabridge'),
    url(r'^goodwillbridge$', views.goodwillbridge, name='goodwillbridge'),
    url(r'^angelospastafactory$', views.angelospastafactory, name='angelospastafactory'),
    url(r'^noosachocolatefactory$', views.noosachocolatefactory, name='noosachocolatefactory'),
    url(r'^theglassfactory$', views.theglassfactory, name='theglassfactory'),
    url(r'^queenslandpolicemuseum$', views.queenslandpolicemuseum, name='queenslandpolicemuseum'),
    url(r'^queenslandmuseumandsciencentre$', views.queenslandmuseumandsciencentre, name='queenslandmuseumandsciencentre'),
    url(r'^museumofbrisbane$', views.museumofbrisbane, name='museumofbrisbane'),

]

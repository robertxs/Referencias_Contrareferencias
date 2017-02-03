from django.conf.urls import url, patterns
from administrador.views import *

urlpatterns = patterns(
    '',
    url(
        r'^$',
        'administrador.views.user_login',
        name='index'
    ),
    url(
        r'^register/$',
        Register.as_view(),
        name='register'
    ),
    url(
        r'^login/$',
        'administrador.views.user_login',
        name='login'
    ),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/'
        },
        name='logout'),
    url(
        r'^success/$',
        Success.as_view(),
        name='success'
    ),
    url(
        r'^home/$',
        Home.as_view(),
        name='home'
    ),
    url(
        r'^inbox/$',
        Inbox.as_view(),
        name='inbox'
    ),
)

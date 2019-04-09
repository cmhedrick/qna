from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.views.generic.base import RedirectView
from django.urls import path
from graphene_django.views import GraphQLView

from qna_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.IndexPageView.as_view()),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
]

if settings.DEBUG:
    urlpatterns + static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]


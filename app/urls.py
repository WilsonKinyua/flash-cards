from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    # api
    url(r'^api/subjects/$', views.SubjectList.as_view()),
    url(r'^api/subjects/(?P<pk>[0-9]+)/$', views.SubjectDetail.as_view()),
    url(r'^api/notes/$', views.NotesList.as_view()),
    url(r'^api/notes/(?P<pk>[0-9]+)/$', views.NotesDetail.as_view()),
    url(r'^api/profiles/$', views.ProfileList.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

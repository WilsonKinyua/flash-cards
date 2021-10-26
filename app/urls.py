from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    # api
    url(r'^api/subjects/$', views.SubjectList.as_view()),
    url(r'^api/notes/$', views.NotesList.as_view()),
    path('add/', views.add, name='add')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

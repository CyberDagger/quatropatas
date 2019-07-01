from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from animais import views as animais_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^animais/', include('animais.urls')),
    url(r'^conta/', include('conta.urls')),
    url(r'^doacao/', include('doacao.urls')),
    url(r'^$', animais_views.index, name='index')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

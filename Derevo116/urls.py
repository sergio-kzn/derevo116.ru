"""Derevo116 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^yandex\W*.html$', TemplateView.as_view(template_name='../yandex_545a557cc12bb32d.html')),
    path('page/', include('SimplePage.urls')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('cart/', include('Cart.urls')),
    # path('accounts/login/', auth_views.LoginView.as_view()),
    path('', include('Index.urls')),
    path('', include('Product.urls')),
]


# https://github.com/summernote/django-summernote
# Когда опция отладки включена ( DEBUG=True), НЕ забудьте добавить шаблоны URL, как показано ниже:
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static('biofa-kazan.ru/media', document_root=settings.BIOFA_MEDIA_ROOT)

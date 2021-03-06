"""CaixaAngola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('NovasOportunidades', views.novasoportunidades, name='NovasOportunidades'),
    path('SubmissionStatus', views.submissionstatus, name='submissionStatus'),
    path('CaixaSocial', views.caixasocial, name='caixaSocial'),
    # authentication
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register'),
    path('indexPMO', views.indexpmo, name='indexPMO'),
    path('indexGestor', views.indexgestor, name='indexGestor'),
    path('notasGestor', views.notasgestor, name='notasGestor'),
    path('sendFiles', views.sendfiles, name='sendFiles'),
    path('notasPMO', views.notaspmo, name='notasPMO'),
    path('caixaSocialPMO', views.caixasocialpmo, name='caixaSocialPMO'),
    path('manual', views.manual, name='manual'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

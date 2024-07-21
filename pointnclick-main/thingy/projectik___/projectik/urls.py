"""projectik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from apps import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.rendermain, name="index"),
    path('catalog/', views.rendercatalog, name="catalog"),
    path('pagefordimension1/', views.renderdimension1, name="dimension1"),
    path('pagefordimension2/', views.renderdimension2, name="dimension2"),
    path('pagefordimension3/', views.renderdimension3, name="dimension3"),
    path('pagefordimension4/', views.renderdimension4, name="dimension4"),
    path('pagefordimension5/', views.renderdimension5, name="dimension5"),
    path('pagefordimension6/', views.renderdimension6, name="dimension6"),
    path('pagefordimension7/', views.renderdimension7, name="dimension7"),
    path('pagefordimension8/', views.renderdimension8, name="dimension8"),
    path('pagefordimension9/', views.renderdimension9, name="dimension9"),
    path('pagefordimension10/', views.renderdimension10, name="dimension10"),
    path('pagefordimension11/', views.renderdimension11, name="dimension11"),
    path('pagefordimension12/', views.renderdimension12, name="dimension12"),
    path('pagefordimension13/', views.renderdimension13, name="dimension13"),
    path('pagefordimension14/', views.renderdimension14, name="dimension14"),
    path('pagefordimension15/', views.renderdimension15, name="dimension15"),
    path('pagefordimension16a/', views.renderdimension16a, name="dimension16a"),
    path('pagefordimension16b/', views.renderdimension16b, name="dimension16b"),
    path('pagefordimension17a/', views.renderdimension17a, name="dimension17a"),
    path('pagefordimension20/', views.renderdimension20, name="dimension20"),
    path('secondcomics1/', views.secondcomics1, name="seccom1"),
    path('secondcomics2/', views.secondcomics2, name="seccom2"),
    path('secondcomics3/', views.secondcomics3, name="seccom3"),
    path('secondcomics4/', views.secondcomics4, name="seccom4"),
    path('secondcomics5/', views.secondcomics5, name="seccom5"),
    path('secondcomics6/', views.secondcomics6, name="seccom6"),
    path('secondcomics7/', views.secondcomics7, name="seccom7"),
    path('secondcomics8/', views.secondcomics8, name="seccom8"),
    path('secondcomics9/', views.secondcomics9, name="seccom9"),
    path('secondcomics10/', views.secondcomics10, name="seccom10"),
    path('secondcomics11/', views.secondcomics11, name="seccom11"),
    path('secondcomics12/', views.secondcomics12, name="seccom12"),
    path('secondcomics13/', views.secondcomics13, name="seccom13"),
    path('secondcomics14/', views.secondcomics14, name="seccom14"),
    path('secondcomics15/', views.secondcomics15, name="seccom15"),
    path('secondcomics16/', views.secondcomics16, name="seccom16"),
    path('secondcomics17/', views.secondcomics17, name="seccom17"),
    path('secondcomics18/', views.secondcomics18, name="seccom18"),
    path('secondcomics19/', views.secondcomics19, name="seccom19"),
    path('secondcomics20/', views.secondcomics20, name="seccom20"),
    path('secondcomicsEnd/', views.secondcomicsEnd, name="seccomEnd"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

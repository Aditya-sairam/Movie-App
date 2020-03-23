"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from ticket_booking import views as ticket_views

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("movie/create",ticket_views.create_view,name="create"),
    path("movie/list",ticket_views.list_view,name="list"),
    path("<str:slug>",ticket_views.detail_view,name="details"),
    path("<str:slug>/booked",ticket_views.detail_book_view,name="book-details")
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


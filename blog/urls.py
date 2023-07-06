"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list_view, name='home'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>',
         views.post_detail_view, name='post_detail'),
    path('<int:id>/share', views.mail_send_view),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]
# urlpatterns = [
# 6) url(r'^admin/', admin.site.urls),
# 7) url(r'^$', views.post_list_view),
# 8) url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-
# \w]+)/$', views.post_detail_view,name='post_detail'),
# 9) ]

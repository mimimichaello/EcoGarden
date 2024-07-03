from django.urls import path, include

from home_page.views import home_page

urlpatterns = [
    path('', home_page, name='home_page'),
    #path('accounts/', include('allauth.urls')),
]

from django.contrib import admin
from django.urls import path, include

from allauth.account.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('home_page.urls')),
]

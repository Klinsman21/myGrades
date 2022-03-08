from django.contrib import admin
from django.urls import path, include
from my_grades import views


urlpatterns = [
    path('home', views.HomePageView.as_view(), name='home'),
    path('', include('my_grades.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
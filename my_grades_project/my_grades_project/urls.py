from django.contrib import admin
from django.urls import path, include
from my_grades import views
from django.contrib.auth.views import LoginView
admin.site.site_header = 'Adiministração do My Grades'

urlpatterns = [
    path('home', LoginView.as_view(), name='home'),
    path('', include('my_grades.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

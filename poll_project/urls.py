
from django.contrib import admin
from django.urls import path, include

from poll import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('signup/', views.signup, name='signup'),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('update/<poll_id>/', views.update, name='update'),
    path('delete/<poll_id>/', views.delete, name='delete'),
    path('vote/<poll_id>/', views.vote, name='vote'),
    path('results/<poll_id>/', views.results, name='results'),
    path('user/', include("user.urls")),
]

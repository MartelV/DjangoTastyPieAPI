from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', api_views.register, name='register'),
    path('delete/<int:note_id>/', api_views.delete_note, name='delete_note'),
    path('', api_views.note_list, name='note_list'),
]

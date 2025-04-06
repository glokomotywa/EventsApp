from django.urls import path
from django.conf.urls import handler404, handler500
from . import views

handler404 = 'base.views.custom_404'
handler500 = 'base.views.custom_500'


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    
    path('', views.home, name="home"),
    path('event/<str:pk>/', views.event, name="event"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('manage-account/', views.manageAccount, name='manage-account'),
    
    path('create-event/', views.createEvent, name="create-event"),
    path('update-event/<str:pk>/', views.updateEvent, name="update-event"),
    path('delete-event/<str:pk>/', views.deleteEvent, name="delete-event"),
    path('delete-comment/<str:pk>/', views.deleteEvent, name="delete-comment"),
    
    path('500-test/', views.trigger_error),
]
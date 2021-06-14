from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('success/', views.success),
    path('daily/', views.daily),
    path('view_officials', views.view_officials),
    path('show_officials/', views.show_officials),
    path('officials/', views.show_officials),
    path('rate_official/<str:name>/<str:elected_office>', views.rate_official),
    path('addRate/<str:name>/<str:elected_office>', views.addRate),
    path('rate/<str:name>/<str:elected_office>', views.rate_official),
    path('logout', views.logout),
    path('users/', views.users),
    path('deleteUser/<int:user_id>', views.deleteUser),
    path('message', views.message, name='message-list'),
    path('comment', views.comment),
    path('deleteMessage/<int:message_id>', views.deleteMessage),
    path('deleteComment/<int:comment_id>', views.deleteComment),
    path('zipcode/', views.zipcode),
    path('editMessage/<int:message_id>', views.editMessage),
    path('updateMessage/<int:message_id>', views.updateMessage),
    path('editComment/<int:comment_id>', views.editComment),
    path('updateComment/<int:comment_id>', views.updateComment),
    path('deleteUser/<int:user_id>', views.deleteUser),
    path('editUser/<int:user_id>', views.editUser),
    path('addMessage/', views.addMessage),
    path('profile/', views.profile)
]
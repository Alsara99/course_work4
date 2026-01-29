from django.urls import path
from .views import *

app_name = "mailing"

urlpatterns = [
    path('', index, name='index'),
    path('recipients/', RecipientListView.as_view(), name='recipient_list'),
    path('recipients/create/', RecipientCreateView.as_view(), name='recipient_create'),
    path('recipients/<int:pk>/update/', RecipientUpdateView.as_view(), name='recipient_update'),
    path('recipients/<int:pk>/delete/', RecipientDeleteView.as_view(), name='recipient_delete'),

    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    path('', index, name='index'),
    path('mailings/', MailingListView.as_view(), name='mailing_list'),
    path('mailings/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailings/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailings/<int:pk>/send/', send_mailing_view, name='send_mailing'),

    path('statistics/', MailingStatisticsView.as_view(), name='mailing_statistics'),
    path('users/<int:user_id>/block/', BlockUserView.as_view(), name='block_user'),
    path('clients/', RecipientListView.as_view(), name='recipient_list'),
    path('clients/create/', RecipientCreateView.as_view(), name='recipient_create'),
]
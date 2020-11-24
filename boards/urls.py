from django.urls import path

from . import views
from . import api 

urlpatterns = [
    path('',views.BoardListView.as_view(),name='home'),
    path('boards/<int:board_id>/',views.board_topics,name='board_topics'),
    path('boards/<int:board_id>/new/',views.new_topic,name='new_topic'),
    path('boards/<int:board_id>/topics/<int:topic_id>/',views.topic_posts,name='topic_posts'),
    path('boards/<int:board_id>/topics/<int:topic_id>/reply/', views.reply_topic, name='reply_topic'),
    path('boards/<int:board_id>/topics/<int:topic_id>/posts/<int:post_id>/edit/',views.PostUpdateViews.as_view(),name= 'edit_post'),
    
    
    path('api/list/',api.board_list_api, name='boardlistapi'),
    path('api/list/<int:id>',api.board_detail_api, name='board_detail_api'),
    path('api/list/v2',api.BoardListApi.as_view(), name='boardlistapi_v2'),
    path('api/list/v2/<int:id>',api.BoardDetail.as_view(), name='board_detail_api_v2'),
]
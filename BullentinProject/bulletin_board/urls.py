from django.urls import path
from . import views  # 현재 위치의 views.py

# MVC의 controller의 mapping 같은 기능

app_name = 'bulletin_board'
urlpatterns = [  # ''와 index 주소 매핑 후 함수 views.index 부르기
    path('', views.index, name='index'),  # 방법 2가지: python 함수, class(재사용성 증가)
    path('create/', views.create_bulletin, name='new_bulletin'),
    path('add/', views.add_bulletin, name='insert_bulletin'),
    path('<int:bulletin_id>/', views.view_bulletin, name='view'),  # 글 번호로 받아서 아이디에 저장하기
    path('update/<int:bulletin_id>/', views.update_bulletin, name='update'),
    path('delete/<int:bulletin_id>/', views.delete_bulletin, name='delete'),
]
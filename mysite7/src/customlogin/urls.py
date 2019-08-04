'''
Created on 2019. 7. 28.

@author: 405-9
'''
#하위 urls.py를 정의 및 해당 어플리케이션의 뷰함수를 등록
#app_name : 별칭 기반으로 url을 찾을 때 사용하는 그룹 이름
#ex) cl그룹명의 signup별칭을 가진 뷰함수를 찾을 경우 url 'cl:signup'
#하위 urls를 만들경우 url 별칭:그룹명 이런식으로 작성해야함
from django.urls.conf import path
from customlogin.views import signup,signin,signout
app_name = 'cl'
#urlpatterns : path 함수로 뷰함수를 등록 및 관리하는 변수
urlpatterns = [
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
    ]


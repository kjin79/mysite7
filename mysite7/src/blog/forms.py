'''
Created on 2019. 8. 3.

@author: 405-9
'''
from django.forms.models import ModelForm
from blog.models import Post
from django.forms.fields import ImageField, FileField
from django.forms.widgets import ClearableFileInput
class PostingForm(ModelForm):
    #사용자가 업로드할 파일/이미지를 입력받는 공간 생성
    #forms.ImageField : 사용자가 이미지를 선택할 수 있는 입력공간
    #required : forms.xxField의 공용 매개변수
    #required : 사용자가 꼭 입력하지 않아도 되는 설정을 하는 매개변수
    #ClearableFileInput : <input type='file'>형태의 입력공간에 파일 관련 추가설정을 할 수 있는 위젯
    #multiple : True -> 하나의 입력공간에 여러개의 파일을 선택할 수 있도록 허용
    images = ImageField(required=False,widget=ClearableFileInput(attrs={'multiple':True}))
    files = FileField(required=False,widget=ClearableFileInput(attrs={'multiple':True}))
    class Meta:
        model = Post
        fields=['category','title','content']
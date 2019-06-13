
from django import forms

from .models import Post

class PostForm(forms.ModelForm): # 장고에게 PostForm이 ModelForm임을 알려준다
	class Meta: 
		model = Post # 폼을 만들기위해 어떤 model이쓰여야하는지 장고에게 알려주는 구문
		fields = ('title', 'text',)
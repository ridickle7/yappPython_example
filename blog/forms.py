from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:     # 이 폼을 만들기 위해 어떤 model이 쓰여야 하는지 장고에 알려줌 (장고에 맞게 변형
        model = Post
        fields = ('title', 'text',)
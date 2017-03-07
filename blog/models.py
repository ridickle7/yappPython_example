from django.db import models
from django.utils import timezone
# 다른 파일에 있는 것을 추가하라는 뜻입니다.
# 다시 말해, 매번 다른 파일에 있는 것을
# 복사&붙여넣기로 해야하는 작업을
# `from이 대신 불러와주는 거죠.

class Post(models.Model): # 모델 정의
    author = models.ForeignKey('auth.User') # 다른 모델에 대한 링크
    title = models.CharField(max_length=200) #글자 수가 제한된 텍스트
    text = models.TextField() # 글자 수에 제한이 없는 긴 텍스트
    created_date = models.DateTimeField(default=timezone.now) # 날짜 & 시간
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):  # 현재 시간으로 바꿔주는
        self.published_date = timezone.now()
        self.save()

    def __str__(self):  # getTitle()
        return self.title
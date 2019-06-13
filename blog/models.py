from django.db import models
from django.utils import timezone




# models은 Post가 장고 모델임을 의미합니다. 
# 이 코드 때문에 장고는 Post가 데이터베이스에 저장되어야 한다고 알게 됩니다.
class Post(models.Model):
	# 다른모델에 대한 링크
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # 글자 수가 제한된 텍스트를 정의할 때 사용
    title = models.CharField(max_length=200)
    # 글자 수에 제한이 없는 긴 텍스트를 위한 속성
    text = models.TextField()
    # 날짜와 시간
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
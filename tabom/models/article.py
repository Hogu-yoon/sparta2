from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    # 수정일자 설정 auto_now
    updated_at = models.DateTimeField(auto_now=True)
    # 생성일자 설정 auto_now_add
    created_at = models.DateTimeField(auto_now_add=True)

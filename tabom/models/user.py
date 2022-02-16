from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    # 수정일자 사용
    updated_at = models.DateTimeField(auto_now=True)
    # 생성일자 사용
    created_at = models.DateTimeField(auto_now_add=True)

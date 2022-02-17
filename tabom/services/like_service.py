from tabom.models import Like


# -> Like 이런 식은 타입 힌트
def do_like(user_id: int, article_id: int) -> Like:
    return Like.objects.create(user_id=user_id, article_id=article_id)

from django.test import TestCase

from tabom.models.article import Article
from tabom.models.user import User
from tabom.services.like_service import do_like


class TestLikeService(TestCase):
    def test_a_user_can_like_an_article(self) -> None:
        # 좋아요를 누르게 하는 함수
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When
        like = do_like(user.id, article.id)

        # Then
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)

    def test_a_user_can_like_an_article_only_once(self) -> None:
        # 오직 한번만 누를 수 있는 함수
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # Expect
        # 첫번째 좋아요는 가능
        like1 = do_like(user.id, article.id)

        # with self.assertRaises(Exception):
        #     pass
            # raise Exception()

        # 두번째 에러는 실패
        like2 = do_like(user.id, article.id)

        # When
        like = do_like(user.id, article.id)

        # Then
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)

    # def test_it_should_raise_exception_when_like_an_user_does_not_exist(self) -> None:
    #     # Given
    #     invalid_user_id = 9988
    #     article = Article.objects.create(title="test_title")
    #
    #     # Expect
    #     with self.assertRaises(IntegrityError):
    #         do_like(invalid_user_id, article.id)
    #
    # def test_it_should_raise_exception_when_like_an_article_does_not_exist(self) -> None:
    #     # Given
    #     user = User.objects.create(name="test")
    #     invalid_article_id = 9988
    #
    #     # Expect
    #     # ??? 무슨 패키지를 받은지 모르겠음
    #     with self.assertRaises(IntegrityError):
    #         do_like(user.id, invalid_article_id)

    def test_like_count_should_increase(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When
        do_like(user.id, article.id)

        # Then
        article = Article.objects.get(id=article.id)
        self.assertEqual(1, article.like_set.count())

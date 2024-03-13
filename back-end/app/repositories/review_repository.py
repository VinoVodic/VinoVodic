from django.contrib.auth.models import User

from app.models import Review


class ReviewRepository:
    def create_review(
        self,
        user: User,
        winery_id: int,
        rating: int,
        comment: str | None = None,
    ) -> None:
        review = Review.objects.create(
            user=user,
            rating=rating,
            comment=comment,
            winery_id=winery_id,
        )
        review.save()

    def get_review_by_id(self, review_id: int) -> Review | None:
        if review := Review.objects.get(pk=review_id):
            return review

    def delete_review(self, review_id: int) -> None:
        review = Review.objects.get(pk=review_id)
        review.delete()

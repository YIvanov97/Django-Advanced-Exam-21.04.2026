from unittest import TestCase
from products.forms import ReviewCreateForm


class TestProductReviewForm(TestCase):
    def test__review_create_form_with_empty_content__is_invalid(self):
        form = ReviewCreateForm(data={
            'content': '',
        })

        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors['content'])
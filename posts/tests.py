from django.test import TestCase
# from django.urls import reverse

from .models import Author, Post


class PostTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(name="David")
        cls.post = Post.objects.create(
            title="The Magic of Harry Potter",
            author=author,
            snippet="There is magic in the air.",
            body="There is magic in the air at Hogwarts.",
        )

    def test_post_listing(self):
        self.assertEqual(f"{self.post.title}", "The Magic of Harry Potter")
        self.assertEqual(f"{self.post.author}", "David")
        self.assertEqual(f"{self.post.snippet}", "There is magic in the air.")
        self.assertEqual(f"{self.post.body}", "There is magic in the air at Hogwarts.")

    def test_post_detail(self):
        self.assertEqual(f"{self.post.title}", "The Magic of Harry Potter")
        self.assertEqual(f"{self.post.author}", "David")
        self.assertEqual(f"{self.post.snippet}", "There is magic in the air.")
        self.assertEqual(f"{self.post.body}", "There is magic in the air at Hogwarts.")

    def test_post_update(self):
        self.assertEqual(f"{self.post.title}", "The Magic of Harry Potter")
        self.assertEqual(f"{self.post.author}", "David")
        self.assertEqual(f"{self.post.snippet}", "There is magic in the air.")
        self.assertEqual(f"{self.post.body}", "There is magic in the air at Hogwarts.")

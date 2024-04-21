from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import index, contact, about


class IndexPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("index")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_page_template(self):
        self.assertTemplateUsed(self.response, "index.html")

    def test_index_page_contains_correct_html(self):
        self.assertContains(self.response, "Django Extensions")

    def test_index_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there, I should not be on this page!")

    def test_index_page_url_resolves_index_view(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, index.__name__)


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.response, "about.html")

    def test_about_page_contains_correct_html(self):
        self.assertContains(self.response, "Coded By:")

    def test_about_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there, I should not be on this page!")

    def test_about_page_url_resolves_index_view(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, about.__name__)


class ContactPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("contact")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_contact_page_template(self):
        self.assertTemplateUsed(self.response, "contact.html")

    def test_contact_page_contains_correct_html(self):
        self.assertContains(self.response, "Contact Us")

    def test_contact_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there, I should not be on this page!")

    def test_contact_page_url_resolves_index_view(self):
        view = resolve("/contact/")
        self.assertEqual(view.func.__name__, contact.__name__)

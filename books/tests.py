from django.test import Client, TestCase


class ListBooksTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list_books_returns_100_books(self):
        response = self.client.get('/list')

        self.assertEqual(response.status_code, 200)
        payload = response.json()

        self.assertEqual(len(payload), 100)
        self.assertEqual(
            set(payload[0].keys()),
            {'title', 'author', 'year', 'pages', 'borrowed'},
        )

    def test_post_is_not_allowed(self):
        response = self.client.post('/list')

        self.assertEqual(response.status_code, 405)

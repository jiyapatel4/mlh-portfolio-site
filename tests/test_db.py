import unittest
from peewee import *

from app import app
from app import TimelinePost

MODELS = [TimelinePost]

# use an in-memory SQLite for tests.
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection...but a good practice all the same.
        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()

    def test_timeline_post(self):
        # Create 2 timeline posts.
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2

        # Get timeline posts and assert that they are correct
    def test_get_time_line_post(self):
        # Create 2 timeline posts.
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')

        # Get timeline posts.
        response = app.test_client().get('/api/timeline_post')
        data = response.get_json()

        # Assert that the response is correct.
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        self.assertIn('timeline_posts', data)
        self.assertIsInstance(data['timeline_posts'], list)
        self.assertEqual(len(data['timeline_posts']), 2)

        posts_data = {post['id']: post for post in data['timeline_posts']}

        # Assert the first post.
        first_post_data = posts_data[first_post.id]
        self.assertIsInstance(first_post_data, dict)
        self.assertEqual(first_post_data['id'], first_post.id)
        self.assertEqual(first_post_data['name'], 'John Doe')
        self.assertEqual(first_post_data['email'], 'john@example.com')
        self.assertEqual(first_post_data['content'], "Hello world, I'm John!")

        # Assert the second post.
        second_post_data = posts_data[second_post.id]
        self.assertIsInstance(second_post_data, dict)
        self.assertEqual(second_post_data['id'], second_post.id)
        self.assertEqual(second_post_data['name'], 'Jane Doe')
        self.assertEqual(second_post_data['email'], 'jane@example.com')
        self.assertEqual(second_post_data['content'], "Hello world, I'm Jane!")
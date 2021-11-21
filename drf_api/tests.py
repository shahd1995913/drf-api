from django.test import TestCase

from django.contrib.auth import get_user_model

from .models import Post

class PostModelTests(TestCase):

    @classmethod

    def setUpTestData(cls):
   
        test_the_user = get_user_model().objects.create_user(username='Admin', password='admin12345')
   
        test_the_user.save()
   
        test_the_post = Post.objects.create(title='Test Post', body='Test Post Body', author=testuser1)
   
        test_the_post.save()
    

    def testing_the_content(self):
   

        post = Post.objects.get(id=1)


        author = f'{post.author}'
   
        title = f'{post.title}'
   
        body = f'{post.body}'
   
        self.assertEqual(author, 'Admin')
   
        self.assertEqual(title, 'Test Post')
   
        self.assertEqual(body, 'Test Post Body')
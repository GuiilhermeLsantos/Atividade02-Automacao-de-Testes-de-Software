import unittest
from unittest.mock import patch
from blog.blog import Blog

class TestBlog(unittest.TestCase):
    
    @patch('blog.requests.get')
    def test_posts(self, mock_get):
        mock_response = [{'userId': 1, 'id': 1, 'title': 'Title 1', 'body': 'Body 1'},
                         {'userId': 2, 'id': 2, 'title': 'Title 2', 'body': 'Body 2'}]
        mock_get.return_value.json.return_value = mock_response
        
        blog = Blog()
        posts = blog.posts()
        
        self.assertEqual(posts, mock_response)
        
    @patch('blog.requests.get')
    def test_post_by_user_id(self, mock_get):
    
        mock_response = {'userId': 1, 'id': 1, 'title': 'Title 1', 'body': 'Body 1'}
        mock_get.return_value.json.return_value = mock_response
        
        blog = Blog()
        post = blog.post_by_user_id('1')
        
        self.assertEqual(post, mock_response)

if _name_ == '_main_':
    unittest.main()
import unittest
from api.utils.size_recommender import size_recommender_top, size_recommender_bottom, size_recommender

class TestSizeRecommender(unittest.TestCase):

    def test_size_recommender_top_female(self):
        self.assertIn('S', size_recommender_top(78, 60, 154, 'F'))
        self.assertIn('M', size_recommender_top(85, 65, 160, 'F'))
        self.assertIn('L', size_recommender_top(90, 72, 160, 'F'))
        self.assertIn('XL', size_recommender_top(95, 80, 165, 'F'))
        self.assertIn('XXL', size_recommender_top(100, 85, 165, 'F'))

    def test_size_recommender_top_male(self):
        self.assertIn('XS', size_recommender_top(82, 70, 160, 'M'))
        self.assertIn('S', size_recommender_top(86, 74, 160, 'M'))
        self.assertIn('M', size_recommender_top(92, 80, 170, 'M'))
        self.assertIn('L', size_recommender_top(100, 90, 180, 'M'))
        self.assertIn('XL', size_recommender_top(108, 100, 180, 'M'))
        
    def test_size_recommender_bottom_female(self):
        self.assertIn('S', size_recommender_bottom(60, 85, 155, 'F'))
        self.assertIn('M', size_recommender_bottom(65, 90, 158, 'F'))
        self.assertIn('L', size_recommender_bottom(70, 95, 162, 'F'))
        self.assertIn('XL', size_recommender_bottom(80, 105, 165, 'F'))
        self.assertIn('XXL', size_recommender_bottom(85, 110, 166, 'F'))

    def test_size_recommender_bottom_male(self):
        self.assertIn('XS', size_recommender_bottom(70, None, 160, 'M'))
        self.assertIn('S', size_recommender_bottom(75, None, 160, 'M'))
        self.assertIn('M', size_recommender_bottom(82, None, 170, 'M'))
        self.assertIn('L', size_recommender_bottom(90, None, 180, 'M'))
        self.assertIn('XL', size_recommender_bottom(98, None, 180, 'M'))
        
    def test_size_recommender_female(self):
        result = size_recommender(78, 60, 85, 154, 'F')
        self.assertIn('S', result['top_size'])
        self.assertIn('S', result['bottom_size'])
        
    def test_size_recommender_male(self):
        result = size_recommender(82, 70, None, 160, 'M')
        self.assertIn('XS', result['top_size'])
        self.assertIn('XS', result['bottom_size'])

if __name__ == '__main__':
    unittest.main()

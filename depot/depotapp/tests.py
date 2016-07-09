#/usr/bin/python
# -*- coding: utf8 -*-
from django.test import TestCase
from forms import ProductForm


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class ProductTest(TestCase):
    def setUp(self):
        self.product = {
            'title':'My Book Title',
            'description':'yyy',
            'image_url':'https://img3.doubanio.com/mpic/s1727290.jpg',
            'price':1
        }

        f = ProductForm(self.product)
        f.save()
        self.product['title'] = 'My Another Book Title'

    def test_attrs_cannot_empty(self):
        '''title，description，price，image_url不能为空
        '''
        f = ProductForm({})
        self.assertFalse(f.is_valid())
        self.assertTrue(f['title'].errors)
        self.assertTrue(f['description'].errors)
        self.assertTrue(f['price'].errors)
        self.assertTrue(f['image_url'].errors)

    def test_price_positive(self):
        '''price必须大于零
        '''
        f = ProductForm(self.product)
        self.assertTrue(f.is_valid())

        self.product['price'] = 0
        f = ProductForm(self.product)
        self.assertFalse(f.is_valid())

        self.product['price'] = -1
        f = ProductForm(self.product)
        self.assertFalse(f.is_valid())

        self.product['price'] = 1

    def test_imgae_url_endwiths(self):
        '''image_url必须以jpg，png，jpg结尾，并且对大小写不敏感
        '''
        url_base = 'http://www.baidu.com/'
        oks = ('fred.gif', 'fred.jpg', 'fred.png', 'FRED.JPG', 'FRED.Jpg')
        bads = ('fred.doc', 'fred.gif/more', 'fred.gif.more')
        for endwith in oks:
            self.product['image_url'] = url_base+endwith
            f = ProductForm(self.product)
            self.assertTrue(f.is_valid(),msg='error when image_url endwith '+endwith)

        for endwith in bads:
            self.product['image_url'] = url_base+endwith
            f = ProductForm(self.product)
            self.assertFalse(f.is_valid(),msg='error when image_url endwith '+endwith)

        self.product['image_url'] = 'https://img3.doubanio.com/mpic/s1727290.jpg'

    def test_title_unique(self):
        '''titile必须唯一
        '''
        self.product['title'] = 'My Book Title'
        f = ProductForm(self.product)
        self.assertFalse(f.is_valid())
        self.product['title'] = 'My Another Book Title'

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from core.models import Post

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(titulo="Post11", texto="Lorem ipsum do Mussum, cassiudis")
        Post.objects.create(titulo="Post22", texto="Lorem ipsum, normal")

    def test_post_have_value_mussum(self):
        post11 = Post.objects.get(titulo="Post11")
        post22 = Post.objects.get(titulo="Post22")
        self.assertEqual(post11.getMussum(), True)
        self.assertEqual(post22.getMussum(), False)

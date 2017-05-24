# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length = 100)
    texto  = models.TextField()

    def __str__(self):
        return self.titulo

    def getMussum(self):
        return self.texto.lower().find('mussum') != -1

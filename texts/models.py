# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.conf import settings

from stemmer.stemmer import stem

class Word(models.Model):
    word = models.CharField(
        max_length=255,
        unique=True
        )


class Text(models.Model):
    body = models.CharField(
        max_length=512,
        )

    @staticmethod
    def insert_text(text):
        new = Text(body=text)
        new.save()
        text = stem(text)
        for w in text.split(' '):
            try:
                word = Word.objects.get(word=w)
                try:
                    match = TextHasWord.objects.get(word=word, text=new)
                    match.frequency = match.frequency + 1
                    match.save()
                except TextHasWord.DoesNotExist:
                    new_match = TextHasWord(text=new, word=word)
                    new_match.save()

            except Word.DoesNotExist:
                new_word = Word(word=w)
                new_word.save()
                new_match = TextHasWord(text=new, word=new_word)
                new_match.save()



class TextHasWord(models.Model):
    text = models.ForeignKey(
        Text,
        related_name='text_in'
        )

    word = models.ForeignKey(
        Word,
        related_name='word_in'
        )

    frequency = models.IntegerField(
        default=1
        )

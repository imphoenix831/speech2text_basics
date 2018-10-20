# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:16:26 2018

@author: Howie
"""

from google.cloud import speech
from docx import Document
import moviepy.editor as mp
import jieba
from wordcloud import WordCloud
import progressbar
import nltk
nltk.download('punkt')
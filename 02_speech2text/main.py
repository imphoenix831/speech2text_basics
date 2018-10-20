#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 00:28:57 2018

@author: slave1
"""

import speech2text
import re
import os

name = 'sent3'
path =os.getcwd().split('02_speech2text')[0] + 'record'
credential ='憑證檔.json' 
bucket = 'speech2textgood'

# split_audio.split_audio(audio =audio, name = name,  split_time = 30)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential

# 傳送到gcp，以方便進行雲端機器學習
file_list = speech2text.save_to_gcp_storage(bucket = bucket, title_pattern = name, wd =path )

# run speech to text
for i in file_list:
    print(i)
    gcs_uri_name ='gs://'+ bucket +'/' + i
    speech2text.speech_to_text(gcs_uri = gcs_uri_name, doc_title = re.sub(r'.wav','',i), timeout = None, sample_rate_hertz = 48000,json_os = credential)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 00:28:57 2018

@author: slave1
"""

import speech2text   
import re
import os


def single_speech(filename,rate_hertz=48000):   
   
    path = os.getcwd().split('02_speech2text')[0] + 'record'   
    
    
    credential ='Speech2text憑證檔.json' 
    bucket = 'speech2text_imphoenix'

    # split_audio.split_audio(audio =audio, name = name,  split_time = 30)
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential

    # 傳送到gcp，以方便進行雲端機器學習
   
    file_list = speech2text.save_to_gcp_storage(bucket = bucket, title_pattern = filename, wd =path )   
    file_list = [i for i in file_list if 'wav' in i]
    
    # run speech to text
    for i in file_list:
        print(i) 
        gcs_uri_name ='gs://'+ bucket +'/' + i
        speech2text.speech_to_text(gcs_uri = gcs_uri_name, doc_title = re.sub(r'.wav','',i), timeout = None, sample_rate_hertz = rate_hertz ,json_os = credential)
        return True
    
    return False
    #------如果遇到無音檔的狀況------------
        #i = '無.wav'
        #file_list = speech2text.save_to_gcp_storage(bucket = bucket, title_pattern = i, wd =path )
        #gcs_uri_name ='gs://'+ bucket +'/' + i
        #speech2text.speech_to_text(gcs_uri = gcs_uri_name, doc_title = re.sub(r'.wav','',i), timeout = None, sample_rate_hertz = rate_hertz ,json_os = credential)
    

def all_speech(rate_hertz=48000):

    #------run 全部的音檔 ------------
    credential ='Speech2text憑證檔.json' 
    bucket = 'speech2text_imphoenix'

    # split_audio.split_audio(audio =audio, name = name,  split_time = 30)
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential
    
    path = os.getcwd().split('02_speech2text')[0] + 'record/'   
    file_list = [i for i in os.listdir(path) if '.wav' in i]

    # run speech to text
    for i in file_list:
        print(i)
        file_list = speech2text.save_to_gcp_storage(bucket = bucket, title_pattern = i, wd =path )
        gcs_uri_name ='gs://'+ bucket +'/' + i
        speech2text.speech_to_text(gcs_uri = gcs_uri_name, doc_title = re.sub(r'.wav','',i), 
                                   timeout = None, sample_rate_hertz = rate_hertz , json_os = credential,
                                   path = path)

    print("巳完成逐字稿")
    return True


#主程式 
    
def menu():
    os.system("cls")
    print("請輸入語音轉文字稿的功能")
    print("=========================")
    print("1:單一檔案" )
    print("2:record 目錄全部檔案")
    print("0:結束")
    print("=========================")
    
    return


menu()
menu = int(input("請輸入你的選擇:"))
    
if menu == 1:
    filename = input("請輸入 1.檔案名 : " ) 
    rate_hertz = int(input("音檔 Hertz: "))
    result = single_speech(filename,rate_hertz)
    
elif menu == 2:    
    rate_hertz = int(input("音檔 Hertz: "))
    result = all_speech(rate_hertz) 

if result:
    print("文字稿巳經完成")
else:
    print("請檢查檔案名稱: {} 是否正確?!".format(filename))    
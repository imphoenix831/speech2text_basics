from pydub import AudioSegment
import datetime
# ref: https://stackoverflow.com/questions/37003862/google-cloud-storage-how-to-upload-a-file-from-python-3
# Imports the Google Cloud client library
from google.cloud import storage
import os


def split_audio(audio = "Acc.wav", name = 'TEST時尚#01_03_',  split_time = 10 ):

    audio = AudioSegment.from_wav(audio )
    a = audio.duration_seconds / split_time
    
    #time_record = []
    for i in range(int(a)+1):
        if i ==0:
            start = i*split_time
            end = (i+1)*split_time
            print(i*split_time, (i+1)*split_time)
        
        else:
            start = i*split_time+1
            end = (i+1)*split_time
            print(i*split_time+1, (i+1)*split_time)
    
        if i==len(range(int(a))):
            start = (i)*split_time +1
            end =  audio.duration_seconds #- ((i+1)*split_time +1)  
            print(start, end )
        
        
        # title of audio file
        start_title = str(datetime.timedelta(seconds=start))
        end_title = str(datetime.timedelta(seconds=end))
        title = name + start_title + '-'+end_title
        
        # transform start and end time
        start = start *1000
        end = end *1000
        
        
        # time_record
        g = audio[start:end]
        
        # save audio
        g.export(title+".wav", format="wav")
        
        
        
def transform_to_mono(title_pattern = 'TEST時尚#01', path ='/home/slave1/git/Google_Speech_AI_tool/record' ):
    original_file = os.getcwd()
    os.chdir(path)
    file_list = os.listdir()     
    file_list = list(filter(lambda x:title_pattern in x, file_list))
    from pydub import AudioSegment
    for i in file_list:
        print('mono transforming', i)
        try:
            sound = AudioSegment.from_wav(i)
            if sound.channels > 1:
                sound = sound.set_channels(1)
                sound.export(i, format="wav")
                print(i, 'tranformed done with mono audio')
            else:
                print(i, 'no need to transform')
        except:
            print('1.檢查一下你的sample rate 是否大於 48000，如果是，請由降轉到 48000\n2.檔案是否為wav檔？ \n以上可由 https://audio.online-convert.com/convert-to-wav 處理')
    os.chdir(original_file)
    print('轉換完成')
    
        
def save_to_gcp_storage(bucket = 'speechfashion', title_pattern = 'TEST時尚#01', path ='/home/slave1/git/Google_Speech_AI_tool/record' ):
    # list out files
    #file_list = path  
    original_file = os.getcwd()
    os.chdir(path)
    file_list = os.listdir()     
    file_list = list(filter(lambda x:title_pattern in x, file_list))
            
    # store init
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket)
    
    # for loop to store
    for i in file_list:
        blob = bucket.blob(i)
        blob.upload_from_filename(i)
    
    os.chdir(original_file)
    
    return file_list



   


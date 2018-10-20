

"""
Created on Tue May 22 17:33:41 2018

Author: Zino and Howard Chung at Taiwan Marketing Research

# 主題：Python 0到1
* 目的：針對AI聽打課程導向的python 0到1學習
"""


'''
# 資料型態與基礎運算
'''

# 變數
anyname
test

# 給予值
anyname = "It's str."
anyname

# 運算
a = 3
b = 2

c = a + b
c
 
c = a - b
c

c = a * b
c

c = a / b
c

c = a ** b 
c

# 常犯錯誤
g = anyname + c # error
g = anyname+str(c)
g

# 題目
'''
1. 請指定test1變數為 1加2乘7
2. 請指定test1變數為 5的3次方
'''
test1  = (1+2)*7 
print(test1)

test2  = 5 **3 
print(test2)


# 變數覆蓋

var = 10
var

var = '被覆蓋掉了'
var


'''
整數
'''
type(1) # 整數
1+2+3



'''
浮點數
'''
type(0.1) # 浮點數
0.1 + 0.248

'''
布林質
'''

# 在語音轉字檔的應用: 選出title_pattern的錄音檔
'''
select_wav = []
for i in file_list:
    if title_pattern in i:
        select_wav.append(i)

'''
type(True) # 布林質
if True:
    print(1)

a = True
a
if a:
    print(1)

'''
字串
'''

# 在語音轉字檔的應用: #輸出不同語音檔案時將會使用到
'''
correctness_summary_df.to_excel(doc_title+'_文章認字信心矩陣.xlsx')
'''
type('1') #字串
aa = 'good'
'1' + '2' + '3'
aa + '2 2222222'



'''
print的變形
'''

# 在語音轉字檔的應用: 將錄音檔的文字print到ipython console，讓開發者可以第一時間看到文字敘述與信心水準
'''
print('Transcript: {}'.format(alternative.transcript))
print('Confidence: {}'.format(alternative.confidence))
'''

a = 'you'
print('I love {} {} {} {}'.format(a, a,a,a))
print('I love' +' '+ a+' '+a+' '+a+' '+a)


'''
list 
'''

# 在語音轉字檔的應用: 使用list儲存秒數
'''

timer_translist =[]
for hah,timer in zip(transcript_list,timerecored):
   timer_translist.append(hah+'  ' +'【'+' to '.join(timer)+'】')

'''

type(['a','1']) # list
vec = ['a', 1, 0.5]
vec[0]
vec[1]


vec = [1,2,3,4,5]
vec
print(vec)


# 計算長度
print(len(vec))

# 常見操作

# 在語音轉字檔的應用: 去除停止字

'''
# 載入stopwords
with open('stopwords.txt', encoding = 'UTF-8') as f:
    stopwords = f.readlines()
stopwords= [w.replace('\n', '') for w in stopwords]
stopwords= [w.replace(' ', '') for w in stopwords]
stopwords.append('\n')
stopwords.append('\n   \n')
stopwords.append('\x0b')

'''
vec.append(7)
vec.append(9)
vec.append(5)
vec.sort()
vec.clear()


# for 迴圈

# 在語音轉字檔的應用: 將翻譯出來的句子一句句取出來
'''
for result in response.results:
    alternative = result.alternatives[0]
    # The first alternative is the most likely one for this portion.
    transcript_list.append(alternative.transcript)
    transcript_confidence.append(alternative.confidence)
'''

for i in vec:
    print(i)



# 迴圈 { }
c = 0
while c <10:
    c = c + 1
    print(c)
    
# 無限迴圈
while True:
    print("yooooooo~~")

# Function- for與list的組合技能

# 在語音轉字檔的應用 - 化多行程式碼為一行，實現近幾一行搞定語音辨識的關鍵:
'''
speech_to_text_in_a_min(doc_title = '範例1', title_pattern='nlpno', 
                            wd ='/home/slave1/git/Speech2Text_workshop/record',
                            json_os = '/home/slave1/git/Speech2Text_workshop/speech2text-3de4444fd46a.json',sample_rate_hertz =  48000)

'''
    
tmp = ''
lists = ['今天','天氣','很好！']
for item in lists:
    tmp = tmp + item
    print(tmp)    

def str_add(lists):
    tmp = ''
    for item in lists:
        tmp = tmp + ' ' + item 
    print(tmp)
        
mystring = ['我','KO','You']        
str1 = str_add(mystring)
    
def str_Mix(lists):
    tmp = ''
    for item in lists:
        tmp = tmp + item
        print(tmp)
    return tmp

str_list = ['今天','天氣','很好！']

g=str_Mix(str_list)
g

str_list = ['我','真的','很喜歡妳！']
g=str_Mix(str_list)
g

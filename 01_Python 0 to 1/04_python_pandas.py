# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 10:18:30 2018

@author: Howie
"""


'''
# Pandas 實戰演練 - 薪資資料整理
![](https://imgur.com/olLGePA.png)

大學畢業後，不知不覺就到某初創電商公司上班，很不巧的老闆只聘請你一個行銷資訊人員，所以就找你來辦公室商討行銷目標。
老闆說：「最近那個什麼大數據很紅阿！公司有2011-2014年的資料，你去搞個什麼東西出來看看！」

資料來源：Kaggle open data - [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries)

'''


'''
## 設定工作目錄(working directory)
進行資料分析前，首先要做的事情便是設定工作目錄
'''
#import os
#os.chdir('您的工作目錄/Python 0 to 1')
#


'''
載入library
'''
import pandas as pd



'''
載入資料集
'''

df = pd.read_csv('Salaries.csv')

'''
查看前五筆資料
'''
df.head()

'''
查看欄位資訊
'''
df.info()

'''
查看所有欄位名稱
'''
df.columns



'''
老闆走過來問：「我們公司基本的平均工資是多少？」
'''

# 在語音轉字檔的應用:平均總體認字信心水準，看整體文章認字信心程度
'''
 document.add_paragraph('機器認字信心水準' + str(round(correctness_summary_df['機器認字信心水準'].mean(),2) ) + '\n\n' + '\n\n'.join(timer_translist) )
'''

df['BasePay'].mean()

'''
跟老闆來個舉一反三
'''
# describe 類似 R.summary
df.describe()['BasePay']


'''
老闆走過來問：「那公司「各工作職銜」基本的平均工資是多少？」
'''

# 在語音轉字檔的應用: 統計詞頻，判斷簡易的字詞重要性
'''
correctness_summary_df = df_count_all.groupby(['文章段句', '機器認字信心水準', 'start', 'end', '改善順序'], as_index=False)['重要性'].mean().round(2)
'''

dept1 = df.groupby(['JobTitle'], as_index=True)['BasePay'].mean()

# as_index = false 是指 欄位名稱, 用原來的 JobTitle
dept = df.groupby(['JobTitle'], as_index=False)['BasePay'].mean()
dept

'''
老闆問：「那公司最高加班費是多少？ 那各工作職銜？ 各地區？」
'''

'''
最高加班費
'''

# 在語音轉字檔的應用: 統計最高詞頻，判斷簡易的字詞重要性

df['OvertimePay'].max()


'''
各工作職銜最高加班費
'''

job_overtime = df.groupby(['JobTitle'], as_index=False)['OvertimePay'].max()
job_overtime

'''
舉一反三：各工作職銜最高加班費的「員工」有哪些？
'''
# 去除 0  job_overtime['OvertimePay']!=0 
idx = job_overtime['OvertimePay']!=0

job_overtime = job_overtime[job_overtime['OvertimePay']!=0]

#把 job_overtime 和原來的 df 做 Merge , 依據 JobTitle, 
# OvertimePay 在 job_overtime, OvertimePay 二個欄位是相同的

overpay_df = pd.merge(job_overtime, df, on=['JobTitle','OvertimePay'])
overpay_df

'''
老闆走過來問：「那公司「加班費」根據職銜，由高至低產出表單給我～」
'''

# 在語音轉字檔的應用: 將機器認字信心水準進行排序，按改善順序排列
'''correctness_summary_df = correctness_summary_df.sort_values(['機器認字信心水準'])'''

job_overtime = df.groupby(['JobTitle'],as_index=False)['OvertimePay'].max()

#因為要把判斷後, 第一個當成我的 第一個建議, 所以要要先 Sort by
job_overtime_descending = job_overtime.sort_values(['OvertimePay'], ascending = False)
job_overtime_descending.head(25)



'''
舉一反三：各工作職銜最高加班費由高至低的「員工」有哪些？
'''
overpay_df = overpay_df.sort_values(['OvertimePay'], ascending = False)


'''
老闆問：「公司職銜有chief的人有哪些？」
'''

'''
* 方法一
使用pandas的時間 - 0.12秒
'''

import time
start_time = time.time()

# 在語音轉字檔的應用: 挑選出詞句中含有的權重特殊字詞，當作字詞重要性的依據
''' 
df_count = correctness_summary_df[correctness_summary_df['文章段句'].str.contains(i['word'])]
'''

tempdf1 = df[df['JobTitle'].str.lower().str.contains('chief')]
elapsed_time = time.time() - start_time
elapsed_time
tempdf1



'''
* 方法二 
老闆問：「公司職銜有chief的人有哪些？」
使用原生python寫法的時間 - 35秒
'''

import progressbar
#temp = pd.DataFrame()
temp = []
for i in progressbar.progressbar(range(0, len(df))):
    df_temp_extract = df.loc[i:i,::]
    
    if 'chief' in df_temp_extract['JobTitle'].values[0].lower():
        temp.append(df_temp_extract.values.tolist()[0])
        #temp  = pd.concat([temp , df_temp_extract])

tempdf2 = pd.DataFrame(temp, columns = df.columns.tolist())
tempdf2

#%%
from cProfile import label
from cgitb import grey
from os import sep
import re
from tokenize import PlainToken
from konlpy.tag import Kkma
import pandas as pd
import csv
import numpy as np
from itertools import chain
import matplotlib.pyplot as plt

kkma = Kkma()

dic = pd.read_csv('C:/Users/JUN/Desktop/FDR/FD.csv', sep=',', encoding = 'cp949' ,header=0)
data = open('C:/Users/JUN/Desktop/FDR/test.csv', 'r', encoding = 'cp949')

morphs =[]
    
for i in data :
    morphs.append(kkma.morphs(i)) #데이터 분할

data_word = list(chain(*morphs)) #분할된 데이터 셋 1차원 배열로 바꿔주기

count = {}

word_result = pd.DataFrame(columns = ['word', 'word_root' , 'polarity' , 'depression' , 'anxiety' , 'loneliness' , 'violence'])  #빈데이터셋 
result =pd.DataFrame(columns = ['depression' , 'anxiety' , 'loneliness' , 'violence']) #빈데이터셋

for i in dic['word']:
    for j in data_word:
        if i == j: #비교
            count[j] = count.get(j,0)+1
            
            data_insert = {'word' : j, 'word_root' : dic.word_root[dic.index[dic['word'] == j][0]], 'polarity' : dic.polarity[dic.index[dic['word'] == j][0]], 'depression': dic.depression[dic.index[dic['word'] == j][0]], 'anxiety': dic.anxiety[dic.index[dic['word'] == j][0]], 'loneliness': dic.loneliness[dic.index[dic['word'] == j][0]], 'violence': dic.violence[dic.index[dic['word'] == j][0]]} #데이터 셋 추가 단계 
            
            word_result = word_result.append(data_insert, ignore_index=True) #추가된 데이테 셋 빈데이터에 넣어주기


insert ={'depression': word_result['depression'].sum(), 'anxiety': word_result['anxiety'].sum(), 'loneliness': word_result['loneliness'].sum(), 'violence': word_result['violence'].sum()} #합계 데이터셋 추가 단계

result = result.append(insert, ignore_index=True) #계산된 데이터셋 넣어주기

print("=============================================")  
print(count)
print(word_result)

plt.style.use("ggplot")
result = result.transpose()
result.columns = ['value']


plt.figure()
plt.bar(result.index,result.value)
plt.title("Result of Emotion Analysis", fontsize = 20)
plt.xlabel("Emotion")
plt.ylabel("Score")
plt.show()

# %%
 
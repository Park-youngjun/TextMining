import pandas as pd
from konlpy.tag import Kkma
import csv
kkma = Kkma()

dic = pd.read_csv('C:/Users/JUN/Desktop/FDR/FD.csv', sep=',', encoding = 'cp949' ,header=0)

root = dic['word']

word_root = []
for i in root:
    word_root.append(kkma.morphs(i))
    
# print(word_root)

word = csv.writer("C:/Users/JUN/Desktop/FDR/file.csv",delimiter = ',')
word.writerow(word_root)
//test1
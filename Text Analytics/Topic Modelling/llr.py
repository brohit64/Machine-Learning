# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 03:05:07 2019

@author: lenovo lappy
"""

import nltk
from collections import Counter
import math
from nltk.tokenize import RegexpTokenizer
import operator


def pre(text1):
 lis1=nltk.word_tokenize(text1)
 lis1=[nltk.stem.PorterStemmer().stem(word.lower()) for word in lis1 if word not in nltk.corpus.stopwords.words("English")]
 text=" ".join(lis1)
 return text

def llr(corpus1,corpus2):
    tokenizer=RegexpTokenizer(r'\w+')
    corp1=Counter(tokenizer.tokenize(corpus1))
	corp2=Counter(tokenizer.tokenize(corpus2))
    sig_terms={}
    for k,v in corp1.items():
     if v>5:
        row1=[v,corp2[k],v+corp2[k]]
        row2=[sum(corp1.values())-v,sum(corp2.values())-corp2[k],sum(corp1.values())-v+sum(corp2.values())-corp2[k]]
        row3=[row1[0]+row2[0],row1[1]+row2[1],row1[2]+row2[2]]
        E=[(row3[0]*row1[2])/row3[2],(row3[1]*row1[2])/row3[2],(row3[0]*row2[2])/row3[2],(row3[1]*row2[2])/row3[2]]
        chi_square=((row1[0]-E[0])*(row1[0]-E[0])/E[0])+((row1[1]-E[1])*(row1[1]-E[1])/E[1])+((row2[0]-E[2])*(row2[0]-E[2])/E[2])+((row2[1]-E[3])*(row2[1]-E[3])/E[3])
        if chi_square>3.84:
         sig_terms[k]=[1,chi_square]
   
    for k,v in corp2.items():
     if v>5:
        row1=[v,corp1[k],v+corp1[k]]
        row2=[sum(corp1.values())-v,sum(corp1.values())-corp1[k],sum(corp1.values())-v+sum(corp1.values())-corp1[k]]
        row3=[row1[0]+row2[0],row1[1]+row2[1],row1[2]+row2[2]]
        E=[(row3[0]*row1[2])/row3[2],(row3[1]*row1[2])/row3[2],(row3[0]*row2[2])/row3[2],(row3[1]*row2[2])/row3[2]]
        chi_square=((row1[0]-E[0])*(row1[0]-E[0])/E[0])+((row1[1]-E[1])*(row1[1]-E[1])/E[1])+((row2[0]-E[2])*(row2[0]-E[2])/E[2])+((row2[1]-E[3])*(row2[1]-E[3])/E[3])
        if chi_square>3.84:
         sig_terms[k]=[2,chi_square]
        
    return sig_terms

#cat=llr(corpus1,corpus2)
#print(sorted(cat.items(), key=operator.itemgetter(1)))


        
        
    


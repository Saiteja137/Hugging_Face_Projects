# -*- coding: utf-8 -*-
"""Text_Generation_Hugging_Face.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QeN4lE4Dt7TOaohHML5CuJjBn9Z-b-iR

#Text Generation Using Hugging Face

Importing Necessary Libraries
"""

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, confusion_matrix, roc_auc_score

from transformers import pipeline

import torch

"""Importing the dataset for Text Generation"""

peoms = pd.read_csv('robert_frost_collection.csv')
peoms.head(5)

content=peoms['Content'].dropna().tolist()

lines = []
for peom in content:
  for line in peom.split('\n'):
    lines.append(line.rstrip())

lines = [line for line in lines if len(line) > 0]
lines[:5]

gen = pipeline('text-generation')

lines[0]

"""Generating the text by using the maxlength upto"""

gen(lines[0],max_length = 20)

"""BY number of texts to generate"""

gen(lines[1],max_length = 20, num_return_sequences = 2)

"""In The output we got 2 text generation with token also"""

import textwrap
def wrap(x):
  return textwrap.fill(x, replace_whitespace=False, fix_sentence_endings=True)

out = gen(lines[0],max_length = 30)
print(wrap(out[0]['generated_text']))

"""Taking my prompt as a input"""

prompt="transformers have a wide variety of applications in nlp"
out=gen(prompt,max_length=50)
print(wrap(out[0]['generated_text']))
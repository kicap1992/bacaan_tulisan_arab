import librosa
import librosa.display as display
import matplotlib.pyplot as plt
import os
# from numpy import array
from datetime import datetime

from numpy.linalg import norm
from dtw import dtw

# import math

import warnings
warnings.filterwarnings("ignore")

def dot(A,B): 
    return (sum(a*b for a,b in zip(A,B)))

def cosine_similarity(a,b):
    return dot(a,b) / ( (dot(a,a) **.5) * (dot(b,b) ** .5) )

def fungsi_librosa(sound_url1,sound_url2):
  
	print(sound_url1)
	print(sound_url2)
  
	y1, sr1 = librosa.load(sound_url1)
	y2, sr2 = librosa.load(sound_url2)
		
	mfcc1 = librosa.feature.mfcc(y1,sr1) 
	mfcc2 = librosa.feature.mfcc(y2,sr2)

	
	path = 'static/created_image/'
	if not os.path.exists(path):
		os.makedirs(path)
  
	today_date = datetime.now().strftime("%Y-%m-%d")
  
  
	path = path + today_date+ '/'
	path_nya = path
 
	if not os.path.exists(path):
		os.makedirs(path)
  
	hour_min_sec = datetime.now().strftime("%H-%M-%S")
  
	plt.figure(figsize=(14, 5))
	display.waveshow(y1, sr=sr1)
	plt.savefig(path+'spec'+hour_min_sec+'.png')

	plt.figure(figsize=(14, 5))
	display.waveshow(y2, sr=sr2)
	plt.savefig(path+'spec1'+hour_min_sec+'.png')
 
	dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
 
	array1 = []
	for nums in mfcc1:
			for val in nums:
					array1.append(val)
        
	array2 = []
	for nums in mfcc2:
			for val in nums:
					array2.append(val)
 
	cosine_similaritynya = cosine_similarity(array1, array2) 
 
	return {'dist': dist, 'cosine_similaritynya': cosine_similaritynya, 'path': path_nya, 'hour_min_sec': hour_min_sec}
    

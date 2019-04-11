# Imports for data-preprocessing
import pandas as pd
import numpy as np
from __future__ import print_function

# Import for spiting the data set
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import StandardScaler

# Imports for classification 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.decomposition import PCA 
from sklearn.pipeline import Pipeline
from sklearn import metrics as mt
import matplotlib.pyplot as plt

# Import for Statistical Comparison 
import math


### Lets do some classification 
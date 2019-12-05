import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb    # Graph




def read_csv(self, file_name):
    input_data = pd.read_csv("abc.csv")
    print(input_data.head())
    
def pearson_correlation_coefficient(self, a, b):
    pearsoncorr = input_data.corr(method='pearson')
    print(pearsoncorr)

def pearsoncorr_graph():
    sb.heatmap(
        pearsoncorr, 
        xticklabels = pearsoncorr.columns,
        yticklabels = pearsoncorr.columns,
        cmap = 'RdBu_r',
        annot = True,
        linewidth = 0.5
    )


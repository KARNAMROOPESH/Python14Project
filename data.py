import pandas as pd
import statistics
import plotly.figure_factory as pf 
import random

dataframe = pd.read_csv('./medium_data.csv')
data = dataframe['id'].tolist()

popmean = statistics.mean(data)
popstdev = statistics.stdev(data)

print(popmean,popstdev)

def ex():
    sample = []

    for i in range(100):
        index = random.randint(0 , len(data)-1)
        value = data[index]
        sample.append(value)
    
    meansample = statistics.mean(sample)
    
    return meansample 

expmean = []

for i in range(1000):
    meansample = ex()
    expmean.append(meansample)
print(meansample)
samplingmean = statistics.mean(expmean)
samplingstan = statistics.stdev(expmean)
print(samplingmean,samplingstan)


fig = pf.create_distplot([expmean], ["Sampling Mean"] , show_hist= False)
fig.show()




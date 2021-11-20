import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random

df=pd.read_csv("data.csv")
data=df["claps"].tolist()
mean=st.mean(data)
stdev=st.stdev(data)
median=st.median(data)
mode=st.mode(data)
print(mean,mode,median,stdev)
def randomSetOfMeans(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex= random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    mean=st.mean(dataSet)
    return mean

meanList=[]
for i in range(0,1000):
    setofMean=randomSetOfMeans(30)
    meanList.append(setofMean)
mean=st.mean(meanList)
stdev=st.stdev(meanList)

sd1start,sd1end=mean-stdev,mean+stdev
sd2start,sd2end=mean-(2*stdev),mean+(2*stdev)
sd3start,sd3end=mean-(3*stdev),mean+(3*stdev)

fig=ff.create_distplot([meanList],["mean"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.1],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[sd1start,sd1start],y=[0,1],mode="lines",name="standard deviation1"))
fig.add_trace(go.Scatter(x=[sd1end,sd1end],y=[0,0.1],mode="lines",name="standard deviation1"))
fig.add_trace(go.Scatter(x=[sd2start,sd2start],y=[0,0.1],mode="lines",name="standard deviation2"))
fig.add_trace(go.Scatter(x=[sd2end,sd2end],y=[0,0.1],mode="lines",name="standard deviation2"))
fig.add_trace(go.Scatter(x=[sd3start,sd3start],y=[0,0.1],mode="lines",name="standard deviation3"))
fig.add_trace(go.Scatter(x=[sd3end,sd3end],y=[0,0.1],mode="lines",name="standard deviation3"))

fig.show()

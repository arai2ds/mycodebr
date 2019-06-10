#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas as pd

def pygraph(booktoread):
    mdf = pd.read_excel(booktoread,sheet_name="Sheet1")
    menMeans = mdf['mins']
    menMeans = tuple(menMeans.values) # this produces a tuple from the mins column

    quaters = mdf['Quarter']
    quaters = tuple(quaters.values) # this produces a tuple from the quarter column


    N = 4
    menMeans = (20, 35, 30, 35)
    menStd = (2, 3, 4, 1)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.30       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, menMeans, width, yerr=menStd) #these are the blue bottom values

    plt.ylabel('outage minutes')
    plt.title('outage minutes per quarter')
    plt.xticks(ind, quaters) # xaxis data
    plt.yticks(np.arange(0,201, 15))
    #plt.yticts(np.arrange(0,max(memMeans) +20,(max(memMeans) +20)/10)
    plt.legend((p1[0],),('minutes',))

    now=datetime.datetime.now()
    filesaved = now.strftime("%Y-%m-%d-outage.png")
    plt.savefig(filesaved)
    return filesaved
    #plt.show()

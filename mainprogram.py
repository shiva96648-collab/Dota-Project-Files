#!/usr/bin/env python
# coding: utf-8

# In[20]:


import json

#gamelog=[]
#with open("C:\\Users\\Shiva Prasad\\output1.txt") as json_data:
    #d = json.load(json_data)
    #print(type(d))
    #print(type(d[0]))
    #print(json.dumps(d[0], indent=2))
    
gamelog = []
log=[]
for line in open("C:\\Users\\Shiva Prasad\\Desktop\\termination project\\output files\\testoutput5.txt", 'r',encoding='utf-8'):
    log.append(json.loads(line))
print(log[0]["time"])


# In[26]:


import matplotlib.pyplot as plt

TeamAplayer1gd=0
TeamAplayer2gd=0
TeamAplayer3gd=0
TeamAplayer4gd=0
TeamAplayer5gd=0
goldTeamA=0
TeamBplayer1gd=0
TeamBplayer2gd=0
TeamBplayer3gd=0
TeamBplayer4gd=0
TeamBplayer5gd=0
goldTeamB=0
TeamAplayer1xp=0
TeamAplayer2xp=0
TeamAplayer3xp=0
TeamAplayer4xp=0
TeamAplayer5xp=0
xpTeamA=0
TeamBplayer1xp=0
TeamBplayer2xp=0
TeamBplayer3xp=0
TeamBplayer4xp=0
TeamBplayer5xp=0
xpTeamB=0
goldTeamAtotal=[]
goldTeamBtotal=[]
timetotal=[]
TeamAx=[]
TeamAy=[]
TeamBx=[]
TeamBy=[]
for i in range(0,len(log)):
    if log[i]["type"]=="interval" and log[i]["time"]>0:
        if log[i]["slot"]==0: 
            TeamAplayer1gd=log[i]["gold"]
            TeamAplayer1xp=log[i]["xp"]
            TeamAx.append(log[i]["x"])
            TeamAy.append(log[i]["y"])
        if log[i]["slot"]==1: 
            TeamAplayer2gd=log[i]["gold"]
            TeamAplayer2xp=log[i]["xp"]
            TeamAx.append(log[i]["x"])
            TeamAy.append(log[i]["y"])
        if log[i]["slot"]==2: 
            TeamAplayer3gd=log[i]["gold"]
            TeamAplayer3xp=log[i]["xp"]
            TeamAx.append(log[i]["x"])
            TeamAy.append(log[i]["y"])
        if log[i]["slot"]==3: 
            TeamAplayer4gd=log[i]["gold"]
            TeamAplayer4xp=log[i]["xp"]
            TeamAx.append(log[i]["x"])
            TeamAy.append(log[i]["y"])
        if log[i]["slot"]==4: 
            TeamAplayer5gd=log[i]["gold"]
            TeamAplayer5xp=log[i]["xp"]
            TeamAx.append(log[i]["x"])
            TeamAy.append(log[i]["y"])
        if log[i]["slot"]==5: 
            TeamBplayer1gd=log[i]["gold"]
            TeamBplayer1xp=log[i]["xp"]
            TeamBx.append(log[i]["x"])
            TeamBy.append(log[i]["y"])
        if log[i]["slot"]==6: 
            TeamBplayer2gd=log[i]["gold"]
            TeamBplayer2xp=log[i]["xp"]
            TeamBx.append(log[i]["x"])
            TeamBy.append(log[i]["y"])
        if log[i]["slot"]==7: 
            TeamBplayer3gd=log[i]["gold"]
            TeamBplayer3xp=log[i]["xp"]
            TeamBx.append(log[i]["x"])
            TeamBy.append(log[i]["y"])
        if log[i]["slot"]==8: 
            TeamBplayer4gd=log[i]["gold"]
            TeamBplayer4xp=log[i]["xp"]
            TeamBx.append(log[i]["x"])
            TeamBy.append(log[i]["y"])
        if log[i]["slot"]==9: 
            TeamBplayer5gd=log[i]["gold"]
            TeamBplayer5xp=log[i]["xp"]
            TeamBx.append(log[i]["x"])
            TeamBy.append(log[i]["y"])
    timetotal.append(log[i]["time"])
    goldTeamA=TeamAplayer1gd+TeamAplayer2gd+TeamAplayer3gd+TeamAplayer4gd+TeamAplayer5gd
    xpTeamA=TeamAplayer1xp+TeamAplayer2xp+TeamAplayer3xp+TeamAplayer4xp+TeamAplayer5xp
    goldTeamB=TeamBplayer1gd+TeamBplayer2gd+TeamBplayer3gd+TeamBplayer4gd+TeamBplayer5gd
    xpTeamB=TeamBplayer1xp+TeamBplayer2xp+TeamBplayer3xp+TeamBplayer4xp+TeamBplayer5xp
    
    goldTeamAtotal.append(goldTeamA)
    goldTeamBtotal.append(goldTeamB)
    #print(goldTeamA,goldTeamB,xpTeamA,xpTeamB)
    
timetotal=timetotal[:len(timetotal)-2]
goldTeamAtotal=goldTeamAtotal[:len(goldTeamAtotal)-2]
goldTeamBtotal=goldTeamBtotal[:len(goldTeamBtotal)-2]

plt.plot(timetotal,goldTeamAtotal)
plt.plot(timetotal,goldTeamBtotal)
plt.legend(['Radiant', 'Dire'], loc='upper right')
plt.savefig('C:\\Users\\Shiva Prasad\\Desktop\\termination project\\graphs\\testgraph5.svg')
plt.show()

plt.scatter(TeamAx,TeamAy)
plt.xlabel('Radiantx')
plt.ylabel('Radianty')
plt.show()

plt.scatter(TeamBx,TeamBy)
plt.xlabel('Direx')
plt.ylabel('Direy')
plt.show()


#print(goldTeamA,goldTeamB,xpTeamA,xpTeamB)


# In[63]:


import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.hist2d(TeamAx, TeamAy, bins=15, cmap='YlOrRd')
cb = plt.colorbar()
cb.set_label('Number of entries')

# Add title and labels to plot.
plt.title('Heatmap of Team A')
plt.xlabel('x axis')
plt.ylabel('y axis')

# Show the plot.
plt.show()

plt.hist2d(TeamBx, TeamBy, bins=15, cmap='YlOrRd')
cb = plt.colorbar()
cb.set_label('Number of entries')

# Add title and labels to plot.
plt.title('Heatmap of Team B')
plt.xlabel('x axis')
plt.ylabel('y axis')

# Show the plot.
plt.show()


# In[ ]:





# In[ ]:





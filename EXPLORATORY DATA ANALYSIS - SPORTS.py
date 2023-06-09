#!/usr/bin/env python
# coding: utf-8

# GRIP @ The Sparks Foundation - Data Science and Business Analytics

# ## TASK 1: EXPLORATORY DATA ANALYSIS - SPORTS

# Author : ADITYA RAJ

# Objective : To perform "Exploratory Data Analysis" on the dataset 'Indian Premier League'

# ## IMPORTING THE REQUIRED LIBRARIES

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ## LOADING AND READING DATASET

# In[2]:


matches_df = pd.read_csv("matches.csv")
matches_df.head(10)


# ## FEATURE EXPLORATION

# In[14]:


matches_df.shape


# In[15]:


matches_df.info()


# In[16]:


matches_df.describe()


# In[17]:


matches_df.columns


# In[19]:


matches_df.nunique()


# In[20]:


# checking for null values
matches_df.isnull().sum()


# In[21]:


#droping the umpire column to get the rid of null values
matches_df = matches_df.drop(['umpire3'],axis=1)


# In[22]:


len(matches_df['season'].unique())


# In[23]:


pd.concat([matches_df['team1'],matches_df['team2']]).unique()


# ## DATA VISUALIZATION

# TEAMS THAT WON THE MATCH

# In[27]:


plt.figure(figsize=(10,5))
sns.countplot(x = 'winner',data = matches_df)
plt.title('winning Teams')
plt.xticks(rotation = 90);


# wins by Run

# In[28]:


win_max = matches_df.groupby(['winner'],as_index=False)['win_by_runs'].max()
plt.subplots(figsize=(10,5))
plt.xticks(rotation=90)
sns.barplot(win_max['winner'],win_max['win_by_runs'])


# MAN OF THE MATCH WINNERS

# In[30]:


matches_df['player_of_match'].value_counts()[0:5]


# In[32]:


plt.figure(figsize=(10,5))
sns.barplot(x=matches_df.player_of_match.value_counts()[:10].index,y=matches_df.player_of_match.value_counts()[:10])
plt.title('Man of the match winners')
plt.xlabel('player')
plt.ylabel('Match')
plt.xticks(rotation=90)


# NUMBER OF MATCHES PER SEASON

# In[35]:


plt.subplots(figsize=(10,5))
sns.countplot(x=matches_df['season'].sort_values())
plt.title('Number of matches in each Season',fontsize=20)
plt.show()


# TOSS WINNERS

# In[36]:


plt.figure(figsize=(10,5))
plt.bar(list(matches_df['toss_winner'].value_counts().keys()),list(matches_df['toss_winner'].value_counts()))
plt.xticks(rotation=90)
plt.show()


# COMPARISION ON TOSS DECISIONS

# In[37]:


plt.figure(figsize=(15,5))
sns.countplot(matches_df['season'].sort_values(),hue=matches_df['toss_decision'])
plt.title("Decision to field or bat across seasons")
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()


# In[ ]:





# WINNING OF A TEAM AFTER BATTING ON THE FIRST AND SECOND POSITIONS 

# In[38]:


batting_first = matches_df[matches_df['win_by_runs']!=0]
plt.figure(figsize=(10,10))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[41]:


plt.subplots(figsize=(15,5))
sns.countplot(x ='venue',data = matches_df,order = matches_df['venue'].value_counts().index)
plt.title('Match Venues')
plt.xlabel('stadium')
plt.ylabel('Matches')
plt.xticks(rotation = 90)


# LOADING READING AND ANALYSING THE DELIVERIES DATASET

# In[42]:


deliveries_df = pd.read_csv('deliveries.csv')
deliveries_df


# In[43]:


deliveries_df.shape


# In[44]:


deliveries_df.info()


# In[45]:


deliveries_df.describe()


# In[46]:


#Total matches where super over wasand wasn't played
deliveries_df['is_super_over'].value_counts()


# In[47]:


#Total runs given by extra
sum(deliveries_df['extra_runs'])


# In[48]:


#Total runs given by no balls
sum(deliveries_df['noball_runs'])


# In[49]:


#Total runs given on penality
sum(deliveries_df['penalty_runs'])


# In[50]:


#Total soft-dismissal of players over the years
sum(deliveries_df['player_dismissed'].value_counts())


# KINDS OF DISMISSAL

# In[52]:


sns.countplot(x=deliveries_df['dismissal_kind'],data=deliveries_df)
plt.xticks(rotation = 90)


# # CONCLUSION 

# 1)Total number of matches played was 636
# 
# 2)Total seassons played was 12
# 
# 3)Winning Teams
a)Mumbai Indians : first position
b)Rising Pune Supergiants : last position    
# 4)Win by Runs
a)Mumbai Indians : first position
b)Rising PuneSupergiants: last position
# 5)Man of the match
a)CH Gayle : first position
b)VH kohli : last position     
# 6)Highest number of matches per season was on 2013

# 7)Mumbai Indians were the toss winners.

# 8)The only year with same toss for fielding and bating was on 2012

# 9)Winning of the team after batting on the firstand second position were.
a) win by runs : Mumbai Indians
b) win by wickets : Kolkata Knight Riders    
# 10)M chinnaswamy Stadium is the most popular match venue.

# In[ ]:


THANKYOU!!


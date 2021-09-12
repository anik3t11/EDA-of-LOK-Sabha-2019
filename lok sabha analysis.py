#!/usr/bin/env python
# coding: utf-8

# # LOK SABHA
# 
# ![](https://i2.wp.com/opportunitycell.com/wp-content/uploads/2021/06/lok-sabha-india-2-638.jpg?fit=638%2C479&ssl=1)
# 
#    #### General elections were held in India in seven phases from 11 April to 19 May 2019 to elect the members of the 17th Lok Sabha. Votes were counted and the result declared on 23 May. Around 912 million people were eligible to vote, and voter turnout was over 67 percent – the highest ever, as well as the highest ever participation by women voters.
# #### All 543 elected MPs are elected from single-member constituencies using first-past-the-post voting. The President of India appoints an additional two members from the Anglo-Indian community if he believes that community is under-represented.
# #### Eligible voters must be Indian citizens, 18 or older than 18, an ordinary resident of the polling area of the constituency and registered to vote (name included in the electoral rolls), possess a valid voter identification card issued by the Election Commission of India or an equivalent. Some people convicted of electoral or other offences are barred from voting.
# #### The elections are held on schedule and as per the Constitution of India that mandates parliamentary elections once every five years.
# #### In this analysis report we will analyze the LOK SABHA 2019 result. I have downloaded the election data set from kaggle with over 2,264 no. of rows and 19 column consisting of different parameter.
#     
#     

# In[2]:


import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# Imported Different moeules that will help us in analysis

# In[3]:


sns.set_style('whitegrid')
matplotlib.rcParams['font.size'] =14
matplotlib.rcParams['figure.figsize'] = (9,5)
matplotlib.rcParams['figure.facecolor'] = '#ffffff'


# Set parameters for visualization to get the output in desire shape

# In[4]:


elec_df = pd.read_csv('LS_2.0.csv')
elec_df


# Imported CSV file that we are going to analyze

# In[5]:


elec_df.shape


# fom this we get to k/w the size of table i.e. it contain 2263rows and 19 columns.

# In[6]:


elec_df.info()


# In[7]:


elec_df.NAME.value_counts().drop('NOTA').head(10)


# In[8]:


elec_winner =  elec_df[elec_df.WINNER >0]
elec_winner


# Extracted winner from the csv file who won the election

# In[9]:


elec_loss = elec_df[elec_df.WINNER<1]
elec_loss


# Contestant who faced defeat in the election

# ## Tabluating table for parties contesting the election  
# ### and
# ## Winning The Election

# In[10]:


#tabluating the winning party 
win_party =elec_winner.PARTY.value_counts()
win_party

Parties won election on different seats.
# In[11]:


win_last= win_party[6:]
win_last


# In[12]:


win_5 = win_party.head(5)
win_5['other']=win_last.sum()
win_5


# top 5 parties won the election

# In[13]:


final_list =win_5.copy()
final_list


# In[14]:


total_party = elec_df.PARTY.value_counts()
total_last = total_party[6:]
total_5 = total_party.head(5)
total_5['others'] = total_last.sum()
total_5

Parties contested the election
# # Tabluating the contestant and winner based on Gender ratio!!
# 
# Contested the election and winners based on the ration 

# In[15]:


gender_df=elec_df.GENDER.value_counts()
gender_df


# In[16]:


gender_winner=elec_winner.GENDER.value_counts()
gender_winner


# In[17]:


plt.figure(figsize=(12,6))
plt.title('WINNER GENDER RATIO')
plt.pie(gender_winner,labels=gender_winner.index,autopct='%1.1f%%',startangle =180);
plt.figure(figsize=(12,6))
plt.title('Gender percentage who contest the Election')
plt.pie(gender_df,labels=gender_df.index,autopct='%1.1f%%',startangle =180);


# ## Tabualation based on Category
# 
# Contested the election based on their gender

# In[18]:


category_df=elec_df.CATEGORY.value_counts()
category_df


# In[19]:


category_winner=elec_winner.CATEGORY.value_counts()
category_winner


# In[20]:


plt.figure(figsize=(12,6))
plt.title('Category percentage contest the Election')
plt.pie(category_df,labels=category_df.index,autopct='%1.1f%%',startangle =180);

plt.figure(figsize=(12,6))
plt.title('Category percentage WON the Election')
plt.pie(category_winner,labels=category_winner.index,autopct='%1.1f%%',startangle =180);


# # Tabulation of contestant got Max. and Min. Votes  
# 
# Contested the elction andd got maximum and minimum votes

# In[21]:


#Contestant winning with maximum margin
margin_df = elec_winner[['NAME','PARTY','CONSTITUENCY','STATE','TOTAL\nVOTES']]
margin_df['Win By'] = round(elec_winner['TOTAL\nVOTES']*100/elec_winner['TOTAL ELECTORS'])
margin_df = margin_df.sort_values(by='Win By',ascending = False).head(10)

margin_df


# In[22]:


#Contestant winning with maximum margin
lessmargin_df = elec_winner[['NAME','PARTY','CONSTITUENCY','STATE','TOTAL\nVOTES']]
lessmargin_df['Win By'] = round(elec_winner['TOTAL\nVOTES']*100/elec_winner['TOTAL ELECTORS'])
lessmargin_df = lessmargin_df.sort_values(by='Win By',ascending = True).head(10)

lessmargin_df


# In[23]:


#Contestant got least% votes all over india
least_df = elec_df[['NAME','PARTY','CONSTITUENCY','STATE','TOTAL\nVOTES']]
least_df['Win By'] = (elec_df['TOTAL\nVOTES']*100/elec_df['TOTAL ELECTORS'])
least_df = least_df.sort_values(by='Win By',ascending = True).head(10)

least_df


# In[24]:


x = least_df['NAME']
y = least_df['Win By']
plt.figure(figsize=(12,6))
plt.scatter(x,y,color='r')
plt.plot(x,y,color='g')
plt.xticks(rotation =60)
plt.title('Got Least Vote',color='r')
plt.xlabel('NAME OF POLITICIAN',color='r')
plt.ylabel('% of vote from Constituency',color='r');


# In[25]:


x = margin_df['NAME']
y = margin_df['Win By']
plt.figure(figsize=(12,6))
plt.scatter(x,y,color='r')
plt.plot(x,y,color='g')
plt.xticks(rotation =60)
plt.title('WIN BY MOST MARGIN',color='r')
plt.xlabel('NAME OF POLITICIAN',color='r')
plt.ylabel('% of vote from Constituency',color='r');


# # Tabulation of contestant with maximum number of Criminal Case
# 
# Contestant having most number of criminal charges on them.

# In[26]:


#Contestant with maximum number of criminal case
crime_df = elec_df[['PARTY','NAME','CONSTITUENCY','STATE','CRIMINAL\nCASES']].dropna()
crime_df= crime_df.replace('Not Available',0)
crime_df['CRIMINAL\nCASES']=crime_df['CRIMINAL\nCASES'].apply(pd.to_numeric)
crime_df = crime_df.sort_values(by='CRIMINAL\nCASES',ascending=False).head(10) 
crime_df


# In[27]:


#present LS member with most no. of crime cases
crime_win = elec_winner[['PARTY','NAME','CONSTITUENCY','STATE','CRIMINAL\nCASES']].dropna()
crime_win= crime_win.replace('Not Available',0)
crime_win['CRIMINAL\nCASES']=crime_win['CRIMINAL\nCASES'].apply(pd.to_numeric)
crime_win = crime_win.sort_values(by='CRIMINAL\nCASES',ascending=False).head(10) 
crime_win


# In[28]:


crime_df.info()


# In[29]:


plt.figure(figsize=(12,6))
plt.xticks(rotation=90)
plt.title('No. of Criminal Cases')
plt.xlabel('Name of Contestant')
plt.ylabel('No. of Cases')
plt.plot(crime_df['NAME'],crime_df['CRIMINAL\nCASES'])
plt.scatter(crime_df['NAME'],crime_df['CRIMINAL\nCASES'],c='r');


# # Table of Most aged person contested the election
# 
# Contestant with maximum age
# 

# In[30]:


age_df = elec_df[['PARTY','NAME','CONSTITUENCY','STATE','AGE']].dropna().sort_values(by='AGE',ascending = False).head(5)
age_df


# In[31]:


win_age = elec_winner[['PARTY','NAME','CONSTITUENCY','STATE','AGE']].dropna().sort_values(by='AGE',ascending = False).head(5)
win_age


# In[32]:


x= age_df['NAME']
y= age_df['AGE']
plt.figure(figsize=(12,6))
plt.xticks(rotation=60)
plt.title('OLDEST CONTESTANT TO RUN THE ELECTION')
plt.scatter(x,y)
plt.plot(x,y);


# # Cities which pools maximum no. of votes
# 
# Cities which pools maximum number of voters

# In[33]:


most_elector= elec_df[['STATE','CONSTITUENCY','TOTAL ELECTORS']].sort_values(by='TOTAL ELECTORS',ascending = False).drop_duplicates().head(10)
most_elector


# In[34]:


x= most_elector['CONSTITUENCY']
y= most_elector['TOTAL ELECTORS']
plt.figure(figsize=(12,6))
plt.xticks(rotation=60)
plt.title('CITIES WITH HIGHEST ELECTORS')
plt.scatter(x,y)
plt.plot(x,y);


# # Contestant Education 
# 
# Eduction of candidates

# In[35]:


edu_df=elec_df.EDUCATION.value_counts().head(10)
edu_df


# In[36]:


plt.figure(figsize=(12,6))
plt.xticks(rotation=60)
plt.title('EDUCATION OF CONTESTANT')
count =0
number= pd.DataFrame(edu_df)
number['num'] = edu_df
for i in number['num']:
    plt.text(count-0.1,i+1,str(i),c='black')
    count+=1
sns.barplot(edu_df.index,edu_df);


# In[37]:


ru_df =elec_df[['NAME','PARTY','STATE','CONSTITUENCY','ASSETS','LIABILITIES',]].dropna()

ru_df


# In[38]:


rich_df=ru_df.sort_values(by='ASSETS',ascending=False)
rich_df


# # Questions

# ### 1) Parties contested the election and Total no. of seats of parties in Lok Sabha?

# In[39]:


#table of party contested
total_5


# In[40]:


#table of party won
final_list


# In[41]:


#PIE-CHART OF PARTIES CONTESTED....
plt.figure(figsize=(12,6))
plt.title('Parties Contested the Elections ')
plt.pie(total_5,labels=total_5.index,autopct='%1.1f%%',startangle =180);

#PIE -CHART OF PARTIES WON....
plt.figure(figsize=(12,6))
plt.title('Parties Won the Elections')
plt.pie(final_list,labels=final_list.index,autopct='%1.1f%%',startangle =180);


# Observation from Graph 1
# 
# We can clearly see that BJP is the aprty which contested at maximum seats with over 19.4% of total seats and INC with second highest number i.e. 19.1% not a major difference 3 rd hihest party is IND which contested at 11.3% of total seats 

# Observation from Graph 2
# 
# We can clearly see that BJP coming as a majority party which won at 57.6% of total seats in Loksabha . While INC comimg at second with 10% of total sets followed by DMk at 4.4% of total seats.

# #### Q Gender of ratio contested the election and how many of them won? 

# In[42]:


gender_df=elec_df.GENDER.value_counts()
gender_df


# In[43]:


gender_winner=elec_winner.GENDER.value_counts()
gender_winner


# In[44]:


#Ratio of contestant ine election
plt.figure(figsize=(12,6))
plt.title('Gender percentage who contest the Election')
plt.pie(gender_df,labels=gender_df.index,autopct='%1.1f%%',startangle =180);
#ratio of the won
plt.figure(figsize=(12,6))
plt.title('WINNER GENDER RATIO')
plt.pie(gender_winner,labels=gender_winner.index,autopct='%1.1f%%',startangle =180);


# Graph 1
# There are 87.2% of total male and 12.8% of female candidate contesting the elections.
# 
# Graph 2
# We can observe the percentage of women leader increase to the percentage of contested the election i.e there are 14.1% of total women leader in LS and 85.9% of male candidates wich decreased from 87% of candidate contested the elections

# ### Q. Visualize the graph on contestant category and winners category?

# In[45]:


#Based on category contesting the elction
plt.figure(figsize=(12,6))
plt.title('Category percentage contest the Election')
plt.pie(category_df,labels=category_df.index,autopct='%1.1f%%',startangle =180);

#Based on category won
plt.figure(figsize=(12,6))
plt.title('Category percentage WON the Election')
plt.pie(category_winner,labels=category_winner.index,autopct='%1.1f%%',startangle =180);


# Visualized the graph based on category of the contestant  category 

# ###  Q Contestant won by maximum Margin?

# In[46]:


margin_df


# We have extracted top 10 contestant that won with maximum margin. 

# In[47]:


x = margin_df['NAME']
y = margin_df['Win By']
plt.figure(figsize=(12,6))
plt.scatter(x,y,color='r')
plt.plot(x,y,color='g')
plt.xticks(rotation =60)
plt.title('WIN BY MOST MARGIN',color='r')
plt.xlabel('NAME OF POLITICIAN',color='r')
plt.ylabel('% of vote from Constituency',color='r');


# We  can see from graph rahul gandhi from INC won with maximum margin i.e. 52% which is maximum by any other contestant
# then there was tie b/w 3 contestant which won it with equal margin i.e. is 51%

# ### Q Contestant got least Votes? 

# In[48]:


least_df


# In[49]:


x = least_df['NAME']
y = least_df['Win By']
plt.figure(figsize=(12,6))
plt.scatter(x,y,color='r')
plt.plot(x,y,color='g')
plt.xticks(rotation =60)
plt.title('Got Least Vote',color='r')
plt.xlabel('NAME OF POLITICIAN',color='r')
plt.ylabel('% of vote from Constituency',color='r');


# contestant who secured least votes in LS election there are contest with less then 0.1% of total votes with least vote of Gh. Mohd Wani from J&K gained only 0.097% of total voting

# ### Q. Contestant with maximum number of criminal case?
# ### Q. LS member with most number of criminal case?

# In[50]:


crime_df


# In[51]:


plt.figure(figsize=(12,6))
plt.xticks(rotation=90)
plt.title('No. of Criminal Cases')
plt.xlabel('Name of Contestant')
plt.ylabel('No. of Cases')
plt.plot(crime_df['NAME'],crime_df['CRIMINAL\nCASES'])
plt.scatter(crime_df['NAME'],crime_df['CRIMINAL\nCASES'],c='r');


# There are contestat in the election with near 240 criminal cases on them K. sunderan who has about 240 criminal cases on him.
# while prakash babu who is last in top 10 criminal contestant has about 22 Criminal cases on him.

# In[52]:


crime_win


# In[53]:


plt.figure(figsize=(12,6))
plt.xticks(rotation=90)
plt.title('No. of Criminal Cases')
plt.xlabel('Name of Contestant')
plt.ylabel('No. of Cases')
plt.plot(crime_win['NAME'],crime_win['CRIMINAL\nCASES'])
plt.scatter(crime_win['NAME'],crime_win['CRIMINAL\nCASES'],c='r');


# Adv. Dean kuriakose top the list of most number of criminal cases as lok sabha member he won the seat from IDDUKI,Kerala with 204 criminal cases.
# While subrat pathak is at least with about 11  cases and a member of lok sabha

# ### Q. Oldest contestant to contest 
# ### Q. Oldest person to won?

# In[54]:


age_df


# In[55]:


x= age_df['NAME']
y= age_df['AGE']
plt.figure(figsize=(12,6))
plt.xticks(rotation=60)
plt.title('OLDEST CONTESTANT TO RUN THE ELECTION')
plt.scatter(x,y)
plt.plot(x,y);


# In[56]:


win_age


# In[57]:


x= win_age['NAME']
y= win_age['AGE']
plt.figure(figsize=(12,6))
plt.xticks(rotation=60)
plt.title('OLDEST CONTESTANT TO won THE ELECTION')
plt.scatter(x,y)
plt.plot(x,y);


# This graph comprise of oldest member of lok sabha dr. sabha bariq from up with age of 86 is oldest member of loksabha

# ### Q City wich pools maximum no. of Votes?

# In[58]:


most_elector


# In[59]:


x= most_elector['CONSTITUENCY']
y= most_elector['TOTAL ELECTORS']
plt.figure(figsize=(12,6))
plt.xticks(rotation=60)
plt.title('CITIES WITH HIGHEST ELECTORS')
plt.scatter(x,y)
plt.plot(x,y);


# As India is democratic country and it is imporatnt to vote to choose the correct representive so malkajgiri from telangana has maximum election pool in LS election

# ### Q No. of contestant with different Educations level?

# In[60]:


edu_df


# In[61]:


plt.figure(figsize=(12,6))
plt.xticks(rotation=60)
plt.title('EDUCATION OF CONTESTANT')
count =0
number= pd.DataFrame(edu_df)
number['num'] = edu_df
for i in number['num']:
    plt.text(count-0.1,i+1,str(i),c='black')
    count+=1
sns.barplot(edu_df.index,edu_df);


# As education is important things that play a amjor ole in a person act and behaviour so we extracted information based on thier education level so we can see that there are 502 candidates who are post graduate in their respective fiELD and there are only 28 who has only studied till 5 class. 

# # By Aniket Vyas 

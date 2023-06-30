#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data= { 'Name':['Jani','Prachi','Anjli','Aman','Rupesh','Raj','Yogita'],
      'Age': [18,22,18,20,21,27,19],
      'Gender': ['F', 'F', 'F', 'M', 'M','M', 'F'],
      'Marks':[80, 'NaN', 'NaN', 65, 'NaN', 80, 70]}

df = pd.DataFrame(data)
df


# In[2]:


c = avg =0
for ele in df['Marks']:
    if str(ele).isnumeric():
        c += 1
        avg += ele
avg /=c

df = df.replace(to_replace="NaN",
                value=avg)
df


# In[3]:


df['Gender'] = df['Gender'].map({'M': 0,
                        'F': 1, }).astype(float)
   
df


# In[4]:


df = df[df['Marks'] >= 60].copy()
df


# In[5]:


import pandas as pd

details = pd.DataFrame({
'ID': [1001, 1002, 1003, 1004, 1005, 1006,
1007, 1008, 1009, 1100],
'NAME': ['Pradeep', 'Pankaj', 'Hitesh',
'Pooja', 'Rahul', 'Nikita',
'Shubham', 'Mohit', 'Deepak', "Ravi"],
'BRANCH': ['MCA', 'MCA', 'MCA', 'MCA', 'MCA',
'MCA', 'MCA', 'CSE', 'CSE', 'CSE']})

print(details)


# In[6]:


import pandas as pd

fees_status = pd.DataFrame(
{'ID': [1001, 1002, 1103, 1004, 1005,
1006, 1007, 1008, 1009, 1100],
'PENDING': ['500', '300', 'NIL',
'9000', '15000', '5000',
'450', 'NIL', '550', '650']})

print(fees_status)


# In[7]:


import pandas as pd

details = pd.DataFrame({
'ID': [1001, 1002, 1003, 1004, 1005, 1006,
1007, 1008, 1009, 1100],
'NAME': ['Pradeep', 'Pankaj', 'Hitesh',
'Pooja', 'Rahul', 'Nikita',
'Shubham', 'Mohit', 'Deepak', "Ravi"],
'BRANCH': ['MCA', 'MCA', 'MCA', 'MCA', 'MCA',
'MCA', 'MCA', 'CSE', 'CSE', 'CSE']})

fees_status = pd.DataFrame(
{'ID': [1001, 1002, 1103, 1004, 1005,
1006, 1007, 1008, 1009, 1100],
'PENDING': ['500', '300', 'NIL',
'9000', '15000', '5000',
'450', 'NIL', '550', '650']})

print(pd.merge(details, fees_status, on='ID'))


# In[8]:


import pandas as pd

car_selling_data = {'Brand': ['Tata', 'BMW', 'Tata',
                            'BMW', 'Tata', 'BMW',
                            'Tata', 'Toyota', 'Ford',
                            'Ford', 'Tata', 'Ford'],
                    'Year': [2010, 2011, 2009, 2014,
                            2012, 2009, 2015, 2014,
                            2009, 2021, 2010, 2021],
                    'Sold': [5, 10, 11, 4, 7, 9,
                            9, 8, 7, 1, 3, 11]}

df = pd.DataFrame(car_selling_data)

print(df)


# In[9]:


import pandas as pd

car_selling_data = {'Brand': ['Tata', 'BMW', 'Tata',
                            'BMW', 'Tata', 'BMW',
                            'Tata', 'Toyota', 'Ford',
                            'Ford', 'Tata', 'Ford'],
                    'Year': [2010, 2011, 2009, 2014,
                            2012, 2009, 2015, 2014,
                            2009, 2021, 2010, 2021],
                    'Sold': [5, 10, 11, 4, 7, 9,
                            9, 8, 7, 1, 3, 11]}

df = pd.DataFrame(car_selling_data)

grouped = df.groupby('Year')
print(grouped.get_group(2009))


# In[10]:


import pandas as pd

student_data = {'Name': ['Sonam', 'Priti', 'Jaggu',
                        'Rohan', 'Vikash', 'Surjan',
                        'Shubam', 'Prakash', 'Anil',
                        'Khemeen', 'Pinky', 'Ayush'],

                'Roll_no': [11, 23, 10, 49, 50, 55,
                            12, 33, 44, 21, 51, 20],

                'Email': ['xxxx@gmail.com', 'xxxxxx@gmail.com',
                        'xxxxxx@gmail.com', 'xx@gmail.com',
                        'xxxx@gmail.com', 'xxxxx@gmail.com',
                        'xxxxx@gmail.com', 'xxxxx@gmail.com',
                        'xxxxx@gmail.com', 'xxxxxx@gmail.com',
                        'xxxxxxxxxx@gmail.com', 'xxxxxxxxxx@gmail.com']}

df = pd.DataFrame(student_data)

print(df)


# In[11]:


import pandas as pd

student_data = {'Name': ['Sonam', 'Priti', 'Jaggu',
                        'Rohan', 'Vikash', 'Surjan',
                        'Shubam', 'Prakash', 'Anil',
                        'Khemeen', 'Pinky', 'Ayush'],

                'Roll_no': [11, 23, 10, 49, 50, 55,
                            12, 33, 44, 21, 51, 20],

                'Email': ['xxxx@gmail.com', 'xxxxxx@gmail.com',
                        'xxxxxx@gmail.com', 'xx@gmail.com',
                        'xxxx@gmail.com', 'xxxxx@gmail.com',
                        'xxxxx@gmail.com', 'xxxxx@gmail.com',
                        'xxxxx@gmail.com', 'xxxxxx@gmail.com',
                        'xxxxxxxxxx@gmail.com', 'xxxxxxxxxx@gmail.com']}

df = pd.DataFrame(student_data)

non_duplicate = df[~df.duplicated('Roll_no')]

print(non_duplicate)


# In[12]:


import pandas as pd
   
data1 = {'Name':['keshri', 'Ruchi', 'Mahir', 'Manju'],
        'Age':[22, 21, 20, 31],
        'Address':['Knake', 'Goa', 'Jharkhand', 'Panjab'],
        'Qualification':['M.Tech', 'MCA', 'MBA', 'B.Tech'],
        'Mobile No': [91, 71, 60, 70]}
     
data2 = {'Name':['Umesh', 'Raj', 'Raju', 'Homend'],
        'Age':[18, 20, 32, 45],
        'Address':['Chhattishgar', 'Raipur', 'MadhyPradesh', 'Bhopal'],
        'Qualification':['Mcom', 'MBA', 'BCA', 'B.A'],
        'Salary':[9000, 10000, 5500, 44000]}
   
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
   
df1 = pd.DataFrame(data2, index=[2, 3, 6, 7])


# In[13]:


res = pd.concat([df, df1])


# In[ ]:





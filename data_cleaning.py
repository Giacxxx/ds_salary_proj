#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 10:08:00 2020

@author: gm
"""


import pandas as pd

df = pd.read_csv('/Users/gm/Documents/ds_salary_proj/glassdoor_jobs.csv')

#1 remove -1
#2 salary parsing
#3 company name text only
#4 state field
#5 age of company
#6 parsing of job description

#append to df a column for per hour salary and one column for'employer provided'
df["Hourly"]= df["Salary Estimate"].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df["Employer_Provided"]= df["Salary Estimate"].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

#1 remove -1
df=df[df['Salary Estimate']!='-1']

#2 salary parsing

#remove text 'Glassdoor estimate' from Salary Estimate
salary =df['Salary Estimate'].apply(lambda x: x.split( '(' )[0])

#remove the Ks and dollar signs from salary df
minus_kd= salary.apply(lambda x : x.replace("K"," ").replace("$"," "))


#remove Per Hour and Employer Provided Salary items from minus_kd
min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

#create minimum salary column in df by splitting the two values of min_hr + make it an integer
df['min_salary']= min_hr.apply(lambda x: int(x.split('-')[0]))
df['min_salary'].dtype

#create max salary column in df by splitting the two values of min_hr + make it an integer
df['max_salary']= min_hr.apply(lambda x: int(x.split('-')[1]))
df['max_salary'].dtype

#create average salary column in df
df['avg_salary']= (df.min_salary + df.max_salary)/2


#3 company name text only
# remove last 3 characters from Company Name

df['company_txt']=df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3], axis=1)

#4 state field - what state is the company in? creates columns job_state

df['job_state']=df['Location'].apply(lambda x: x.split(',')[1])
df['job_state'].value_counts()

#See if job position is at the headquarter

df['same_state']=df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)

#5 age of company: subtract year founded from current year

df['age']=df.Founded.apply(lambda x: x if x<1 else 2020-x)

#6 parsing of job description: python, r studio, spark, aws, excel

df['python_yn']=df['Job Description'].apply(lambda x: 1 if 'python'in x.lower() else 0)
df['R_yn']=df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio'in x.lower() else 0)
df['R_yn'].value_counts()
df['spark']=df['Job Description'].apply(lambda x: 1 if 'spark'in x.lower() else 0)
df['aws']=df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['excel']=df['Job Description'].apply(lambda x: 1 if 'excel'in x.lower() else 0)

df.excel.value_counts()





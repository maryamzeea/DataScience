import pandas as pd
import numpy as np

df = pd.read_csv("Salaries.csv",low_memory=False)
df.to_csv("Sal.csv")
print(df.head())
df['BasePay'] = pd.to_numeric(df['BasePay'], errors='coerce')
df['OvertimePay'] = pd.to_numeric(df['OvertimePay'], errors='coerce')
print(f"Average of BasePay: {round(df['BasePay'].mean(),2)}")
print(f'highest amount of OvertimePay: {round(df['OvertimePay'].max(),2)}')
job_title = df.loc[df['EmployeeName']=='JOSEPH DRISCOLL','JobTitle']
print(f'Job Title of Joseph Driscoll:{job_title}')
make = df.loc[df['EmployeeName']=='JOSEPH DRISCOLL','TotalPayBenefits']
print(f'Make of Joseph Driscoll:{make}')
highestPaidPerson = df[df['TotalPay']==df['TotalPay'].max()]
print(f'Highest paid person: {highestPaidPerson}')
lowestPaidPerson = df[df['TotalPay']==df['TotalPay'].min()]
print(f'Lowest paid person: {lowestPaidPerson}')
peryearPay = df.groupby('Year')['BasePay'].mean()
print(f'Peryear pay: {peryearPay}')
print(f'unique job titles: {df['JobTitle'].nunique()}')
print(f'unique job titles: {df['JobTitle'].value_counts().head()}')

# def Have_Chief(CHIEF):
#     if CHIEF not in df['JobTitle']:
#         return False
#     else:
#         return True
print(f'Chief: {df['JobTitle'].str.contains('CHIEF').sum()}')
    

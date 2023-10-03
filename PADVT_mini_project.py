""" 
For the given dataset on bank, perform the following task based on the preliminary analysis of a positive response (term deposit) to direct calls 
from a bank. In essence, the task is a matter of bank scoring, i.e according to the characteristics of a client (potential client), their behaviour
is predicted(loan default,a wish to make a deposit, etc).
For the given dataset, make a visual analysis in order to plan marketing benking campaigns more effectively and also give answers to set of questions
that may be relevant when analyzing banking data:
1. What is the share of slients attracted in our source data?
2. What are the mean values of numerical features among the attracted clients?
3. What is the average call duration for the attracted clients?
4. what is the average age among the attracted and unmarried clients?
5. What is the average age and call duration for different types of client employment?

"""
# Importing necessasary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the data
df=pd.read_csv("bank-additional-full.csv",sep=";")

#Searching for null values
print(df.isnull().sum())


#Droping the rows which has nnull values
print(df.dropna(how='any',inplace=True))


#Duplicate values in the dataset
print(f"There are {df.duplicated().sum()} duplicates")


# Droping the duplicate values
df=df.drop_duplicates()

# Dataframe containing only attracted clients
attracted_clients=df[df['attracted']=='yes']



# 1.Share of clients attracted in our source data.
no_of_attracted_clients=len(attracted_clients)
total_clients=len(df)
attracted_clients_share=no_of_attracted_clients/total_clients
print(f"Share of attracted clients are {attracted_clients_share:.2%}")

# Visualization of the solution
categories_1=["Attracted clients","Other clients"]
values_1=[attracted_clients_share,1-attracted_clients_share]
plt.figure(figsize=(5,5))
plt.pie(values_1,labels=categories_1,autopct='%1.1f%%')
plt.title("Distribution of clients")
plt.show()




# 2.Mean values of numerical features among attracted clients.
numerical_columns=attracted_clients.select_dtypes(include=[np.number])
numerical_feature_mean=numerical_columns.mean()
print(f"Mean values of numerical features among the attracted clients is:")
print(numerical_feature_mean)

# Visualization of the solution
plt.figure(figsize=(5,5))
numerical_feature_mean.plot(kind='bar',color='blue')
plt.title("Mean of all numerical features")
plt.xlabel("Numerical features")
plt.ylabel("Mean value")
plt.tight_layout()
plt.show()




# 3.Average call duration for the attracted clients.
average_call_duration=attracted_clients['duration'].mean()
print(f"Average call duration of attracted clients is {average_call_duration:.2f} seconds")




# 4.Average age among the attracted and unmarried clients.
unmarried_attracted=attracted_clients[attracted_clients['marital']=='single']
married_attracted=attracted_clients[attracted_clients['marital']=='married']
average_age_unmarried=unmarried_attracted['age'].mean()
average_age_married=married_attracted['age'].mean()

# Visualization of the solution
plt.figure(figsize=(8,5))
plt.bar(['Married attraced clients','Unmarried attracted clients'],[average_age_married,average_age_unmarried],color=['red','yellow'])
plt.xlabel('Attracted clients')
plt.ylabel('Average Age')
plt.title("Average age among the attracted and unmarried clients")
plt.tight_layout()
plt.show()
print(f"Average age among the attracted and unmarried clients is {average_age_unmarried:.2f}")
print(f"Average age among the attracted and married clients is {average_age_married:.2f}")




# 5.What is the average age and call duration for different types of client employment?
average_age_and_call_duration_by_job=attracted_clients.groupby('job')[['age','duration']].mean()
print(f"Average age and call duration by job:{average_age_and_call_duration_by_job}")

# Visualization of the solution
average_age_and_call_duration_by_job.plot(kind='bar',figsize=(8,5))
plt.xlabel('jobs')
plt.ylabel('Mean')
plt.title("Average age and call duration by job")
plt.tight_layout()
plt.show()
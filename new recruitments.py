import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("recruitment_data.csv")

companies = df['Company']
recruits = df['Recruits']

plt.figure()
plt.bar(companies, recruits)
plt.xlabel("Company")
plt.ylabel("Number of Recruitments")
plt.title("New Recruitments by Company")
plt.xticks(rotation=45)
plt.show()

plt.figure()
plt.pie(recruits, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

plt.figure()
colors = ['gold','lightcoral','lightskyblue','lightgreen','violet','orange','cyan','pink']
explode = [0.1 if c in ['IBM','Amdocs'] else 0 for c in companies]
plt.pie(recruits, labels=companies, autopct='%1.1f%%', colors=colors, explode=explode, shadow=True)
plt.title("Customized Pie Chart")
plt.show()

plt.figure()
plt.pie(recruits, labels=companies, autopct='%1.1f%%')
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()

ibm_amdocs = df[df['Company'].isin(['IBM','Amdocs'])]

plt.figure()
plt.bar(ibm_amdocs['Company'], ibm_amdocs['Recruits'], color=['blue','green'])
plt.xlabel("Company")
plt.ylabel("Number of Recruitments")
plt.title("IBM vs Amdocs Recruitment Comparison")
plt.show()
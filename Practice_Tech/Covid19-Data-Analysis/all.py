import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

print('Modules are imported.')

corona_dataset_csv = pd.read_csv('Dataset/covid19_Confirmed_dataset.csv')
corona_dataset_csv.head(10)
corona_dataset_csv.shape
corona_dataset_csv.drop(['Lat','Long'],axis=1,inplace=True)
corona_dataset_csv.head(10)

corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()

corona_dataset_aggregated.head(10)

corona_dataset_aggregated.shape

corona_dataset_aggregated.loc['China'].plot()
corona_dataset_aggregated.loc['Italy'].plot()
corona_dataset_aggregated.loc['Spain'].plot()
plt.legend()


corona_dataset_aggregated.loc['China'].plot()


corona_dataset_aggregated.loc['China'].diff().plot()

corona_dataset_aggregated.loc['China'].diff().max()
corona_dataset_aggregated.loc['Italy'].diff().max()

corona_dataset_aggregated.loc['Italy'].diff().max()

countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for country in countries :
    max_infection_rates.append(corona_dataset_aggregated.loc[country].diff().max())
corona_dataset_aggregated['max infection rate'] = max_infection_rates

corona_dataset_aggregated.head()


corona_data = pd.DataFrame(corona_dataset_aggregated['max infection rate'])

corona_data.head()

world_happiness_report = pd.read_csv("Dataset/worldwide_happiness_report.csv")
world_happiness_report.head()
world_happiness_report.shape

columns_to_dropped = ['Overall rank','Score','Generosity','Perceptions of corruption']
world_happiness_report.drop(columns_to_dropped,axis=1 , inplace=True)

world_happiness_report.head()

world_happiness_report.set_index(['Country or region'],inplace=True)
world_happiness_report.head()
corona_data.head()

world_happiness_report.head()

data = world_happiness_report.join(corona_data).copy()
data.head()
data.corr()
data.head()

x = data['GDP per capita']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))

sns.regplot(x,np.log(y))

x = data['Social support']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))

sns.regplot(x,np.log(y))

x = data['Healthy life expectancy']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))

sns.regplot(x,np.log(y))
x = data['Freedom to make life choices']
y = data['max infection rate']
sns.scatterplot(x,np.log(y))

sns.regplot(x,np.log(y))


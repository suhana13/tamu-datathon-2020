import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import rand_num
from rand_num import user
# %matplotlib inline

"""This is a revised version of the Team building notebook that I created previously, using dictionaries integrated with list index values."""

data_original = pd.read_csv('https://drive.google.com/uc?id=1mPK8_AasPMdqy3D9D0kxjjKcIXmhhcQo')
data = data_original
del data['userid']
del data['school'] 
del data['other_school']
del data['majors']
del data['minors']
data["age_bin"].replace({'(15, 18]': 0, '(18, 20]': 1, '(20, 22]': 2, '(22, 25]': 3, '(25, 30]': 4, '(30, 50]': 5}, inplace=True)
data["classification"].replace({'O':0, 'Fr': 1, 'So': 2, 'Jr': 3, 'Sr': 4, 'Ma': 5, 'PhD': 6, }, inplace=True)
data["first_generation"].replace({False:0, True:1}, inplace=True)
data["num_hackathons_attended"].replace({'0':0, '1-3':1, '4-7':2, '10+':3, '8-10':4}, inplace=True)
data_2 = data
del data_2['technology_experience']
del data_2['workshop_suggestions']
del data_2['relavent_industries']

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_features = scaler.fit_transform(data_2)

kmeans = KMeans(init="random", n_clusters=50, n_init=10, max_iter=300, random_state=42)
kmeans.fit(scaled_features)
k = kmeans.labels_[:1250]
df_1 = pd.DataFrame(k)
df_1.columns = ['Cluster']
df_2 = pd.concat([data, df_1], axis=1)
df_2
df_2['index'] = df_2.index
df_2
cluster_num = df_2['Cluster'].values[user]
cluster_num
data_original = pd.read_csv('https://drive.google.com/uc?id=1mPK8_AasPMdqy3D9D0kxjjKcIXmhhcQo')
df_final = pd.concat([df_1, data_original], axis=1)
df_final
build_result = df_final.loc[df_final['Cluster'] == cluster_num]
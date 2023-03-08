import pandas as pd
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from scipy.stats import spearmanr
import numpy as np
import os

# Settings
alpha = 0.1
gamma = 0.1
kernel = 'laplacian' # kernel function
test_size = 0.2  # fraction held-out for testing
seed = 42  # random seed
fingerprint_path = '../../data/features/ofm_fingerprints.csv' # path to fingerprints (length N)
y_path = os.path.join('../../data','qmof.csv') # path to band gap data (length N)

#---------------------------------------
# Read in data
df_features = pd.read_csv(fingerprint_path, index_col=0)
df_BG = pd.read_csv(y_path, index_col="qmof_id")['outputs.pbe.bandgap']
df = pd.concat([df_features, df_BG], axis=1, sort=True)
df = df.dropna()
refcodes = df.index

# Stratification
THRESHOLD = #fillme (get the 0.75 quantile of band gap value)
stratification = #fillme (Hint: [1 if value > THRESHOLD else 0 for value in df[label]])

# Make a training and testing set
train_set, test_set = train_test_split(
	df, test_size=test_size, shuffle=True, stratify=stratification, random_state=seed)
X_train = train_set.loc[:, (df.columns != 'outputs.pbe.bandgap')]
X_test = test_set.loc[:, (df.columns != 'outputs.pbe.bandgap')]

refcodes_train = X_train.index
refcodes_test = X_test.index

scaler = MinMaxScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

y_train = train_set.loc[:, df.columns == 'outputs.pbe.bandgap'].to_numpy()
y_test = test_set.loc[:, df.columns == 'outputs.pbe.bandgap'].to_numpy()

# Train and evaluate KRR model
krr = KernelRidge(alpha=alpha, gamma=gamma, kernel=kernel)
krr.fit(#fillme) (train the model)
y_train_pred = #fillme (used the trained model to predict band gaps)
y_test_pred = #fillme (used the trained model to predict band gaps)

# Save results
df_train = pd.DataFrame(np.concatenate((y_train, y_train_pred), axis=1), 
                        columns=['DFT', 'ML'], index=refcodes_train)
df_train.to_csv('../../results/ofm/train_results.csv', header=True, index=True)

df_test = pd.DataFrame(np.concatenate((y_test, y_test_pred), axis=1), 
                       columns=['DFT', 'ML'], index=refcodes_test)
df_test.to_csv('../../results/ofm/test_results.csv', header=True, index=True)

print('Train size: ', len(y_train))
print('Test size: ', len(y_test))
print('Train/test MAE: ', mean_absolute_error(#fillme),
	  mean_absolute_error(#fillme))
print('Train/test MSE: ', mean_squared_error(#fillme),
	  mean_squared_error(#fillme))
print('Train/test r2: ', r2_score(#fillme),
	  r2_score(#fillme))

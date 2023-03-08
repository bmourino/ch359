import pandas as pd
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, r2_score
from scipy.stats import spearmanr
import numpy as np
import os

# Settings
alpha = 0.1 (fill the best value you found)
gamma = 0.1 (fill the best value you found)
kernel = 'laplacian'  # kernel function
test_size = 0.2  # fraction held-out for testing
seeds = [42, 125, 267, 541, 582]  # random seeds
train_sizes = [2**7, 2**8, 2**9, 2**10, 2**11, 2**12, 2**13, -1]  # train sizes
fingerprint_path = '../../data/features/ofm_fingerprints.csv' # path to fingerprints (length N)
y_path = os.path.join('..../data','qmof-bandgaps.csv') # path to band gap data (length N)

#---------------------------------------
#Read in data
df_features = pd.read_csv(fingerprint_path, index_col=0)
df_BG = pd.read_csv(y_path, index_col="qmof_id")['outputs.pbe.bandgap']
df = pd.concat([df_features, df_BG], axis=1, sort=True)
df = df.dropna()
refcodes = df.index

# Stratification
THRESHOLD = 2.887478
stratification = [1 if value > THRESHOLD else 0 for value in df["outputs.pbe.bandgap"]]

mae = []
mse = []
r2 = []
mae_std = []
mse_std = []
r2_std = []

for train_size in train_sizes:
	mae_test_seeds = []
	mse_test_seeds = []
	r2_test_seeds = []
	for seed in seeds:
		# Make a training and testing set
		train_set, test_set = train_test_split(
			df, test_size=test_size, shuffle=True, random_state=seed)
		if train_size != -1:
			train_set = train_set[0:train_size]
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
		krr.fit(X_train, y_train)
		y_train_pred = krr.predict(X_train)
		y_test_pred = krr.predict(X_test)

		mae_test_seeds.append(mean_absolute_error(y_test, y_test_pred))
		mse_test_seeds.append(mean_squared_error(y_test, y_test_pred))
		r2_test_seeds.append(r2_score(y_test, y_test_pred))

	mae.append(np.average(mae_test_seeds)) # append the average of MAE to list
	mse.append(np.average(mse_test_seeds))
	r2.append(np.average(r2_test_seeds))

	mae_std.append(np.std(mae_test_seeds))
	mse_std.append(np.std(mse_test_seeds))
	r2_std.append(np.std(r2_test_seeds))

	print('Training size: ', train_size)
	print('Avg. testing MAE: ', np.round(np.average(mae_test_seeds), 3))
	print('Avg. testing MSE: ', np.round(np.average(mse_test_seeds), 3))
	print('Avg. testing r2: ', np.round(np.average(r2_test_seeds), 3))

df_evaluation = pd.DataFrame(
	np.array([train_sizes, mae, mse, r2, mae_std, mse_std, r2_std]).T, 
	columns=["Training size", "MAE", "MSE", "R2", "MAE_std", "MSE_std", "R2_std"])
df_evaluation.to_csv('../../results/stoich120/learning_curve.csv', index=False)
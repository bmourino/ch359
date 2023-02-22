import pandas as pd
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, r2_score
from scipy.stats import spearmanr
import numpy as np
import os

# Settings
alpha = #fillme (fill the best value you found)
gamma = #fillme (fill the best value you found)
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
THRESHOLD = #fillme
stratification = #fillme

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
			train_set = #fillme (select the subset of train_set with $train_size data points)
		X_train = train_set.loc[:, (df.columns != 'outputs.pbe.bandgap')]
		X_test = test_set.loc[:, (df.columns != 'outputs.pbe.bandgap')]
		refcodes_train = X_train.index
		refcodes_test = X_test.index

		scaler = MinMaxScaler()
		scaler.fit(X_train)
		X_train = scaler.transform(#fillme)
		X_test = scaler.transform(#fillme)

		y_train = train_set.loc[:, df.columns == 'outputs.pbe.bandgap'].to_numpy()
		y_test = test_set.loc[:, df.columns == 'outputs.pbe.bandgap'].to_numpy()

		# Train and evaluate KRR model
		krr = KernelRidge(alpha=alpha, gamma=gamma, kernel=kernel)
		krr.fit(#fillme)
		y_train_pred = #fillme
		y_test_pred = #fillme

		mae_test_seeds.append(mean_absolute_error(#fillme))
		mse_test_seeds.append(mean_squared_error(#fillme))
		r2_test_seeds.append(r2_score(#fillme))

	mae.append(#fillme) # append the average of MAE to list
	mse.append(#fillme)
	r2.append(#fillme)

	mae_std.append(np.std(mae_test_seeds))
	mse_std.append(np.std(mse_test_seeds))
	r2_std.append(np.std(r2_test_seeds))

	print('Training size: ', train_size)
	print('Avg. testing MAE: ', np.round(np.average(mae_test_seeds), 3))
	print('Avg. testing MSE: ', np.round(np.average(mse_test_seeds), 3))
	print('Avg. testing r2: ', np.round(np.average(r2_test_seeds), 3))

np.savetxt('../../results/ofm/learning_curve_avg.csv',np.vstack([mae,mse,r2]),delimiter=',')
np.savetxt('../../results/ofm/learning_curve_std.csv',np.vstack([mae_std,mse_std,r2_std]),delimiter=',')

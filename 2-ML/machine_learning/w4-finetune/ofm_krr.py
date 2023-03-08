import pandas as pd
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import os
import joblib
import json

# Define evaluation function
def get_regression_metrics(y_true, y_pred, prefix=""): 
	"""
    Get a dicionary with regression metrics:
    
    y_true: ground truth labels 
	y_pred: model predicted labels
	prefix: specify "train" or "test" dataset
	"""
	metrics = {}
	metrics[f"{prefix}_mse"] = #fillme
	metrics[f"{prefix}_mae"] = #fillme
	metrics[f"{prefix}_r2"] = #fillme
    
	return metrics

# Settings
param_grid = {
                'alpha': #fillme,
                '#fillme': #fillme
            }
			# Hint: You can use the np.logspace function to generate a grid for values that you want to vary on a logarithmic scale
			# There are two hyperparameters for KRR: the regularization strength alpha and the Gaussian width gamma
			# For the regularization strength, values between 1 and 1e-3 can be reasonable. For gamma you can use the median heuristic, gamma = 1 / median, or values between 1e-3 and 1e3
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
stratification =  #fillme (Hint: [1 if value > THRESHOLD else 0 for value in df[label]])

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
krr = KernelRidge(kernel=kernel)
random_krr = RandomizedSearchCV(
	#your estimator, param_distributions=param_grid, n_iter=#number of evaluations,
	#cv=#number of folds, verbose=2, n_jobs=2
)
random_krr.fit(#fillme)
model = random_krr.best_estimator_
y_train_pred = #fillme (used the trained model to predict band gaps)
y_test_pred = #fillme (used the trained model to predict band gaps)

train_loss = get_regression_metrics(#fillme, #fillme, "train")
test_loss = get_regression_metrics(#fillme, #fillme, "test")

# Save results
joblib.dump(model, "../../results/ofm/best_model.pkl")
df_train = pd.DataFrame(np.concatenate((y_train, y_train_pred), axis=1), 
			columns=['DFT', 'ML'], index=refcodes_train)
df_train.to_csv('../../results/ofm/train_results.csv', header=True, index=True)

df_test = pd.DataFrame(np.concatenate((y_test, y_test_pred), axis=1), 
		       columns=['DFT', 'ML'], index=refcodes_test)
df_test.to_csv('../../results/ofm/test_results.csv', header=True, index=True)

print('Train size: ', len(y_train))
print('Test size: ', len(y_test))
print('Best hyperparameters: ', random_krr.best_params_)
print('Train loss: ', train_loss)
print('Test loss: ', test_loss)

# Save evaluation matrix
loss = train_loss
loss.update(test_loss)

loss_obj = json.dumps(loss, indent=4)
with open('../../results/ofm/loss.json', 'w') as file:
	file.write(loss_obj)

pd.DataFrame(random_krr.cv_results_).to_csv('../../results/ofm/cv_results.csv')
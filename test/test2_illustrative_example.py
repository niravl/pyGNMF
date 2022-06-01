import numpy as np

## Generating the dataset
num_rows, num_cols, num_fact = 20, 6, 3
G_true = np.random.rand(num_rows, num_fact)
F_true = np.random.rand(num_fact, num_cols)
X_true = G_true@F_true

## Generating Covaraince
a = np.random.randn(num_rows*num_cols, num_rows*num_cols)
covariance = 1e-4*(a.T@a)
cov_inv = np.linalg.inv(covariance)

error_vector = np.random.multivariate_normal(np.zeros(num_rows*num_cols), covariance)

X_error = X_true + error_vector.reshape(num_rows, num_cols)

from scipy import io
io.savemat("IllustrativeExample.mat", {
    "G_true":G_true,
    "F_true":F_true,
    "X_true":X_true,
    "X_error":X_error,
    "covariance":covariance,
})
## Using pyGNMF
from pyGNMF import gnmf_projected_gradient as gproj
from pyGNMF import gnmf_multiplicative_update as gmult
from scipy import io
data = io.loadmat("IllustrativeExample.mat")

X_error = data['X_error']
covariance = data['covariance']
num_fact = 3

GMat, FMat, OFunc = gproj.running_method(
    X_matrix = X_error,
    covariance = covariance,
    G_init = 'random',
    F_init = 'random',
    option='row_stacked',
    num_fact=4,
    num_init=10,
    alpha_init_G=1e-5,
    alpha_init_F=1e-5,
    max_iter=500000,
    tolerance=1e-16,
    conv_typ='relative',
    conv_num=3,
)





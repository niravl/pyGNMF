# pyGNMF
 Python Library for Generalised Non-Negative Matrix Factorisiation (GNMF)

This Python library implements GNMF method introduced in article titled "Generalised Non-Negative Matrix Factorisation for Air Pollution Source Apportionment" published in the Science of Total Environment Journal.

Please refer to the article in SoftwareX for more details. 

## Some Features
Uses NumPy (or CuPy, if the package is installed) to factorise a matrix $X_{n\times m}$ into $G_{n\times p}$ and $F_{p\times m}$. Depending on the choice of the Covariance matrix, the GNMF will result in one of the following methods,

### Covariance Matrix
The covariance matrix ($\Sigma$) should be of size $nm\times nm$ which captures element-wise covariance information. Depending on the type of covariance, GNMF method can act as different methods in the literature,
1. **Covariance Matrix as Identity**: In this case, GNMF method with multiplicative update is same as Lee and Seung's NMF method with multiplicative update. Projected gradient updates can also be used.
2. **Covariance Matrix is Diagonal Matrix**: In this case, GNMF method with multiplicative update is same as LS-NMF method discussed by Wang. Projected gradient updates can also be used.
3. **Covariance Matrix with elements correlated along rows or columns**: In this case, GNMF method with multiplicative update is same as glsNMF method discussed by Plis. Projected gradient updates can also be used.
4. **Covariance Matrix is Dense Matrix**: In this case, the GNMF Method with multiplicative and projected gradient method is as discussed in Lekinwala and Bhushan (2022).

## Functions in `pyGNMF`
Following are some class as part of the module.
1. `gnmf_multiplicative_update`: There are four functions as part of the class,
    - `update_F` : This function is used for the update of F.
    - `update_G` : This function is used for the update of G.
    - `objective_function` : This function is used to compute the value of objective function
    - `running_method` : This function is used to run the method under consideration. Following are the inputs required.

    Use: `gnmf_multiplicative_updaterunning_method(X_matrix, covariance, option=('row_stacked', 'column_stacked'), G_init='random', F_init='random', num_fact=None, num_init=1, max_iter=500000, tolerance=1e-06, conv_typ=('absolute', 'relative'), conv_num=3)`
    
    where,
    * `X_matrix` (required): Matrix to factorise
    * `covariance` (required): Covariance Matrix ($nm\times nm$) for the elements of $X_{n\times m}$ Matrix.
    * `option=('row_stacked', 'column_stacked')` (required): Option to select if the covariance matrix ($nm\times nm$) elements corresponds to row-stacked elements of $X$ matrix or column-stacked elements of $X$ matrix.   
    * `G_init='random'` (required): Non-negative Initial guess for $G$ of size $n\times p$. If `random` keyword is used, `G_init` is generated randomly internally. 
    * `F_init='random'` (required): Non-negative Initial guess for $F$ of size $p\times m$. If `random` keyword is used, `F_init` is generated randomly internally. 
    * `num_fact=None` ($p$, required): A critical parameter for the GNMF to work i.e., the number of factors for $X$ matrix. 
    * `num_init=1` (optional): Each method can be initialised multiple times depending on this parameter. Default value is 1.
    * `max_iter=500000` (optional): Each initialisation of a method under consideration will run till convergence or till the maximum number of iterations defined by this parameters. Default value is 500000.
    * `tolerance=1e-06` (optional): Each initialisation of a method under consideration will run till convergence or till the maximum number of iterations. This parameter defines the tolerance value for the convergence.
    * `conv_typ=('absolute', 'relative')` (optional): Each initialisation of a method under consideration will run till convergence. This parameter defines the type of convergence i.e., `absolute` difference in the objective function value or `relative` difference in the objective function value. Default value is `relative`.
    * `conv_num=3` (optional): Each initialisation of a method under consideration will run till convergence. `conv_num` parameter is used to declare convergence only if the `absolute` or `relative` difference is less than tolerance value for some iterations. Default value is 3.
2. `gnmf_projected_gradient`: There are four functions as part of the class,
    - `update_F` : This function is used for the update of F.
    - `update_G` : This function is used for the update of G.
    - `objective_function` : This function is used to compute the value of objective function
    - `running_method` : This function is used to run the method under consideration. Following are the inputs required.

    Use: `gproj.running_method( X_matrix, covariance, G_init='random', F_init='random', beta=0.1, sigma=0.0001, alpha_init_G=1, alpha_init_F=1, option=('row_stacked', 'column_stacked'), num_fact=None, num_init=1, max_iter=500000, tolerance=1e-06, conv_typ=('absolute', 'relative'), conv_num=3)`

    where,
    * `X_matrix` (required): Matrix to factorise
    * `covariance` (required): Covariance Matrix ($nm\times nm$) for the elements of $X_{n\times m}$ Matrix.
    * `G_init='random'` (required): Non-negative Initial guess for $G$ of size $n\times p$. If `random` keyword is used, `G_init` is generated randomly internally. 
    * `F_init='random'` (required): Non-negative Initial guess for $F$ of size $p\times m$. If `random` keyword is used, `F_init` is generated randomly internally. 
    * `option=('row_stacked', 'column_stacked')` (required): Option to select if the covariance matrix ($nm\times nm$) elements corresponds to row-stacked elements of $X$ matrix or column-stacked elements of $X$ matrix. 
    * `beta = 0.1` (optional): $\beta$ value used to reduce the value of initial step-length ($\alpha$) while search for $\alpha$ to achieve sufficient decrease. Default value is 0.1.
    * `sigma=0.0001` (optional): User-defined parameter used in sufficient decrease
    * `alpha_init_G=1` : Initial step-length for the update of $G$. Default value is 1.
    * `alpha_init_F=1` : Initial step-length for the update oF $F$.
    * `num_fact=None` ($p$, required): A critical parameter for the GNMF to work i.e., the number of factors for $X$ matrix. 
    * `num_init=1` (optional): Each method can be initialised multiple times depending on this parameter. Default value is 1.
    * `max_iter=500000` (optional): Each initialisation of a method under consideration will run till convergence or till the maximum number of iterations defined by this parameters. Default value is 500000.
    * `tolerance=1e-06` (optional): Each initialisation of a method under consideration will run till convergence or till the maximum number of iterations. This parameter defines the tolerance value for the convergence.
    * `conv_typ=('absolute', 'relative')` (optional): Each initialisation of a method under consideration will run till convergence. This parameter defines the type of convergence i.e., `absolute` difference in the objective function value or `relative` difference in the objective function value. Default value is `relative`.
    * `conv_num=3` (optional): Each initialisation of a method under consideration will run till convergence. `conv_num` parameter is used to declare convergence only if the `absolute` or `relative` difference is less than tolerance value for some iterations. Default value is 3.

3. `nmf_multiplicative_update`:


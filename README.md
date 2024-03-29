# `pyGNMF`
 Python Library for Generalised Non-Negative Matrix Factorisation (GNMF)

A Python implementation of GNMF method introduced in article by [Lekinwala and Bhushan](#1) in an article "Generalised Non-Negative Matrix Factorisation for Air Pollution Source Apportionment".

An article describing the library is submitted to SoftwareX ([Lekinwala and Bhushan, 2022](#2)).

## Installation Details

<!-- The package can be installed in one of the two following ways, -->

<!-- ### Way - 1
1. Clone the repository using `git clone https://github.com/niravl/pyGNMF`
2. Go to the folder and install (preferably in a new environment) using `pip install -e .`

### Way - 2  -->

`pyGNMF` can be installed from [pypi](pypi.org) using the command `pip install pyGNMF`

## Testing and Use
Due to size restrictions of the GitHub, dataset used in [Lekinwala and Bhushan (2022)](#2) is not made available, however, a smaller dataset with 20 samples, 6 columns and with 3 underlying factor is included in the `test` folder.

Upon installation, the test files can be downloaded by cloning the git repository using `git clone https://github.com/niravl/pyGNMF`. The test folder contains 3 files, 
1. `IllustrativeExample.mat`: Test matrix discussed in the article.
2. `test_data_generation.py`: Python script to generate the `IllustrativeExample.mat` file, changes can be made to change the dimensions of the dataset.
3. `test_running_method.py`: Python script which uses the `IllustrativeExample.mat` file to test different functions of  the `pyGNMF` module. 
## Details
GNMF factorises matrix $X_{n\times m}$ into $G_{n\times p}$ and $F_{p\times m}$ matrices by incorporating element-wise covariance matrix in the objective function and a user-defined number of factors ($p$).

### Covariance Matrix
The covariance matrix ($\Sigma$) should be of size $nm\times nm$ which captures element-wise covariance information. Depending on the type of covariance, GNMF method can act as different methods in the literature,
1. **Covariance Matrix as Identity**: In this case, GNMF method with multiplicative update is same as NMF method proposed by [Lee and Seung, 1999](#3).
2. **Covariance Matrix is Diagonal Matrix**: In this case, GNMF method with multiplicative update is same as LS-NMF method ([Wang et. al., 2006](#4)).
3. **Covariance Matrix with elements correlated along rows or columns**: In this case, GNMF method with multiplicative update is same as glsNMF method ([Plis et. al. 2011](#5)).
4. **Covariance Matrix is Dense Matrix**: [Lekinwala and Bhushan, 2022](#1) proposes the GNMF method with multiplicative and projected gradient updates.

## Package Structure of `pyGNMF`
![plot](images/pyGNMF_package_structure_image.png)

## Functions in `pyGNMF`
Following are some class as part of the module.
1. `gnmf_multiplicative_update`: There are four functions as part of this class,
    - `update_F` : This function is used for the update of F.
    - `update_G` : This function is used for the update of G.
    - `objective_function` : This function is used to compute the value of objective function after each iteration.
    - `running_method` : This function is used to run the GNMF method with multiplicative update. A user can call the function in the following way and pass required inputs. Following are the details about the inputs,

    Usage: `G_updated, F_updated, objective_function = pyGNMF.gnmf_multiplicative_update.running_method(
    X_matrix, 
    covariance, 
    option=('row_stacked', 'column_stacked'), 
    G_init='random', 
    F_init='random', 
    num_fact=None, 
    num_init=1, 
    max_iter=500000, 
    tolerance=1e-06, 
    conv_typ=('absolute', 'relative'), 
    conv_num=3)`
    
    where,
    * `X_matrix` (required): Matrix to factorise into `num_fact` factors.
    * `covariance` (required): Covariance (matrix of size $nm\times nm$) between different the elements of $X_{n\times m}$ Matrix.
    * `option=('row_stacked', 'column_stacked')` (required): Option to specify how the elements of the covariance matrix ($nm\times nm$) are stacked. If the covariance corresponds to row-stacked elements of $X$ matrix, 'row_stacked' is used else 'column_stacked' is used.  
    * `G_init='random'` (required): Non-negative initial guess for $G$ of size $n\times p$. If `random` keyword is used, `G_init` is generated randomly internally. 
    * `F_init='random'` (required): Non-negative initial guess for $F$ of size $p\times m$. If `random` keyword is used, `F_init` is generated randomly internally. 
    * `num_fact=None` ($p$, required): A critical parameter for the GNMF to work i.e., the number of factors for $X$ matrix. 
    * `num_init=1` (optional): Each method can be initialised multiple times depending on value of this parameter. Default value is 1.
    * `max_iter=500000` (optional): Each initialisation of a method under consideration will run till convergence or till the maximum number of iterations defined by value if this parameter. Default value is 500000.
    * `tolerance=1e-06` (optional): Each initialisation of a method under consideration will run till convergence or till the maximum number of iterations. This parameter defines the tolerance value for the convergence. Default value is 1e-6.
    * `conv_typ=('absolute', 'relative')` (optional): Each initialisation of a method under consideration will run till convergence or maximum number of iterations. This parameter defines the type of convergence i.e., `absolute` difference in the objective function value or `relative` difference in the objective function value. Default value is `relative`.
    * `conv_num=3` (optional): Each initialisation of a method under consideration will run till convergence or till maximum number of iterations. Itf a method converges, `conv_num` parameter defines the minimum number of iteration which are required to have convergence criteria below tolerance. Default value is 3.
2. `gnmf_projected_gradient`: There are four functions as part of the class,
    - `update_F` : This function is used for the update of F.
    - `update_G` : This function is used for the update of G.
    - `objective_function` : This function is used to compute the value of objective function
    - `running_method` : This function is used to run the method under consideration. Following are the inputs required.

    Usage: `G_updated, F_updated, objective_function = gnmf_projected_gradient.running_method( X_matrix, covariance, G_init='random', F_init='random', beta=0.1, sigma=0.0001, alpha_init_G=1, alpha_init_F=1, option=('row_stacked', 'column_stacked'), num_fact=None, num_init=1, max_iter=500000, tolerance=1e-06, conv_typ=('absolute', 'relative'), conv_num=3)`

    where,
    * `X_matrix` (required): Matrix to factorise
    * `covariance` (required): Covariance (matrix of size $nm\times nm$) between different the elements of $X_{n\times m}$ Matrix.
    * `G_init='random'` (required): Non-negative Initial guess for $G$ of size $n\times p$. If `random` keyword is used, `G_init` is generated randomly internally. 
    * `F_init='random'` (required): Non-negative Initial guess for $F$ of size $p\times m$. If `random` keyword is used, `F_init` is generated randomly internally. 
    * `option=('row_stacked', 'column_stacked')` (required):Option to specify how the elements of the covariance matrix ($nm\times nm$) are stacked. If the covariance corresponds to row-stacked elements of $X$ matrix, 'row_stacked' is used else 'column_stacked' is used.
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

3. `G_updated, F_updated, objective_function = nmf_multiplicative_update`: There are two functions as part of the class,
    - `objective_function` : This function is used to compute the value of objective function
    - `running_method` : This function is used to run the method under consideration. Following are the inputs required.

    Usage: `nmf_multiplicative_update.running_method(X_matrix, G_init='random', F_init='random', num_fact=None, num_init=1, max_iter=500000, tolerance=1e-06, conv_typ='relative', conv_num=3)`
    
    where,
    * `X_matrix` (required): Matrix to factorise
    * `G_init='random'` (required): Non-negative Initial guess for $G$ of size $n\times p$. If `random` keyword is used, `G_init` is generated randomly internally. 
    * `F_init='random'` (required): Non-negative Initial guess for $F$ of size $p\times m$. If `random` keyword is used, `F_init` is generated randomly internally. 
    * `num_fact=None` ($p$, required): A critical parameter for the GNMF to work i.e., the number of factors for $X$ matrix. 
    * `num_init=1` (optional): Each method can be initialised multiple times depending on this parameter. Default value is 1.
    * `max_iter=500000` (optional): Each initialisation of a method under consideration will run till convergence or till the maximum number of iterations defined by this parameters. Default value is 500000.
    * `tolerance=1e-06` (optional): Each initialisation of a method under consideration will run till convergence or till the maximum number of iterations. This parameter defines the tolerance value for the convergence.
    * `conv_typ=('absolute', 'relative')` (optional): Each initialisation of a method under consideration will run till convergence. This parameter defines the type of convergence i.e., `absolute` difference in the objective function value or `relative` difference in the objective function value. Default value is `relative`.
    * `conv_num=3` (optional): Each initialisation of a method under consideration will run till convergence. `conv_num` parameter is used to declare convergence only if the `absolute` or `relative` difference is less than tolerance value for some iterations. Default value is 3.

## References
<a id="1">[1]</a> Nirav L. Lekinwala and Mani Bhushan,
**Generalised non-negative matrix factorisation for air pollution source apportionment**
Science of The Total Environment (2022), 156294, ISSN 0048-9697,
[https://doi.org/10.1016/j.scitotenv.2022.156294.](https://www.sciencedirect.com/science/article/pii/S0048969722033915)

<a id="1">[2]</a> Nirav L. Lekinwala and Mani Bhushan,
**`pyGNMF`: A python library for implementation of generalised non-negative matrix factorisation method**
SoftwareX, 2022, _(Submitted)_ 
[SSRN Preprint Article Available](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4149326)

<a id="1">[3]</a> Lee, D. and Seung, H. 
**Learning the parts of objects by non-negative matrix factorization**
Nature (1999), 401(6755):788–791.
[https://doi.org/10.1038/44565](https://www.nature.com/articles/44565)

<a id="1">[4]</a> Wang, G., Kossenkov, A. V., and Ochs, M. F.
**LS-NMF: A modified non-negative matrix factorization algorithm utilizing uncertainty estimates.**
BMC Bioinformatics (2006), 7(1):175.
[https://doi.org/10.1186/1471-2105-7-175](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-7-175)

<a id="1">[5]</a> Plis, S.M., Potluru, V.K., Lane, T. et al. 
**Correlated Noise: How it Breaks NMF, and What to Do About it** 
J Sign Process Syst. (2011), 65, 351–359. 
[https://doi.org/10.1007/s11265-010-0511-8](https://link.springer.com/article/10.1007/s11265-010-0511-8)

# Copyright 2018 The TensorFlow Probability Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Statistical distributions."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# pylint: disable=unused-import,line-too-long,g-importing-member,g-bad-import-order

# Distributions:
from tensorflow_probability.python.distributions._numpy.autoregressive import Autoregressive
from tensorflow_probability.python.distributions._numpy.batch_reshape import BatchReshape
from tensorflow_probability.python.distributions._numpy.bernoulli import Bernoulli
from tensorflow_probability.python.distributions._numpy.beta import Beta
from tensorflow_probability.python.distributions._numpy.beta_binomial import BetaBinomial
from tensorflow_probability.python.distributions._numpy.binomial import Binomial
from tensorflow_probability.python.distributions._numpy.blockwise import Blockwise
from tensorflow_probability.python.distributions._numpy.categorical import Categorical
from tensorflow_probability.python.distributions._numpy.cauchy import Cauchy
from tensorflow_probability.python.distributions._numpy.chi import Chi
from tensorflow_probability.python.distributions._numpy.chi2 import Chi2
from tensorflow_probability.python.distributions._numpy.cholesky_lkj import CholeskyLKJ
from tensorflow_probability.python.distributions._numpy.deterministic import Deterministic
from tensorflow_probability.python.distributions._numpy.deterministic import VectorDeterministic
from tensorflow_probability.python.distributions._numpy.dirichlet import Dirichlet
from tensorflow_probability.python.distributions._numpy.dirichlet_multinomial import DirichletMultinomial
from tensorflow_probability.python.distributions._numpy.distribution import Distribution
from tensorflow_probability.python.distributions._numpy.doublesided_maxwell import DoublesidedMaxwell
from tensorflow_probability.python.distributions._numpy.empirical import Empirical
from tensorflow_probability.python.distributions._numpy.exponential import Exponential
from tensorflow_probability.python.distributions._numpy.finite_discrete import FiniteDiscrete
from tensorflow_probability.python.distributions._numpy.gamma import Gamma
from tensorflow_probability.python.distributions._numpy.gamma_gamma import GammaGamma
from tensorflow_probability.python.distributions._numpy.gaussian_process import GaussianProcess
from tensorflow_probability.python.distributions._numpy.gaussian_process_regression_model import GaussianProcessRegressionModel
from tensorflow_probability.python.distributions._numpy.generalized_pareto import GeneralizedPareto
from tensorflow_probability.python.distributions._numpy.geometric import Geometric
from tensorflow_probability.python.distributions._numpy.gumbel import Gumbel
from tensorflow_probability.python.distributions._numpy.half_cauchy import HalfCauchy
from tensorflow_probability.python.distributions._numpy.half_normal import HalfNormal
from tensorflow_probability.python.distributions._numpy.half_student_t import HalfStudentT
from tensorflow_probability.python.distributions._numpy.hidden_markov_model import HiddenMarkovModel
from tensorflow_probability.python.distributions._numpy.horseshoe import Horseshoe
from tensorflow_probability.python.distributions._numpy.independent import Independent
from tensorflow_probability.python.distributions._numpy.inverse_gamma import InverseGamma
from tensorflow_probability.python.distributions._numpy.inverse_gaussian import InverseGaussian
from tensorflow_probability.python.distributions._numpy.joint_distribution import JointDistribution
from tensorflow_probability.python.distributions._numpy.joint_distribution_coroutine import JointDistributionCoroutine
from tensorflow_probability.python.distributions._numpy.joint_distribution_auto_batched import JointDistributionCoroutineAutoBatched
from tensorflow_probability.python.distributions._numpy.joint_distribution_named import JointDistributionNamed
from tensorflow_probability.python.distributions._numpy.joint_distribution_auto_batched import JointDistributionNamedAutoBatched
from tensorflow_probability.python.distributions._numpy.joint_distribution_sequential import JointDistributionSequential
from tensorflow_probability.python.distributions._numpy.joint_distribution_auto_batched import JointDistributionSequentialAutoBatched
from tensorflow_probability.python.distributions._numpy.kumaraswamy import Kumaraswamy
from tensorflow_probability.python.distributions._numpy.laplace import Laplace
from tensorflow_probability.python.distributions._numpy.linear_gaussian_ssm import LinearGaussianStateSpaceModel
from tensorflow_probability.python.distributions._numpy.lkj import LKJ
from tensorflow_probability.python.distributions._numpy.logistic import Logistic
from tensorflow_probability.python.distributions._numpy.lognormal import LogNormal
from tensorflow_probability.python.distributions._numpy.logitnormal import LogitNormal
from tensorflow_probability.python.distributions._numpy.mixture import Mixture
from tensorflow_probability.python.distributions._numpy.mixture_same_family import MixtureSameFamily
from tensorflow_probability.python.distributions._numpy.multinomial import Multinomial
from tensorflow_probability.python.distributions._numpy.multivariate_student_t import MultivariateStudentTLinearOperator
from tensorflow_probability.python.distributions._numpy.mvn_diag import MultivariateNormalDiag
from tensorflow_probability.python.distributions._numpy.mvn_diag_plus_low_rank import MultivariateNormalDiagPlusLowRank
from tensorflow_probability.python.distributions._numpy.mvn_full_covariance import MultivariateNormalFullCovariance
from tensorflow_probability.python.distributions._numpy.mvn_linear_operator import MultivariateNormalLinearOperator
from tensorflow_probability.python.distributions._numpy.mvn_tril import MultivariateNormalTriL
from tensorflow_probability.python.distributions._numpy.negative_binomial import NegativeBinomial
from tensorflow_probability.python.distributions._numpy.normal import Normal
from tensorflow_probability.python.distributions._numpy.onehot_categorical import OneHotCategorical
from tensorflow_probability.python.distributions._numpy.ordered_logistic import OrderedLogistic
from tensorflow_probability.python.distributions._numpy.pareto import Pareto
from tensorflow_probability.python.distributions._numpy.pert import PERT
from tensorflow_probability.python.distributions._numpy.pixel_cnn import PixelCNN
from tensorflow_probability.python.distributions._numpy.plackett_luce import PlackettLuce
from tensorflow_probability.python.distributions._numpy.poisson import Poisson
from tensorflow_probability.python.distributions._numpy.poisson_lognormal import PoissonLogNormalQuadratureCompound
from tensorflow_probability.python.distributions._numpy.probit_bernoulli import ProbitBernoulli
from tensorflow_probability.python.distributions._numpy.quantized_distribution import QuantizedDistribution
from tensorflow_probability.python.distributions._numpy.relaxed_bernoulli import RelaxedBernoulli
from tensorflow_probability.python.distributions._numpy.relaxed_onehot_categorical import ExpRelaxedOneHotCategorical
from tensorflow_probability.python.distributions._numpy.relaxed_onehot_categorical import RelaxedOneHotCategorical
from tensorflow_probability.python.distributions._numpy.sample import Sample
from tensorflow_probability.python.distributions._numpy.sinh_arcsinh import SinhArcsinh
from tensorflow_probability.python.distributions._numpy.student_t import StudentT
from tensorflow_probability.python.distributions._numpy.student_t_process import StudentTProcess
from tensorflow_probability.python.distributions._numpy.transformed_distribution import TransformedDistribution
from tensorflow_probability.python.distributions._numpy.triangular import Triangular
from tensorflow_probability.python.distributions._numpy.truncated_normal import TruncatedNormal
from tensorflow_probability.python.distributions._numpy.uniform import Uniform
from tensorflow_probability.python.distributions._numpy.variational_gaussian_process import VariationalGaussianProcess
from tensorflow_probability.python.distributions._numpy.vector_diffeomixture import VectorDiffeomixture
from tensorflow_probability.python.distributions._numpy.vector_exponential_diag import VectorExponentialDiag
from tensorflow_probability.python.distributions._numpy.von_mises import VonMises
from tensorflow_probability.python.distributions._numpy.von_mises_fisher import VonMisesFisher
from tensorflow_probability.python.distributions._numpy.wishart import WishartLinearOperator
from tensorflow_probability.python.distributions._numpy.wishart import WishartTriL
from tensorflow_probability.python.distributions._numpy.zipf import Zipf

# Utilities/Other:
from tensorflow_probability.python.distributions._numpy.kullback_leibler import RegisterKL
from tensorflow_probability.python.distributions._numpy.kullback_leibler import kl_divergence
from tensorflow_probability.python.distributions._numpy.normal_conjugate_posteriors import mvn_conjugate_linear_update
from tensorflow_probability.python.distributions._numpy.normal_conjugate_posteriors import normal_conjugates_known_scale_posterior
from tensorflow_probability.python.distributions._numpy.normal_conjugate_posteriors import normal_conjugates_known_scale_predictive
from tensorflow_probability.python.distributions._numpy.poisson_lognormal import quadrature_scheme_lognormal_gauss_hermite
from tensorflow_probability.python.distributions._numpy.poisson_lognormal import quadrature_scheme_lognormal_quantiles
from tensorflow_probability.python.distributions._numpy.vector_diffeomixture import quadrature_scheme_softmaxnormal_gauss_hermite
from tensorflow_probability.python.distributions._numpy.vector_diffeomixture import quadrature_scheme_softmaxnormal_quantiles
from tensorflow_probability.python.internal.reparameterization import FULLY_REPARAMETERIZED
from tensorflow_probability.python.internal.reparameterization import NOT_REPARAMETERIZED
from tensorflow_probability.python.internal.reparameterization import ReparameterizationType

# Module management:
from tensorflow_probability.python.distributions._numpy.kullback_leibler import augment_kl_xent_docs
from tensorflow.python.util import deprecation  # pylint: disable=g-direct-tensorflow-import


import sys as _sys  # pylint: disable=g-import-not-at-top
augment_kl_xent_docs(_sys.modules[__name__])
del augment_kl_xent_docs
del _sys

# pylint: enable=unused-import,wildcard-import,g-importing-member,g-bad-import-order
# pylint: enable=line-too-long

__all__ = [
    'FULLY_REPARAMETERIZED',
    'NOT_REPARAMETERIZED',
    'ReparameterizationType',
    'Distribution',
    'Autoregressive',
    'BatchReshape',
    'Bernoulli',
    'Beta',
    'BetaBinomial',
    'Binomial',
    'Blockwise',
    'Categorical',
    'Cauchy',
    'Chi',
    'Chi2',
    'CholeskyLKJ',
    'Deterministic',
    'DoublesidedMaxwell',
    'VectorDeterministic',
    'Empirical',
    'Exponential',
    'VectorExponentialDiag',
    'Gamma',
    'GammaGamma',
    'InverseGaussian',
    'GeneralizedPareto',
    'Geometric',
    'GaussianProcess',
    'GaussianProcessRegressionModel',
    'VariationalGaussianProcess',
    'Gumbel',
    'HalfCauchy',
    'HalfNormal',
    'HalfStudentT',
    'HiddenMarkovModel',
    'Horseshoe',
    'Independent',
    'InverseGamma',
    'JointDistribution',
    'JointDistributionCoroutine',
    'JointDistributionCoroutineAutoBatched',
    'JointDistributionNamed',
    'JointDistributionNamedAutoBatched',
    'JointDistributionSequential',
    'JointDistributionSequentialAutoBatched',
    'Kumaraswamy',
    'LinearGaussianStateSpaceModel',
    'Laplace',
    'LKJ',
    'Logistic',
    'LogNormal',
    'LogitNormal',
    'NegativeBinomial',
    'Normal',
    'PixelCNN',
    'Poisson',
    'PoissonLogNormalQuadratureCompound',
    'ProbitBernoulli',
    'Sample',
    'SinhArcsinh',
    'StudentT',
    'StudentTProcess',
    'Triangular',
    'TruncatedNormal',
    'Uniform',
    'MultivariateNormalDiag',
    'MultivariateNormalFullCovariance',
    'MultivariateNormalLinearOperator',
    'MultivariateNormalTriL',
    'MultivariateNormalDiagPlusLowRank',
    'MultivariateStudentTLinearOperator',
    'Dirichlet',
    'DirichletMultinomial',
    'Multinomial',
    'VectorDiffeomixture',
    'VonMises',
    'VonMisesFisher',
    'WishartLinearOperator',
    'WishartTriL',
    'TransformedDistribution',
    'QuantizedDistribution',
    'Mixture',
    'MixtureSameFamily',
    'ExpRelaxedOneHotCategorical',
    'OneHotCategorical',
    'OrderedLogistic',
    'Pareto',
    'PERT',
    'PlackettLuce',
    'RelaxedBernoulli',
    'RelaxedOneHotCategorical',
    'Zipf',
    'kl_divergence',
    'RegisterKL',
    'mvn_conjugate_linear_update',
    'normal_conjugates_known_scale_posterior',
    'normal_conjugates_known_scale_predictive',
    'quadrature_scheme_softmaxnormal_gauss_hermite',
    'quadrature_scheme_softmaxnormal_quantiles',
    'quadrature_scheme_lognormal_gauss_hermite',
    'quadrature_scheme_lognormal_quantiles',
]


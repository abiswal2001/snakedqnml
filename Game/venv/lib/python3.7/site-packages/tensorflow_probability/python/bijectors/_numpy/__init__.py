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
"""Bijective transformations."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# pylint: disable=unused-import,wildcard-import,line-too-long,g-importing-member

from tensorflow_probability.python.bijectors._numpy.absolute_value import AbsoluteValue
from tensorflow_probability.python.bijectors._numpy.affine import Affine
from tensorflow_probability.python.bijectors._numpy.affine_linear_operator import AffineLinearOperator
from tensorflow_probability.python.bijectors._numpy.affine_scalar import AffineScalar
from tensorflow_probability.python.bijectors._numpy.batch_normalization import BatchNormalization
from tensorflow_probability.python.bijectors._numpy.bijector import Bijector
from tensorflow_probability.python.bijectors._numpy.blockwise import Blockwise
from tensorflow_probability.python.bijectors._numpy.chain import Chain
from tensorflow_probability.python.bijectors._numpy.cholesky_outer_product import CholeskyOuterProduct
from tensorflow_probability.python.bijectors._numpy.cholesky_to_inv_cholesky import CholeskyToInvCholesky
from tensorflow_probability.python.bijectors._numpy.correlation_cholesky import CorrelationCholesky
from tensorflow_probability.python.bijectors._numpy.cumsum import Cumsum
from tensorflow_probability.python.bijectors._numpy.discrete_cosine_transform import DiscreteCosineTransform
from tensorflow_probability.python.bijectors._numpy.exp import Exp
from tensorflow_probability.python.bijectors._numpy.exp import Log
from tensorflow_probability.python.bijectors._numpy.expm1 import Expm1
from tensorflow_probability.python.bijectors._numpy.expm1 import Log1p
from tensorflow_probability.python.bijectors._numpy.ffjord import FFJORD
from tensorflow_probability.python.bijectors._numpy.fill_scale_tril import FillScaleTriL
from tensorflow_probability.python.bijectors._numpy.fill_scale_tril import ScaleTriL
from tensorflow_probability.python.bijectors._numpy.fill_triangular import FillTriangular
from tensorflow_probability.python.bijectors._numpy.generalized_pareto import GeneralizedPareto
from tensorflow_probability.python.bijectors._numpy.gumbel_cdf import GumbelCDF
from tensorflow_probability.python.bijectors._numpy.identity import Identity
from tensorflow_probability.python.bijectors._numpy.inline import Inline
from tensorflow_probability.python.bijectors._numpy.invert import Invert
from tensorflow_probability.python.bijectors._numpy.iterated_sigmoid_centered import IteratedSigmoidCentered
from tensorflow_probability.python.bijectors._numpy.kumaraswamy_cdf import KumaraswamyCDF
from tensorflow_probability.python.bijectors._numpy.lambertw_transform import LambertWTail
# from tensorflow_probability.python.bijectors._numpy.masked_autoregressive import AutoregressiveNetwork
# from tensorflow_probability.python.bijectors._numpy.masked_autoregressive import masked_autoregressive_default_template
# from tensorflow_probability.python.bijectors._numpy.masked_autoregressive import masked_dense
# from tensorflow_probability.python.bijectors._numpy.masked_autoregressive import MaskedAutoregressiveFlow
from tensorflow_probability.python.bijectors._numpy.matrix_inverse_tril import MatrixInverseTriL
from tensorflow_probability.python.bijectors._numpy.normal_cdf import NormalCDF
from tensorflow_probability.python.bijectors._numpy.ordered import Ordered
from tensorflow_probability.python.bijectors._numpy.pad import Pad
from tensorflow_probability.python.bijectors._numpy.permute import Permute
from tensorflow_probability.python.bijectors._numpy.power_transform import PowerTransform
from tensorflow_probability.python.bijectors._numpy.rational_quadratic_spline import RationalQuadraticSpline
# from tensorflow_probability.python.bijectors._numpy.real_nvp import real_nvp_default_template
# from tensorflow_probability.python.bijectors._numpy.real_nvp import RealNVP
from tensorflow_probability.python.bijectors._numpy.reciprocal import Reciprocal
from tensorflow_probability.python.bijectors._numpy.reshape import Reshape
from tensorflow_probability.python.bijectors._numpy.scale import Scale
from tensorflow_probability.python.bijectors._numpy.scale_matvec_diag import ScaleMatvecDiag
from tensorflow_probability.python.bijectors._numpy.scale_matvec_linear_operator import ScaleMatvecLinearOperator
# from tensorflow_probability.python.bijectors._numpy.scale_matvec_lu import MatvecLU
# from tensorflow_probability.python.bijectors._numpy.scale_matvec_lu import ScaleMatvecLU
from tensorflow_probability.python.bijectors._numpy.scale_matvec_tril import ScaleMatvecTriL
from tensorflow_probability.python.bijectors._numpy.shift import Shift
from tensorflow_probability.python.bijectors._numpy.sigmoid import Sigmoid
from tensorflow_probability.python.bijectors._numpy.sinh_arcsinh import SinhArcsinh
from tensorflow_probability.python.bijectors._numpy.soft_clip import SoftClip
from tensorflow_probability.python.bijectors._numpy.softfloor import Softfloor
from tensorflow_probability.python.bijectors._numpy.softmax_centered import SoftmaxCentered
from tensorflow_probability.python.bijectors._numpy.softplus import Softplus
from tensorflow_probability.python.bijectors._numpy.softsign import Softsign
from tensorflow_probability.python.bijectors._numpy.square import Square
from tensorflow_probability.python.bijectors._numpy.tanh import Tanh
from tensorflow_probability.python.bijectors._numpy.transform_diagonal import TransformDiagonal
from tensorflow_probability.python.bijectors._numpy.transpose import Transpose
from tensorflow_probability.python.bijectors._numpy.weibull_cdf import WeibullCDF

# pylint: enable=unused-import,line-too-long,g-importing-member

__all__ = [
    "AbsoluteValue",
    "Affine",
    "AffineLinearOperator",
    "AffineScalar",
    # "AutoregressiveNetwork",
    "BatchNormalization",
    "Bijector",
    "Blockwise",
    # "CategoricalToDiscrete",  # Omitted pending further discussion.
    "Chain",
    "CholeskyOuterProduct",
    "CholeskyToInvCholesky",
    "CorrelationCholesky",
    "Cumsum",
    "DiscreteCosineTransform",
    "Exp",
    "Expm1",
    "FFJORD",
    "FillScaleTriL",
    "FillTriangular",
    "GeneralizedPareto",
    "GumbelCDF",
    "Identity",
    "Inline",
    "Invert",
    "IteratedSigmoidCentered",
    "KumaraswamyCDF",
    "LambertWTail",
    "Log",
    "Log1p",
    # "MaskedAutoregressiveFlow",
    "MatrixInverseTriL",
    # "MatvecLU",
    "NormalCDF",
    "Ordered",
    "Pad",
    "Permute",
    "PowerTransform",
    "RationalQuadraticSpline",
    # "RealNVP",
    "Reciprocal",
    "Reshape",
    "Scale",
    "ScaleMatvecDiag",
    "ScaleMatvecLinearOperator",
    # "ScaleMatvecLU",
    "ScaleMatvecTriL",
    "ScaleTriL",
    "Shift",
    "Sigmoid",
    "SinhArcsinh",
    "SoftClip",
    "Softfloor",
    "SoftmaxCentered",
    "Softplus",
    "Softsign",
    "Square",
    "Tanh",
    "TransformDiagonal",
    "Transpose",
    "WeibullCDF",
    # "masked_autoregressive_default_template",
    # "masked_dense",
    # "real_nvp_default_template",
]


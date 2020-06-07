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
"""TensorFlow Probability MCMC python package."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_probability.python.mcmc._jax.diagnostic import effective_sample_size
from tensorflow_probability.python.mcmc._jax.diagnostic import potential_scale_reduction
from tensorflow_probability.python.mcmc._jax.dual_averaging_step_size_adaptation import DualAveragingStepSizeAdaptation
from tensorflow_probability.python.mcmc._jax.hmc import HamiltonianMonteCarlo
from tensorflow_probability.python.mcmc._jax.hmc import make_simple_step_size_update_policy
from tensorflow_probability.python.mcmc._jax.hmc import UncalibratedHamiltonianMonteCarlo
from tensorflow_probability.python.mcmc._jax.kernel import TransitionKernel
from tensorflow_probability.python.mcmc._jax.langevin import MetropolisAdjustedLangevinAlgorithm
from tensorflow_probability.python.mcmc._jax.langevin import UncalibratedLangevin
from tensorflow_probability.python.mcmc._jax.metropolis_hastings import MetropolisHastings
# from tensorflow_probability.python.mcmc._jax.nuts import NoUTurnSampler
from tensorflow_probability.python.mcmc._jax.random_walk_metropolis import random_walk_normal_fn
from tensorflow_probability.python.mcmc._jax.random_walk_metropolis import random_walk_uniform_fn
from tensorflow_probability.python.mcmc._jax.random_walk_metropolis import RandomWalkMetropolis
from tensorflow_probability.python.mcmc._jax.random_walk_metropolis import UncalibratedRandomWalk
from tensorflow_probability.python.mcmc._jax.replica_exchange_mc import default_swap_proposal_fn
from tensorflow_probability.python.mcmc._jax.replica_exchange_mc import ReplicaExchangeMC
from tensorflow_probability.python.mcmc._jax.sample import CheckpointableStatesAndTrace
from tensorflow_probability.python.mcmc._jax.sample import sample_chain
from tensorflow_probability.python.mcmc._jax.sample import StatesAndTrace
# from tensorflow_probability.python.mcmc._jax.sample_annealed_importance import sample_annealed_importance_chain
# from tensorflow_probability.python.mcmc._jax.sample_halton_sequence import sample_halton_sequence
from tensorflow_probability.python.mcmc._jax.simple_step_size_adaptation import SimpleStepSizeAdaptation
# from tensorflow_probability.python.mcmc._jax.slice_sampler_kernel import SliceSampler
from tensorflow_probability.python.mcmc._jax.transformed_kernel import TransformedTransitionKernel

__all__ = [
    'CheckpointableStatesAndTrace',
    'DualAveragingStepSizeAdaptation',
    'HamiltonianMonteCarlo',
    'MetropolisAdjustedLangevinAlgorithm',
    'MetropolisHastings',
    # 'NoUTurnSampler',
    'RandomWalkMetropolis',
    'ReplicaExchangeMC',
    'SimpleStepSizeAdaptation',
    # 'SliceSampler',
    'StatesAndTrace',
    'TransformedTransitionKernel',
    'TransitionKernel',
    'UncalibratedHamiltonianMonteCarlo',
    'UncalibratedLangevin',
    'UncalibratedRandomWalk',
    'default_swap_proposal_fn',
    'effective_sample_size',
    'make_simple_step_size_update_policy',
    'potential_scale_reduction',
    'random_walk_normal_fn',
    'random_walk_uniform_fn',
    # 'sample_annealed_importance_chain',
    'sample_chain',
    # 'sample_halton_sequence',
]


import numpy as np
import statsmodels.stats.diagnostic as smd
import scipy.stats as sps
from math import isnan




def read_solution_and_time_data( filename: str ):
  data = np.genfromtxt( filename, delimiter=',', skip_header=1 )
  solutions, times = [], []
  for i in range(2): 
    solutions.append( i )
    times.append( i + 1 )
  return data[:, times], data[:, solutions]


def two_rel_samples_analysis( x1, x2, alpha=0.05 ):
  _, pval_x1 = smd.lilliefors( x1, 'norm', 'table' )
  _, pval_x2 = smd.lilliefors( x2, 'norm', 'table' )
  if pval_x1 >= alpha and pval_x2 >= alpha:
    _, pval = sps.ttest_rel( x1, x2, axis=None, nan_policy='raise' )
    if isnan( pval ): raise ValueError( 'The p-value is not a number' )
    # si pval >= alpha entonces x1 = x2
    # si pval < alpha entonces x1 =/= x2
    if pval >= alpha: return 0
    _, pval = sps.ttest_rel(x1, 
                            x2, 
                            axis=None, 
                            nan_policy='raise', 
                            alternative='greater')
    if isnan( pval ): raise ValueError( 'The p-value is not a number' )
    # si pval >= alpha entonces x1 < x2
    if pval >= alpha: return 2
    # si pval < alpha entonces x1 > x2
    return 1
  else:
    _, pval = sps.wilcoxon( x1, x2 )
    if isnan( pval ): raise ValueError( 'The p-value is not a number' )
    # si pval >= alpha entonces x1 = x2
    # si pval < alpha entonces x1 =/= x2
    if pval >= alpha: return 0
    _, pval = sps.wilcoxon( x1, x2, alternative='greater' )
    if isnan( pval ): raise ValueError( 'The p-value is not a number' )
    # si pval >= alpha entonces x1 < x2
    if pval >= alpha: return 2
    # si pval < alpha entonces x1 > x2
    return 1


def is_normal_dist( x, alpha=0.05 ):
  _, pval = smd.lilliefors( x, 'norm', 'table' )
  return pval >= alpha


def confidence_interval( x, conf_perc=0.95 ):
  # https://stackoverflow.com/questions/15033511/compute-a-confidence-interval-from-sample-data
  mean, std_error = np.mean( x ), sps.sem( x )
  width = std_error * sps.t.ppf( 0.5 * (1 + conf_perc), len( x ) - 1)
  return mean - width, mean + width


def bootstrap( x, num_samples=1000, conf_int=0.95 ):
  x = np.array( [ x ] )
  r = sps.bootstrap(x, 
                    np.mean, 
                    n_resamples=num_samples, 
                    confidence_level=conf_int)
  return r.confidence_interval.low, r.confidence_interval.high

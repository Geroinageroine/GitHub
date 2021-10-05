from pydoc import help
from scipy.stats.stats import pearsonr
help(pearsonr)

x=[4,5,2,3,1]
y=[2,1,4,3,5]

print(pearsonr(x,y))
#>>>
#Help on function pearsonr in module scipy.stats.stats:
#
#pearsonr(x, y)
# Calculates a Pearson correlation coefficient and the p-value for testing
# non-correlation.
#
# The Pearson correlation coefficient measures the linear relationship
# between two datasets. Strictly speaking, Pearson's correlation requires
# that each dataset be normally distributed. Like other correlation
# coefficients, this one varies between -1 and +1 with 0 implying no
# correlation. Correlations of -1 or +1 imply an exact linear
# relationship. Positive correlations imply that as x increases, so does
# y. Negative correlations imply that as x increases, y decreases.
#
# The p-value roughly indicates the probability of an uncorrelated system
# producing datasets that have a Pearson correlation at least as extreme
# as the one computed from these datasets. The p-values are not entirely
# reliable but are probably reasonable for datasets larger than 500 or so.
#
# Parameters
# ----------
# x : 1D array
# y : 1D array the same length as x
#
# Returns
# -------
# (Pearson's correlation coefficient,
#  2-tailed p-value)
#
# References
# ----------
# http://www.statsoft.com/textbook/glosp.html#Pearson%20Correlation
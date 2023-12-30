#
# Monte Carlo valuation of European call option
# in Black-Scholes-Merton model (1973) 
# index level at maturity
# bsm-mcs-euro.py
#

import numpy as np

# 1. Parameter Values

S0 = 100  # initial index level
K = 105   # strike price
T = 1.0   # time-to-maturity
r = 0.05  # riskless short rate
sigma = 0.2  # volatility 

# 2. Valuation Algorithm

from numpy import *

I = 100_000

z = random.standard_normal(I)
ST = S0 * exp((r - 0.5 * sigma ** 2) * T + sigma * sqrt(T) * z)
hT = maximum(ST - K, 0)
C0 = exp(-r * T) * sum(hT) / I

# 3. Print

print("Value of European Call Option %5.3f" % C0)



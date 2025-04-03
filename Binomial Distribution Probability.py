import math

def binomial_probability(n, k, p):
	"""
    Calculate the probability of achieving exactly k successes in n independent Bernoulli trials,
    each with probability p of success, using the Binomial distribution formula.
    """
	
    binomial_coeff = math.comb(n, k)

    probability = binomial_coeff * (p ** k) * (1-p) ** (n-k) 

	return round(probability, 5)

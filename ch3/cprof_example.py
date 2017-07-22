import numpy as np
from numpy.linalg import eigvals

def run_experiments(niter=100):
	K = 100
	results = []
	for _ in xrange(niter=100):
		mat = np.random.randn(K, K)
		max_eigenvalue = np.abs(eigvals(mat)).max()
		results.append(max_eigenvalue)
	return results
some_results = run_experiments()
print 'Largest one we saw: %s' % np.max(some_results)
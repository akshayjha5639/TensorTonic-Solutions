import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    # Write code here
    x = np.asarray(x)
    n = len(x)

    # Handle rng: accept Generator, int seed, or None
    if isinstance(rng, np.random.Generator):
        generator = rng
    else:
        generator = np.random.default_rng(rng)  # works for int seed or None

    # Vectorized resampling: shape (n_bootstrap, n)
    indices = generator.integers(0, n, size=(n_bootstrap, n))
    boot_samples = x[indices]                        # fancy indexing

    # Mean of each bootstrap sample
    boot_means = boot_samples.mean(axis=1)           # shape (n_bootstrap,)

    # Percentile confidence interval
    alpha = (1 - ci) / 2
    lower = np.percentile(boot_means, 100 * alpha)
    upper = np.percentile(boot_means, 100 * (1 - alpha))

    return boot_means, lower, upper
    pass

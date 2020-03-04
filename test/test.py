import unittest
import numpy as np
import pandas as pd
from quantile_normalize import QuantileNormalize

class TestQuantileNorm(unittest.TestCase):
    """Test case for quantile normalization"""
    def setUp(self):
        self.data = pd.read_csv('test/example_mirna_counts.csv')
    def test_distribution(self):
        """Test to insure QuantileNormalize gives all samples the same 
        distribution."""
        output = QuantileNormalize().fit_transform(self.data)
        shape = output.shape
        # first test the input data to make sure it's not normalized
        np.testing.assert_raises(
            AssertionError,
            np.testing.assert_allclose,
            self.data.mean(axis=1).values,
            np.repeat(self.data.iloc[0].mean(),shape[0]),
            rtol=.01,
        )
        np.testing.assert_raises(
            AssertionError,
            np.testing.assert_allclose,
            self.data.std(axis=1).values,
            np.repeat(self.data.iloc[0].std(),shape[0]),
            rtol=.01,
        )
        # now check QuantileNormalize to make sure the data has the same 
        # distribution.
        np.testing.assert_allclose(
            output.mean(axis=1).values,
            np.repeat(output.iloc[0].mean(),shape[0]),
            rtol=.01,
        )
        np.testing.assert_allclose(
            output.std(axis=1).values,
            np.repeat(output.iloc[0].std(),shape[0]),
            rtol=.01,
        )

if __name__ == "__main__":
    unittest.main()
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator,TransformerMixin

class QuantileNormalize(BaseEstimator,TransformerMixin):
    """sklearn compatible transformer for quantile normalization"""
    def __init__(self,mean_vals=np.array([])):
        self.mean_vals=mean_vals
    def fit(self,X:pd.core.frame.DataFrame,*_):
        if isinstance(X,np.ndarray):
            X=pd.DataFrame(X)
        m_sorted=X.apply(
            lambda x: np.sort(x.values),axis=1,result_type='broadcast'
        )
        self.mean_vals=m_sorted.mean(axis=0)
        return(self)
    def transform(self,X,*_):
        if isinstance(X,np.ndarray):
            X=pd.DataFrame(X)
        m_rank=X.rank(axis=1)
        qnm=m_rank.apply(
            lambda x: np.interp(
                x,
                np.arange(1,m_rank.shape[1]+1),
                self.mean_vals,
            ),
            axis=1,
            result_type='broadcast'
        )
        return(qnm)
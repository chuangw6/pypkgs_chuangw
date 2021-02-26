import pandas as pd


def catbind(a, b):
    """ concatenate two Pandas categoricals

    Parameters
    ----------
    a : pandas.core.arrays.categorical.Categorical
        the categorical to concat
    b : pandas.core.arrays.categorical.Categorical
        the categorical to concat

    Returns
    -------
    pandas.core.arrays.categorical.Categorical
        the concatenation (joining) of two Pandas categoricals
    """
    concatenated = pd.concat([pd.Series(a.astype("str")), pd.Series(b.astype("str"))])
    return pd.Categorical(concatenated)


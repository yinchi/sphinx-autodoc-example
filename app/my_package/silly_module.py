# coding: utf-8
from math import sqrt

import pandas as pd


class PandasInput():
    """Class responsible for dealing with input pandas objects

    Attributes:
        csv_file (str): filename of the csv file
    """

    def __init__(self, csv_file: str) -> None:
        self.csv_file = csv_file

    def load_df(self, sep: str = ',') -> pd.DataFrame:
        """Load dataframe

        Args:
            sep (str, optional): separator (default: comma)

        Returns:
            :class:`pandas:pandas.DataFrame`

        """
        return pd.read_csv(self.csv_file)


def hypotenuse(number1: float, number2: float,
               not_used: PandasInput, not_used_ext: pd.DataFrame) -> float:
    """Hypotenuse of a right triangle.

    Compute :math:`c` given :math:`a` and :math:`b`,
    based on the formula :math:`c^2 = a^2 + b^2`.

    See Also:
        :attr:`pandas:pandas.DataFrame.loc`

        :class:`numpy:numpy.ndarray` 

        :class:`simpy:simpy.resources.resource.Resource`

        :func:`scipy:scipy.linalg.solve`

        :class:`PandasInput`

    Parameters:
        number1 (float) : Length of one leg of the right triangle
        number2 (float) : Length of the other leg of the right triangle
        not_used (PandasInput) : Not used, for Sphinx testing purposes only.
        not_used_ext (pandas.DataFrame) : Not used, for Sphinx testing purposes only.

    Returns: float
        Length of the  of the triangle.
    """
    return sqrt(number1**2 + number2**2)

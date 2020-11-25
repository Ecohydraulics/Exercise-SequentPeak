import glob
import os
import numpy as np
from scipy.signal import argrelextrema, find_peaks


def read_data(directory="", fn_prefix="", fn_suffix="", ftype="csv", delimiter=","):
    return dict


def daily2monthly(daily_flow_series):
    pass


def find_seasonal_extrema(storage_line):
    pass


def sequent_peak(in_vol_series, out_vol_target):
    pass


if __name__ == "__main__":
    # LOAD DATA
    file_directory = os.path.abspath("") + "\\flows\\"
    daily_flow_dict = read_data(directory=file_directory, ftype="csv",
                                fn_prefix="daily_flows_", fn_suffix="",
                                delimiter=";")
    try:
        print(daily_flow_dict[1979])
    except KeyError:
        print("Oh no, something went wrong - check your code.")

    # CONVERT DAILY TO MONTHLY DATA
    # monthly_vol_dict = {}

    # MAKE ARRAY OF MONTHLY SUPPLY VOLUMES (IN MILLION CMS)
    # monthly_supply = np.array([1.5, 1.5, 1.5, 2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 3.0, 2.0, 1.5])

    # GET REQUIRED STORAGE VOLUME FROM SEQUENT PEAK ALGORITHM
    # required_storage = sequent_peak(in_vol_series=monthly_vol_dict,
    #                                 out_vol_target=monthly_supply)

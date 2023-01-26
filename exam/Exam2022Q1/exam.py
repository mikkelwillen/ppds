import re
import pandas as pd
import random
import math

def is_prime(query_number):
    for i in range(2, query_number):
        if query_number % i == 0:
            return False
    return True

def prime_range(lower, upper):
    res = []
    for i in range(lower, upper):
        if is_prime(i):
            res.append(i)
    return res

def prime_range_one_liner(lower, upper):
    return [i for i in range(lower, upper) if is_prime(i)]

cpr_regexp = re.compile(r"([0-2]\d|3[01])(0\d|1[0-9])([12]\d{1})(-?)\d{4}")

def cpr_century(cpr_number_str):
    assert(cpr_regexp.match(cpr_number_str))
    iiii = 0
    yy = int(cpr_number_str[2:4])
    if (re.match((r"([0-2]\d|3[01])(0\d|1[0-9])([12]\d{1})\d{4}"), cpr_number_str)):
        iiii = int(cpr_number_str[6:10])
    else:
        iiii = int(cpr_number_str[7:11])
    if (1 <= iiii <= 3999):
        if (0 <= yy <= 99):
            return 1900
    elif (4000 <= iiii <= 4999):
        if (0 <= yy <= 36):
            return 2000
        elif (37 <= yy <= 99):
            return 1900
    elif (5000 <= iiii <= 8999):
        if (0 <= yy <= 57):
            return 2000
        elif (58 <= yy <= 99):
            return 1800
    elif (9000 <= iiii <= 9999):
        if (0 <= yy <= 36):
            return 2000
        elif (37 <= yy <= 99):
            return 1900
    return 0

def calc_column_averages(data_list_of_lists):
    res = []
    for j in range(len(data_list_of_lists[0])):
        temp = 0
        for i in range(len(data_list_of_lists)):
            temp += data_list_of_lists[i][j]
        temp /= len(data_list_of_lists)
        res.append(temp)
    return res

def transpose_list_of_lists(data_list_of_lists):
    res = [[0 for j in range(len(data_list_of_lists))] for i in range(len(data_list_of_lists[0]))]
    for i in range(len(data_list_of_lists)):
        for j in range(len(data_list_of_lists[0])):
            res[j][i] = data_list_of_lists[i][j]
    return res

def calc_column_averages_pandas(anomaly_df):
    res = pd.Series(dtype=float)
    set = 0
    for (columnName, columnData) in anomaly_df.items():
        avg = 0
        for (year, data) in columnData.items():
            if (not math.isnan(data)):
                avg += data
        avg /= len(columnData)
        tmp = pd.Series(avg, name=columnName)
        if (set == 0):
            res = tmp
            set = 1
        else:
            res = pd.merge(res, tmp, right_index=True, left_index=True)
    return res

def get_positiv_anomalies(anomaly_df):
    return anomaly_df.drop(anomaly_df[anomaly_df["Annual Anomaly"] < 0].index)

def remove_uncertain_anomalies(anomaly_df):
    return anomaly_df.drop(anomaly_df[abs(anomaly_df["Annual Anomaly"]) * 0.1 < anomaly_df["Annual Unc."]].index)

def set_uncertain_anomalies_to_nan(anomaly_df):
    res = anomaly_df
    res.loc[abs(anomaly_df["Annual Anomaly"]) * 0.1 < 0.3, ["Annual Unc."]] = float("nan")
    return res

class Coin:
    def __init__(self, tails_probability=0.5):
        self.tails_probability = tails_probability
    
    def toss(self):
        tmp = random.random()
        if tmp < self.tails_probability:
            return "TAILS"
        else:
            return "HEADS"
    
    def toss_multiple(self, n_tosses):
        res = {"TAILS": 0, "HEADS": 0}
        for i in range(n_tosses):
            if self.toss() == "TAILS":
                res["TAILS"] += 1
            else:
                res["HEADS"] += 1
        return res
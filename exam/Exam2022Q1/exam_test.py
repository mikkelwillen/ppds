import exam
import random
import pandas as pd

check_prime_1 = exam.is_prime(10)
check_prime_2 = exam.is_prime(11)
primes1 = exam.prime_range(0, 41)
primes2 = exam.prime_range_one_liner(0, 41)
print("cpr_reg", exam.cpr_regexp.match("123456-7890"))
century = exam.cpr_century("111111-1118")

data = [[random.random() for j in range(2)] for i in range(20)]

column_averages = exam.calc_column_averages(data)

data_transposed = exam.transpose_list_of_lists(data)

anomaly_df = pd.read_table("Land_and_Ocean_summary.txt", comment="%", delimiter=r"\s+", index_col=0, usecols=range(5), names=["Year", "Annual Anomaly", "Annual Unc.", "Five-year Anomaly", "Five-year Unc."])

column_averages_series = exam.calc_column_averages_pandas(anomaly_df)

get_positiv_anomalies = exam.get_positiv_anomalies(anomaly_df)

anomaly_df_filtered = exam.remove_uncertain_anomalies(anomaly_df)

anomaly_df_w_nans = exam.set_uncertain_anomalies_to_nan(anomaly_df)
print(anomaly_df_w_nans)

coin = exam.Coin()
print(coin.tails_probability)
biased_coin = exam.Coin(0)
for i in range(3):
    print(biased_coin.toss())

toss_statistics = biased_coin.toss_multiple(1000)
print(toss_statistics)
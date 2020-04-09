import pandas as pd
import math

# オープンデータの最新レコードを変数へ格納
def refer(opendata, charactercode):
    df = pd.read_csv(opendata, index_col=0, encoding = charactercode)
    latest = df.tail(1)
    year = str(math.floor(latest.iloc[0]["年"]))
    month = str(math.floor(latest.iloc[0]["月"]))
    day = str(math.floor(latest.iloc[0]["日"]))
    inspections_per_day = str(math.floor(latest.iloc[0]["日検査数"]))
    inspections_total = str(math.floor(latest.iloc[0]["検査累計"]))
    positives_per_day = str(math.floor(latest.iloc[0]["日陽性数"]))
    positives_total = str(math.floor(latest.iloc[0]["陽性累計"]))
    patients_per_day = str(math.floor(latest.iloc[0]["日患者数"]))
    patients_totals = str(math.floor(latest.iloc[0]["患者累計"]))
    mild_per_day = str(math.floor(latest.iloc[0]["日軽症中等症数"]))
    mild_total = str(math.floor(latest.iloc[0]["軽症中等症累計"]))
    serious_injury_per_day = str(math.floor(latest.iloc[0]["日重症数"]))
    serious_injury_total = str(math.floor(latest.iloc[0]["重症累計"]))
    deaths_per_day = str(math.floor(latest.iloc[0]["日死亡数"]))
    deaths_total = str(math.floor(latest.iloc[0]["死亡累計"]))
    finished_treatment_per_day = str(math.floor(latest.iloc[0]["日治療終了数"]))
    finished_treatment_total = str(math.floor(latest.iloc[0]["治療終了累計"]))

    return (year, # 年
            month, # 月
            day, # 日
            inspections_per_day, # 日検査数
            inspections_total, # 検査累計
            positives_per_day, # 日陽性数
            positives_total, # 陽性累計
            patients_per_day, # 日患者数
            patients_totals, # 患者累計
            mild_per_day, # 日軽症中等症数
            mild_total, # 軽症中等症累計
            serious_injury_per_day, # 日重症数
            serious_injury_total, # 重症累計
            deaths_per_day, # 日死亡数
            deaths_total, # 死亡累計
            finished_treatment_per_day, # 日治療終了数
            finished_treatment_total) # 治療終了累計

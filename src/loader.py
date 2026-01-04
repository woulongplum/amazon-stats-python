import pandas as pd

#CSV を読み込んで DataFrame を返す関数
def load_records(path: str):  

    df = pd.read_csv(path, parse_dates=["日付"]) # CSVファイルを読み込み、日付列を日付型に変換
    
    df["個数"] = df["個数"].astype(int) # 個数列が文字列になっているため整数型に変換
    return df

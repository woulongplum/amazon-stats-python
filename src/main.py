from loader import load_records
from analyzer import (
    summarize_by_month,
    summarize_by_weekday,
    add_weekday_column,
    summarize_by_month_and_weekday,
    summarize_by_month_and_weekday_ratio,
)

def main():
    
    # ---------------------------------------------------------
    # ① データ読み込み
    #    - CSVファイルを読み込み、DataFrame を返す
    #    - parse_dates により「日付」列は datetime 型に変換済み
    # ---------------------------------------------------------
    df = load_records("../data/records.csv")
    
    # ---------------------------------------------------------
    # ② 曜日列の追加（前処理）
    #    - datetime 型の日付から曜日を抽出
    #    - 英語 → 日本語へ変換
    #    - 曜日の並び順（月→日）を固定して扱いやすくする
    # ---------------------------------------------------------
    df = add_weekday_column(df)
    
    # ---------------------------------------------------------
    # ③ 月別集計
    #    - 月ごとの個数合計を計算
    #    - DataFrame（「月」「個数」）として返される
    # ---------------------------------------------------------
    month_summary = summarize_by_month(df)
    print("月別集計:")
    print(month_summary)
    
    # ---------------------------------------------------------
    # ④ 曜日別集計
    #    - 曜日ごとの個数合計を計算
    #    - 曜日順（月→日）で並んだ DataFrame を返す
    # ---------------------------------------------------------
    weekday_summary = summarize_by_weekday(df)
    print("\n曜日別集計:")
    print(weekday_summary)

    # ---------------------------------------------------------
    # ⑤ 月 × 曜日クロス集計（絶対数）
    #    - 月 × 曜日の合計値を pivot_table で作成
    #    - 行：月、列：曜日 のクロス集計表
    # ---------------------------------------------------------
    month_and_weekday_summary = summarize_by_month_and_weekday(df)
    print("\n月☓曜日クロス集計:")
    print(month_and_weekday_summary)
    
    # ---------------------------------------------------------
    # ⑥ 月 × 曜日クロス集計（比率）
    #    - 各月の合計に対する曜日ごとの割合（％）を計算
    #    - 行方向（axis=0）に割り算することで「月ごとの比率」を算出
    # ---------------------------------------------------------
    summary_by_month_and_weekday_ratio = summarize_by_month_and_weekday_ratio(df)
    print("\n月☓曜日比率クロス集計:")
    print(summary_by_month_and_weekday_ratio)
    
    
if __name__ == "__main__":
    main()

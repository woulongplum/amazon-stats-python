from loader import load_records
from analyzer import (
    summarize_by_month,
    summarize_by_weekday,
    add_weekday_column,
    summarize_by_month_and_weekday,
    summarize_by_month_and_weekday_ratio,
    add_moving_average,
)

from reporter import (
    plot_month_summary,
    plot_weekday_summary,
    plot_month_weekday_summary,
    plot_moving_average,
    plot_moving_average_30,
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
    
    
    # 月別集計の棒グラフを表示
    plot_month_summary(df)
    
    # ---------------------------------------------------------
    # ④ 曜日別集計
    #    - 曜日ごとの個数合計を計算
    #    - 曜日順（月→日）で並んだ DataFrame を返す
    # ---------------------------------------------------------
    weekday_summary = summarize_by_weekday(df)
    print("\n曜日別集計:")
    print(weekday_summary)

    # 曜日別集計の棒グラフを表示
    plot_weekday_summary(df)

    # ---------------------------------------------------------
    # ⑤ 月 × 曜日クロス集計（絶対数）
    #    - 月 × 曜日の合計値を pivot_table で作成
    #    - 行：月、列：曜日 のクロス集計表
    # ---------------------------------------------------------
    month_and_weekday_summary = summarize_by_month_and_weekday(df)
    print("\n月☓曜日クロス集計:")
    print(month_and_weekday_summary)
    
    # 月 × 曜日クロス集計の積み上げ棒グラフを表示
    plot_month_weekday_summary(df)
    
    # ---------------------------------------------------------
    # ⑥ 月 × 曜日クロス集計（比率）
    #    - 各月の合計に対する曜日ごとの割合（％）を計算
    #    - 行方向（axis=0）に割り算することで「月ごとの比率」を算出
    # ---------------------------------------------------------
    summary_by_month_and_weekday_ratio = summarize_by_month_and_weekday_ratio(df)
    print("\n月☓曜日比率クロス集計:")
    print(summary_by_month_and_weekday_ratio)
    
    # 日別データに7日移動平均列を追加（短期トレンドを滑らかにする）
    df = add_moving_average(df, 7) 
    print(df.head())
    # 7日移動平均の折れ線グラフを表示
    plot_moving_average(df)
    
    # 日別データに30日移動平均列を追加（長期トレンドを滑らかにする）
    df = add_moving_average(df, 30) 
    # 30日移動平均の折れ線グラフを表示
    plot_moving_average_30(df)
if __name__ == "__main__":
    main()

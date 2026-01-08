import pandas as pd

#月別に集計する関数
def summarize_by_month(df): #csvから読み込んだデータフレームを引数に取る
    
    df["月"] = df["日付"].dt.to_period("M") #日付列から月情報を抽出して新しい列「月」を作成.dt.to_period("M") → 月単位に変換する（今回のやつ）例　2025-09-12→ 2025-09
    
    return df.groupby("月")["個数"].sum().reset_index()


weekday_map = {
    "Monday": "月",
    "Tuesday": "火",
    "Wednesday": "水",
    "Thursday": "木",
    "Friday": "金",
    "Saturday": "土",
    "Sunday": "日",
}

weekday_order = ["月", "火", "水", "木", "金", "土", "日"]

#曜日の順番を整える関数
def add_weekday_column(df):
    
    df["曜日"] = df["日付"].dt.day_name().map(weekday_map)
    df["曜日"] = pd.Categorical(df["曜日"], categories=weekday_order, ordered=True)
    return df

#曜日別に集計する関数
def summarize_by_weekday(df):
    
    # df に「曜日」列があるか確認 
    assert "曜日" in df.columns, "曜日列がありません。add_weekday_column(df) を先に呼んでください。"
    
    weekday_grouped = df.groupby("曜日")["個数"].sum().reset_index()
    grouped = weekday_grouped.sort_values("曜日")
    return grouped


# 月 × 曜日クロス集計を作る関数
def summarize_by_month_and_weekday(df):
    
    df["月"] = df["日付"].dt.to_period("M")
    
    pivot = df.pivot_table(
        index="月",
        columns="曜日",
        values="個数",
        aggfunc="sum",
        fill_value=0,
    ) 
    
    pivot = pivot.sort_index()  
    
    return pivot


#月×曜日の比率のクロス集計を作る関数
def summarize_by_month_and_weekday_ratio(df):
    
    df["月"] = df["日付"].dt.to_period("M")

    pivot = df.pivot_table(
        index="月",
        columns="曜日",
        values="個数",
        aggfunc="sum",
        fill_value=0,
    )

    pivot = pivot.sort_index()

    ratio = pivot.div(pivot.sum(axis=1), axis=0) * 100

    ratio = ratio.round(1).astype(str) + "%"

    return ratio

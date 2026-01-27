# グラフ描画用ライブラリ
import matplotlib.pyplot as plt
from analyzer import summarize_by_month, summarize_by_weekday,summarize_by_month_and_weekday

# 日本語フォントを指定（IPAexGothicを使用）
plt.rcParams["font.family"] = "IPAGothic"

#月別の個数を棒グラフで表示する
def plot_month_summary(df):
  
    month_summary = summarize_by_month(df)
    
    plt.figure(figsize=(10, 5)) # グラフのサイズを指定
    plt.bar(month_summary["月"].astype(str), month_summary["個数"], color='skyblue') # 棒グラフを描画
    
    plt.title("月別集計") # グラフのタイトル
    plt.xlabel("月") # x軸のラベル
    plt.ylabel("個数")
    plt.xticks(rotation=45) # x軸の目盛りを45度回転
    plt.yticks(range(0, max(month_summary["個数"]) + 100, 100)) # y軸の目盛りを100刻みに設定
    
    plt.tight_layout() # レイアウトを調整
    plt.savefig("../output/month_summary.png")  # グラフを保存
    plt.close()  # グラフを閉じてメモリを解放


#曜日別の個数を棒グラフで表示する
def plot_weekday_summary(df):
    weekday_summary = summarize_by_weekday(df)

    colors = {
        "月": "#000000",  # 黒
        "火": "#FF0000",  # 赤
        "水": "#00BFFF",  # 水色
        "木": "#228B22",  # 緑
        "金": "#FFA500",  # オレンジ
        "土": "#800080",  # 紫
        "日": "#FF00FF",  # マゼンタ
    }

    weekday_order = ["月", "火", "水", "木", "金", "土", "日"]
    weekday_summary = weekday_summary.set_index("曜日").loc[weekday_order].reset_index()

    plt.figure(figsize=(10, 5))
    plt.bar(
        weekday_summary["曜日"],
        weekday_summary["個数"],
        color=[colors[day] for day in weekday_summary["曜日"]]
    )

    plt.title("曜日別集計")
    plt.xlabel("曜日")
    plt.ylabel("個数")
    plt.xticks(rotation=45)
    plt.yticks(range(0, max(weekday_summary["個数"]) + 100, 100))
    plt.tight_layout()
    plt.savefig("../output/weekday_summary.png")
    plt.close()

    

# 月×曜日のクロス集計を積み上げ棒グラフで表示する
def plot_month_weekday_summary(df):
    pivot_df = summarize_by_month_and_weekday(df)

    weekday_order = ["月", "火", "水", "木", "金", "土", "日"]

    colors = {
        "月": "#000000",  # 黒
        "火": "#FF0000",  # 赤
        "水": "#00BFFF",  # 水色
        "木": "#228B22",  # 緑
        "金": "#FFA500",  # オレンジ
        "土": "#800080",  # 紫
        "日": "#FF00FF",  # マゼンタ
    }

    pivot_df = pivot_df[weekday_order]

    fig, ax = plt.subplots(figsize=(12, 6))
    pivot_df.plot(
        kind="bar",
        stacked=True,
        color=[colors[day] for day in weekday_order],
        ax=ax
    )

    ax.set_title("月×曜日 積み上げ棒グラフ（絶対数）")
    ax.set_xlabel("月")
    ax.set_ylabel("個数")
    
    ax.tick_params(axis='x', rotation=45)

    fig.tight_layout()
    fig.savefig("../output/month_weekday_stacked.png")
    plt.close(fig)

# 7日移動平均の折れ線グラフを表示する関数
def plot_moving_average(df):
     
    fig, ax = plt.subplots(figsize=(12, 6))
     
    ax.plot(df["日付"], df["移動平均7日"],label="7日移動平均", color="#FF4500")
    ax.set_title("7日移動平均（トレンド）") 
    ax.set_xlabel("日付") 
    ax.set_ylabel("個数") 
    ax.tick_params(axis="x", rotation=45) 
    ax.legend()

    
    fig.tight_layout() 
    fig.savefig("../output/moving_average_7days.png") 
    plt.close(fig)

# 30日移動平均の折れ線グラフを表示する関数
def plot_moving_average_30(df):
    
    fig, ax = plt.subplots(figsize=(12, 6)) 
    
    ax.plot(df["日付"], df["移動平均30日"], label="30日移動平均", color="#1E90FF") 
    ax.set_title("30日移動平均（長期トレンド）") 
    ax.set_xlabel("日付") 
    ax.set_ylabel("個数") 
    ax.tick_params(axis="x", rotation=45) 
    ax.legend() 
    
    fig.tight_layout() 
    fig.savefig("../output/moving_average_30days.png") 
    plt.close(fig)

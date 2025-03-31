import streamlit as st
import pandas as pd

st.title("売上分析ダッシュボード")

st.caption("このダッシュボードでは月次データとメニュー別の売り上げ数をインタラクティブに確認できます")

expander1=st.expander("使用しているファイル",icon="☠️")
expander1.write("2022sales_data.xlsx")
expander1.write("2022financial_data.xlsx")
expander1.write("monthly_sales_comment.txt")
expander1.write("sales_kind_comment.txt")
expander1.write("以上のデータは経理部で管理しています")

expander2=st.expander("メニューの中身に関する問い合わせ先",icon="👽")
expander2.write('''
            事業部\n
            TEL: 03-xxxx-xxx0\n
                ''')

expander3=st.expander("各種売上データに関する問い合わせ先",icon="🤖")
expander3.write('''            
            経理部\n
            TEL: 03-xxxx-xxx1
            ''')

expander4=st.expander("財務諸表に関する問い合わせ先",icon="🤡")
expander4.write('''
                経理部および経営企画部\n
                TEL: 03-xxxx-xxx1（経理部）\n
                TEL: 03-xxxx-xxx2（経営企画部）
                ''')

st.subheader("本社所在地：品川シーサイド")

data = {
    'latitude': [35.6097],  # 品川シーサイドの緯度
    'longitude': [139.7400]  # 品川シーサイドの経度
}
df = pd.DataFrame(data)

# 地図を表示
st.map(df)

st.markdown(":red[【注意事項】]")
st.markdown(":red[ここはシステム開発者の教育用ダッシュボードです]")
st.markdown(":red[そのため、使用するデータは全て架空のデータです。]")

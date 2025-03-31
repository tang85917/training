import streamlit as st
import pandas as pd
from PIL import Image

st.title('当社の財務分析方針')
st.markdown(":blue[主に分析に使う財務諸表は以下の3つとします]")

epd1=st.expander('・損益計算書')
epd1.write('損益計算書は、収益から費用を差し引いた「利益」を計算します')
epd1.write('このダッシュボードで、月次の損益試算表を確認することができます')
epd2=st.expander('・貸借対照表')
epd2.write('貸借対照表は「決算日時点の企業の財政状態」を表します')
epd2.write('前年度のものは、別途、経理部にご確認ください')
epd3=st.expander('・キャッシュフロー計算書')
epd3.write('キャッシュフロー計算書は、「資金(お金)の流れ」を把握するための計算書です。')
epd3.write('前年度のものは、別途、経理部にご確認ください')

st.write('「利益金処分計算書」「付属明細表」は必要に応じて経理部にご確認ください')

image=Image.open("./data/financial_statements.png")
st.image(image)

#損益計算書
st.markdown("### 前年度の損益計算書")
pl_data=pd.read_excel("./data/2022financial_data.xlsx",
                    index_col=0)
st.dataframe(pl_data)

pl_data=pl_data.drop('合計',axis=1)
pl_t=pl_data.T
multi=st.multiselect('項目を選んでください',
                    ['売上高','売上原価','売上総利益','販売費・一般管理費計','営業利益'],
                    ['売上高'])
st.line_chart(pl_t[multi])
import streamlit as st
import pandas as pd
import altair as alt

st.title("月次データ")

def show():
    st.write("月次データ")

#ドリンクの月次データ
def drink_monthly_data():
    drink_data=pd.read_excel('../data/2022sales_data.xlsx',
                        sheet_name='drink',index_col=0)
    month_drink=st.selectbox("月を選んでください",drink_data.columns,key='drink')

    st.write(f"### {month_drink}のドリンク販売実績")

    col1,col2=st.columns(2)
    with col1:
        drink=drink_data[[f'{month_drink}']]
        st.dataframe(drink,use_container_width=False)
    with col2:
        drink2=drink.reset_index()
        drink2.columns=['メニュー','数量']
        st.altair_chart(alt.Chart(drink2).mark_bar().encode(
            x=alt.X('メニュー',sort=None),y='数量',color='メニュー'),use_container_width=False)

if st.checkbox('ドリンク'):
    drink_monthly_data()

#肉の月次データ
def meat_monthly_data():
    meat_data=pd.read_excel('../data/2022sales_data.xlsx',
                            sheet_name='meat',index_col=0)
    
    month_meat=st.selectbox("月を選んでください",meat_data.columns,key='meat')
    st.markdown(f"### {month_meat}の肉の販売実績")
    col1,col2=st.columns(2)

    with col1:
        meat=meat_data[[f"{month_meat}"]]
        st.dataframe(meat,use_container_width=False)
    with col2:
        meat2=meat.reset_index()
        meat2.columns=['メニュー','数量']
        st.altair_chart(alt.Chart(meat2).mark_bar().encode(
            x=alt.X("メニュー",sort=None),y="数量",color="メニュー"),use_container_width=False)
    
if st.checkbox('肉'):
    meat_monthly_data()

#サイドメニューの月次データ
def side_monthly_data():
    side_data=pd.read_excel('../data/2022sales_data.xlsx',
                            sheet_name='sidemenu',index_col=0)
    
    month_side=st.selectbox("月を選んでください",side_data.columns,key="side")
    st.markdown(f"### {month_side}のサイドメニュー販売実績")

    col1,col2=st.columns(2)
    with col1:
        side=side_data[[f"{month_side}"]]
        st.dataframe(side,use_container_width=False)

    with col2:
        side2=side.reset_index()
        side2.columns=['メニュー','数量']
        st.altair_chart(alt.Chart(side2).mark_bar().encode(
            x=alt.X('メニュー',sort=None),y='数量',color='メニュー'),use_container_width=False)
        
if st.checkbox('サイドメニュー'):
    side_monthly_data()

#コメント欄
with st.form(key='月次コメント'):
    coment=st.text_input('コメント')
    submit_btn=st.form_submit_button('Submit')

    if submit_btn:
        with open("../data/coment.txt","w") as f:
            f.write(f"{coment}\n")
    
    with open("../data/coment.txt","r",encoding='shift-jis') as f:
        select_coment=f.read()
        st.write(select_coment)
#注意書き
st.markdown(":red[今回は練習用のにデータベースの代わりにtxtファイルを使用しています]")
st.markdown(":red[また今回はコメント登録後の取り消し機能は実装していません]")
st.markdown(":red[txtファイルを編集することは可能です]")
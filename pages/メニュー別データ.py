import streamlit as st
import pandas as pd
import altair as alt

def show():
    st.write("メニュー別データ")

st.title("品別売上")

#ドリンクの品別売上
def drink():
    drink_data=pd.read_excel('../data/2022sales_data.xlsx',
                            sheet_name='drink',index_col=0)
    drink_t=drink_data.T

    st.subheader("ラジオボタンでメニューを選択してください")
    col1,col2,col3=st.columns(3)
    with col1:
        drink_radio=st.radio("メニューを選択してください",drink_t.columns,key="drink_radio")
    with col2:
        drink_col2=drink_t[[drink_radio]]
        st.dataframe(drink_col2,use_container_width=False)
    with col3:
        drink_col3=drink_col2.reset_index()
        drink_col3.columns=['月','数量']
        st.altair_chart(alt.Chart(drink_col3).mark_bar().encode(
            x=alt.X('月',sort=None),y='数量',color='月'),use_container_width=False)

#肉の品別売上
def meat():
    meat_data=pd.read_excel('../data/2022sales_data.xlsx',
                            sheet_name='meat',index_col=0)
    meat_t=meat_data.T

    st.subheader("ラジオボタンでメニューを選択してください")
    col1,col2,col3=st.columns(3)
    with col1:
        meat_radio=st.radio('メニューを選択してください',meat_t.columns,key='meat_radio')
    with col2:
        meat_col2=meat_t[[meat_radio]]
        st.dataframe(meat_col2,use_container_width=False)
    with col3:
        meat_col3=meat_col2.reset_index()
        meat_col3.columns=['月','数量']
        st.altair_chart(alt.Chart(meat_col3).mark_bar().encode(
            x=alt.X('月',sort=None),y='数量',color='月'),use_container_width=False)

#サイドメニューの品別売上
def side():
    side_data=pd.read_excel('../data/2022sales_data.xlsx',
                            sheet_name='sidemenu',index_col=0)
    side_t=side_data.T

    st.subheader("ラジオボタンでメニューを選択してください")
    col1,col2,col3=st.columns(3)
    with col1:
        side_radio=st.radio('メニューを選択してください',side_t.columns,key='side_radio')
    with col2:
        side_col2=side_t[[side_radio]]
        st.dataframe(side_col2,use_container_width=False)
    with col3:
        side_col3=side_col2.reset_index()
        side_col3.columns=['月','数量']
        st.altair_chart(alt.Chart(side_col3).mark_bar().encode(
            x=alt.X('月',sort=None),y='数量',color='月'),use_container_width=False)

#ドリンクのマルチセレクト
def drink_multi():
    drink_data=pd.read_excel('../data/2022sales_data.xlsx',
                            sheet_name='drink',index_col=0)
    drink_t=drink_data.T

    drink_multiselect=st.multiselect('確認したいドリンクのメニューを選んでください（複数選択可）',
                                    drink_t.columns.unique(),placeholder='こちらから選んでください')
    st.write(drink_t[drink_multiselect])

    if not drink_multiselect:
        st.error("どれか一つを選んでください")
    else:
        drink_multidata=drink_t[drink_multiselect]
        drink_line=drink_multidata.reset_index()
        drink_line.columns.values[0]='月'
        st.altair_chart(alt.Chart(drink_line.melt(id_vars=['月'],var_name='メニュー',value_name='数量')).mark_line().encode(
            x=alt.X('月',sort=None),y='数量',color='メニュー'))

#肉のマルチセレクト
def meat_multi():
    meat_data=pd.read_excel('../data/2022sales_data.xlsx',
                            sheet_name='meat',index_col=0)
    meat_t=meat_data.T

    meat_multiselect=st.multiselect('確認したいドリンクのメニューを選んでください（複数選択可）',
                                    meat_t.columns.unique(),placeholder='こちらから選んでください')
    st.write(meat_t[meat_multiselect])

    if not meat_multiselect:
        st.error("どれか一つを選んでください")
    else:
        meat_multidata=meat_t[meat_multiselect]
        meat_line=meat_multidata.reset_index()
        meat_line.columns.values[0]='月'
        st.altair_chart(alt.Chart(meat_line.melt(id_vars=['月'],var_name='メニュー',value_name='数量')).mark_line().encode(
            x=alt.X('月',sort=None),y='数量',color='メニュー'))
        
#サイドメニューのマルチセレクト
def side_multi():
    side_data=pd.read_excel('../data/2022sales_data.xlsx',
                            sheet_name='sidemenu',index_col=0)
    side_t=side_data.T

    side_multiselect=st.multiselect('確認したいドリンクのメニューを選んでください（複数選択可）',
                                    side_t.columns.unique(),placeholder='こちらから選んでください')
    st.write(side_t[side_multiselect])

    if not side_multiselect:
        st.error("どれか一つを選んでください")
    else:
        side_multidata=side_t[side_multiselect]
        side_line=side_multidata.reset_index()
        side_line.columns.values[0]='月'
        st.altair_chart(alt.Chart(side_line.melt(id_vars='月',var_name='メニュー',value_name='数量')).mark_line().encode(
            x=alt.X('月',sort=None),y='数量',color='メニュー'))
        
#ドリンクボタン設定
if st.checkbox('ドリンクの品別売上(棒グラフ)',key='drinkcheck'):
    drink()

if st.checkbox('ドリンクの品別売上(マルチセレクト折れ線グラフ)',key="drinkmulti"):
    drink_multi()

#肉ボタン設定
if st.checkbox('肉の品別売上(棒グラフ)',key='meatcheck'):
    meat()

if st.checkbox('肉の品別売上(マルチセレクト折れ線グラフ)',key='meatmulti'):
    meat_multi()

#サイドメニューのボタン設定
if st.checkbox('サイドメニューの品別売上(棒グラフ)',key='sidecheck'):
    side()

if st.checkbox('サイドメニューの品別売上(マルチセレクト折れ線グラフ)',key='sidemulti'):
    side_multi()

#コメント欄
with st.form(key='メニュー別フォーム'):
    comment=st.text_input("コメントを記入してください")
    submit_btn=st.form_submit_button("submit")

    if submit_btn:
        with open("../data/coment.txt","w") as f:
            f.write(comment)

    with open("../data/coment.txt","r",encoding='shift-jis') as f:
        comment1=f.read()
        comment1

st.markdown(":red[今回は練習用にデータベースの代わりにtxtファイルを使用しています]")
st.markdown(":red[また今回はコメント登録後の取り消し機能も実装していません]")
st.markdown(":red[txtファイルを直接編集することは可能です。]")
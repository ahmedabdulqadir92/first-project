import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("games.csv")

# Title
st.title("NBA Games Analysis")

# Show data
st.subheader("Dataset Preview")
st.write(df.head())

# Histogram
st.subheader("Distribution of Home Points")
fig1 = px.histogram(df, x='PTS_home')
st.plotly_chart(fig1)
st.write("Insight: أغلب القيم تتمركز حول 100 نقطة، وهذا يدل أن هذا هو المعدل الطبيعي لتسجيل النقاط في مباريات NBA.")
# Box Plot
st.subheader("Home vs Away Points Comparison")
fig2 = px.box(df, y=['PTS_home', 'PTS_away'])
st.plotly_chart(fig2)
st.write("Insight: يوضح الرسم أن الفريق صاحب الأرض يسجل نقاط أعلى بشكل بسيط مقارنة بالفريق الضيف، مما يدل على وجود أفضلية بسيطة للعب على أرضه، مع وجود بعض القيم النادرة.")
# Correlation Heatmap
st.subheader("Correlation Heatmap")
corr = df[['PTS_home', 'PTS_away', 'HOME_TEAM_WINS']].corr()
fig3 = px.imshow(corr, text_auto=True)
st.plotly_chart(fig3)
st.write("Insight: يوضح التحليل أن زيادة نقاط الفريق صاحب الأرض تزيد من احتمالية الفوز، بينما زيادة نقاط الفريق الضيف تقلل من فرصة فوز الفريق صاحب الأرض.")
# Scatter Plot
st.subheader("Relationship between Home and Away Points")
fig4 = px.scatter(df, x='PTS_home', y='PTS_away')
st.plotly_chart(fig4)
st.write("Insight: يوضح الرسم وجود علاقة بين نقاط الفريقين، حيث أن المباريات ذات الطابع الهجومي تؤدي إلى تسجيل نقاط عالية لكلا الفريقين.")
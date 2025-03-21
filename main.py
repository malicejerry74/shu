import streamlit as st
from utils import generate_xiaohongshu

# 添加标题
st.header('爆款小红书AI习作助手')
# 添加侧边栏
with st.sidebar:
    openai_api_key = st.text_input('请输入API密钥', type='password')
    st.markdown('[获取API密钥的方式](https://platform.openai.com/docs/overview)')

theme = st.text_input('主题')
submit = st.button('开始写作')

if submit and not openai_api_key:
    st.info('请输入你的API密钥')
    st.stop()
if submit and not theme:
    st.info('请输入主题')
    st.stop()
if submit:
    with st.spinner('ai正在努力中，请稍等'):
        result = generate_xiaohongshu(theme, openai_api_key)
    st.divider()
    left_columns, right_columns = st.columns(2)
    with left_columns:
        st.markdown('小红书标题1')
        st.write(result.titles[0])
        st.markdown('小红书标题2')
        st.write(result.titles[1])
        st.markdown('小红书标题3')
        st.write(result.titles[2])
        st.markdown('小红书标题4')
        st.write(result.titles[3])
    with right_columns:
        st.markdown('小红书的正文')
        st.write(result.content)
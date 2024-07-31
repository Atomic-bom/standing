'''我的主页'''
import streamlit as st
from PIL import Image
import time

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区', '地图', '网站链接', '网络知识小问答'])

def page_1():
    '''我的兴趣推荐'''
    with open('佐橋俊彦 - ツナ覚醒 (阿纲觉醒).mp3', 'rb') as f:
        mymp3 = f.read()
    tab0, tab1, tab2, tab3, tab4 = st.tabs(['首页','电影推荐','游戏推荐','书籍推荐','习题集推荐'])
    with tab0:
        st.audio(mymp3, format='audio/mp3', start_time=0)
        st.image('slogan.png')
    with tab1:
        st.write(':red[作者的电影推荐]')
        st.image('liu.png')
        st.write('-----------------------------')
    with tab2:
        st.write(':yellow[作者的游戏推荐]')
        st.image('wang.png')
        st.write('-----------------------------')
    with tab3:
        st.write(':blue[作者的书籍推荐]')
        st.image('hong.png')
        st.write('-----------------------------')
    with tab4:
        st.write(':green[作者的习题集推荐]')
        st.image('qian.png')
        st.write('-----------------------------')

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    my_open1 = st.toggle('改色1')
    my_open2 = st.toggle('改色2')
    my_open3 = st.toggle('改色3')
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        # tab1,tab2,tab3,tab4= st.tabs(['原色','改色1','改色2','改色3'])
        # with tab1:
        st.image(img)
        if my_open1:
            st.image(img_change(img,0,2,1))
        else:
            st.image(img)
        if my_open2:
            st.image(img_change(img,1,2,0))
        else:
            st.image(img)
        if my_open3:
            st.image(img_change(img,1,0,2))
        else:
            st.image(img)
    
def page_3():
    '''我的智慧词典'''
    st.write(':blue[智能词典]')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space1.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 2):
        time.sleep(0.01)
        roading.progress(i, '正在加载'+str(i)+'%')
    roading.progress(100, '加载完毕！')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word][1])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        # 触发彩蛋
        if word == 'python':
            st.code('''
                # 恭喜你触发彩蛋，这是一行python代码
                print('hello world')''')
        if word == 'snow':
            st.snow()
        if word == 'birthday':
            st.balloons()

def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '刘下蛋':
            with st.chat_message('🍳'):
                st.write(i[1],':',i[2])
        elif i[1] == '痔疮':
            with st.chat_message('💣'):
                st.write(i[1],':',i[2])
        elif i[1] == 'V娲ρ':
            with st.chat_message('ρ'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['刘下蛋', '痔疮','V娲ρ'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
    msg_lst = ['留言1', '留言2', '留言3', '留言4', '留言5', '留言6', '留言7', '留言8']
    begin, end = st.slider('选择显示的留言信息：', 1, len(msg_lst), (1, len(msg_lst)))
    for i in range(begin-1, end):
        st.write(msg_lst[i])

def page_5():
    data = {'latitude': [37.7749, 34.0522, 40.7128],'longitude': [-122.4194, -118.2437, -74.0060],'name': ['San Francisco', 'Los Angeles', 'New York']}
    st.map(data, zoom=4, use_container_width=True)

def page_6():
    go = st.selectbox('你想跳转到那个网页？', ['百度', 'bilibili', '抖音'])
    if go == '百度':
        st.link_button('跳转', 'https://www.baidu.com/')
    elif go == 'bilibili':
        st.link_button('跳转', 'https://www.bilibili.com/')
    elif go == '抖音':
        st.link_button('跳转', 'https://www.douyin.com/')

def page_7():
    st.write('下面哪些小程序可以被嵌入网页中？')
    cb1 = st.checkbox('A.turtle绘图作品')
    cb2 = st.checkbox('B.图片处理工具')
    cb3 = st.checkbox('C.智能词典工具')
    cb4 = st.checkbox('D.pygame小游戏')
    b1 = st.button('第1题答案')
    if b1:
        if cb1 == False and cb2 == True and cb3 == True and cb4 == False:
            st.write('回答正确！')
        else:
            st.write('再想想')

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '地图':
    page_5()
elif page == '网站链接':
    page_6()
elif page == '网络知识小问答':
    page_7()
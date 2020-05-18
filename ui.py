import tkinter as tk
import tkinter.font as tkFont


# 定义窗口
top = tk.Tk()
top.title('小圆练题')
top.resizable(0, 0)    # 不可改变窗口大小

# 定义 & 放置框架
f1 = tk.Frame(top)
f2 = tk.Frame(top)
f3 = tk.Frame(top)
f1.grid(row=1, pady=3)
f2.grid(row=2, pady=3)
f3.grid(row=3, pady=3)

# 定义可变文本
label_1_text = tk.StringVar()   # 用于显示题目
choosen = tk.StringVar()        # 用于获取已选择项


# 定义标签显示题目

label_1 = tk.Label(
    f1,
    textvariable = label_1_text,
    bg = 'yellow',
    anchor = 'nw',
    justify = 'left',
    wraplength = 950,
    font = tkFont.Font(size=20),
    height = 8,
    width = 60,
)



# 定义单选
radio_bt_A = tk.Radiobutton(
    f2,
    text = '',
    anchor = 'w',
    width = 80,
    font = tkFont.Font(size=14),
    variable = choosen,
    value = '',
)
radio_bt_B = tk.Radiobutton(
    f2,
    text = '',
    anchor = 'w',
    width = 80,
    font = tkFont.Font(size=14),
    variable = choosen,
    value = '',
)
radio_bt_C = tk.Radiobutton(
    f2,
    text = '',
    anchor = 'w',
    width = 80,
    font = tkFont.Font(size=14),
    variable = choosen,
    value = '',
)
radio_bt_D = tk.Radiobutton(
    f2,
    text = '',
    anchor = 'w',
    width = 80,
    font = tkFont.Font(size=14),
    variable = choosen,
    value = '',
)
radio_bt_E = tk.Radiobutton(
    f2,
    text = '',
    anchor = 'w',
    width = 80,
    font = tkFont.Font(size=14),
    variable = choosen,
    value = '',
)
radio_bt_A.grid(column=1, sticky='NSWE', padx=2)
radio_bt_B.grid(column=1, sticky='NSWE', padx=2)
radio_bt_C.grid(column=1, sticky='NSWE', padx=2)
radio_bt_D.grid(column=1, sticky='NSWE', padx=2)
radio_bt_E.grid(column=1, sticky='NSWE', padx=2)


# 定义上一题按钮
button_pre = tk.Button(
    f3,
    text = '提交，到上一题',
    width = 15
)

# 定义下一题按钮
button_next = tk.Button(
    f3,
    text = '提交，到下一题',
    width = 15
)

# 定义交卷按钮
button_sub = tk.Button(
    f3,
    text = '现在交卷',
    width = 15
)


if __name__ == "__main__":
    
    label_1_text.set('1.某男，60岁，纤维胃镜检查发现胃窦部有一直径3cm大小边缘高起的溃疡，你认为确诊的方法是')
    options_dict = {'A': '细胞学检查', 'B': '活体组织检查', 'C': 'X线钡餐检查', 'D': '大便化验', 'E': '胃液分析'}
    # 放置组件
    label_1.grid(column=1, row=1, sticky='NSWE', padx=2, pady=2)
    button_pre.grid(row=1, column=1, pady=2)
    button_next.grid(row=1, column=2, padx=40, pady=2)
    button_sub.grid(row=1, column=3, pady=2)

    top.mainloop()
import time
from ui import *

if __name__ == "__main__":

    dict1 = {'A': '甲', 'B': '乙', 'C': '丙', 'D': '丁', 'E': '戊'}
    radio_bt(dict1)

    # 放置组件
    label_1.grid(column=1, row=1, sticky='NSWE', padx=2, pady=2)
    button_pre.grid(row=1, column=1, pady=2)
    button_next.grid(row=1, column=2, padx=30, pady=2)
    button_sub.grid(row=1, column=3, pady=2)

    top.mainloop()
import win32clipboard as wc
import win32con
import time
import logic
import os


def get_text():
    """读取剪贴板"""
    wc.OpenClipboard()
    text = wc.GetClipboardData(win32con.CF_TEXT)
    wc.CloseClipboard()
    return text


def main():
    pre_t = ''
    while 1:
        t = str(get_text().decode('gbk'))
        if pre_t != t:
            pre_t = t
            r = 'none'
            r = logic.search_by_words(0, [t])
            os.system('cls')
            print(r)
        time.sleep(1)


if __name__ == "__main__":
    main()

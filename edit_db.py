# 写入数据库
import sqlite3

conn = sqlite3.connect('bingsheng.db')
c = conn.cursor()
c.execute('CREATE TABLE cases (question text, answer text)')
# c.execute('CREATE TABLE choices (question text, answer text)')

# 读取txt文件
with open('./txts/案例分析.txt', 'r', encoding='utf-8') as f1:
    lines = f1.readlines()
    # 名解
    # qna = [(l.strip().split(':')[0], ':'.join(l.strip().split(':')[1:])) for l in lines]
    # 选择
    # qna = [tuple(l.strip().split('@')) for l in lines]
    # 问答
    # qna = [(lines[i].strip(), lines[i+1].strip()) for i in range(0, len(lines), 2)]
    # 论述
    w = False
    w0 = False
    w1 = False
    qna = []
    cache_list = ['', '']
    for l in lines:
        if w:
            qna.append(tuple(cache_list))
        
        if l.strip() == '':
            w = True
            w0 = False
            w1 = False
        elif l[:2] == '案例':
            w = False
            w0 = True
            w1 = False
            cache_list = ['', '']
        elif l[0] == '答':
            w = False
            w0 = False
            w1 = True
        
        if w0:
            cache_list[0] += l
        if w1:
            cache_list[1] += l
        print()
    qna.append(tuple(cache_list))
    

    print(qna[:5])
    # c.executemany('INSERT INTO phrases VALUES (?, ?)', qna)
    c.executemany('INSERT INTO cases VALUES (?, ?)', qna)
    conn.commit()

# 关闭数据库
conn.close()
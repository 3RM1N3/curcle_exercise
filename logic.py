import sqlite3

conn = sqlite3.connect('bingsheng.db', check_same_thread=False)
c = conn.cursor()

def search_by_words(search_type: int, words: str):
    if words.strip() == '':
        return '什么也没有输入！'

    words_list = words.split(' ')
    table = ['choices', 'phrases', 'qnas', 'cases']
    keywords = ' AND question LIKE '.join(['"%'+w+'%"' for w in words_list])
    statement = 'SELECT * FROM %s WHERE question LIKE ' % table[search_type]
    statement += keywords
    c.execute(statement)
    result = ['：\n\t'.join(i) for i in c.fetchall()]
    end_list = [('%d.%s' %(i+1, result[i])) for i in range(len(result))]
    txt = '\n\n'.join(end_list)
    if txt.strip() == '':
        return '没有查询到该题'
    return txt


if __name__ == '__main__':
    print(search_by_words(3, ['男性']))
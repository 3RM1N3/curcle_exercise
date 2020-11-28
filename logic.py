import sqlite3

conn = sqlite3.connect('bingsheng.db', check_same_thread=False)
c = conn.cursor()

def search_by_words(search_type: int, words_list: list):
    table = {
        0: ['choices', 'question', 'answer'],
        1: ['phrases', 'phrase', 'explanation']
    }
    used_table = table[search_type]
    keywords = ' AND %s LIKE ' % used_table[1]
    keywords = keywords.join(['"%'+w+'%"' for w in words_list])
    statement = 'SELECT * FROM %s WHERE %s LIKE ' % (used_table[0], used_table[1])
    statement += keywords
    c.execute(statement)
    result = c.fetchall()
    result = ['\n\t'.join(i) for i in result[:]]
    txt = '\n\n'.join(result)
    return txt


if __name__ == '__main__':
    print(search_by_words(0, ['心', '细胞', '肥大', '表面', '减少']))
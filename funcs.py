def import_data(path):
    '''通过传入路径导入题库'''
    
    # 打开文件
    with open('path', 'r', encoding='UTF-8') as f:
        lines = f.readlines()

    '''
    定义全部题目嵌套列表，数据结构:
    all_questions = [['题目1', {'A': '选项', 'B': '选项', 'C': '选项', 'D': '选项', 'E': '选项'}, '正确答案'],
                     ['题目2', {'A': '选项', 'B': '选项', 'C': '选项', 'D': '选项', 'E': '选项'}, '正确答案'],
                     ...]
    '''
    all_questions = []
    for l in lines:
        pass



def generate_question_dict():
    '''以选中的题库生成100道题目，储存为字典'''

    pass


if __name__ == "__main__":
    pass

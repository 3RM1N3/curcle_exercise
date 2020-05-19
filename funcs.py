def import_data(path):
    '''通过传入路径导入题库'''
    
    # 打开文件
    with open(path, 'r', encoding='UTF-8') as f:
        lines = f.readlines()

    '''
    定义全部题目嵌套列表，数据结构:
    all_questions = [['题目1', {'A': '选项', 'B': '选项', 'C': '选项', 'D': '选项', 'E': '选项'}, '正确答案'],
                     ['题目2', {'A': '选项', 'B': '选项', 'C': '选项', 'D': '选项', 'E': '选项'}, '正确答案'],
                     ...]
    '''
    all_questions = []
    answer_dict = {}

    for l in lines:
        if l[0] in '123456789':
            all_questions.append([l])
        elif l[0] in 'ABCDE':
            answer_dict[l.split('.')[0]] = l.split('.')[1]
        elif '正确答案' in l:
            all_questions[-1].append(answer_dict)
            all_questions[-1].append(l.split(':')[-1])
            answer_dict = {}
    print('导入完成')

    return all_questions



def generate_question_dict():
    '''以选中的题库生成100道题目，储存为字典'''

    pass


if __name__ == "__main__":
    ques_list = import_data('病理选择15章.txt')
    for i in ques_list:
        print(i)

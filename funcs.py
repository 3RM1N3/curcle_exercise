import gui, global_var


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


def generate_options(options_dict):
    '''生成选项'''

    radio_bt_list = [gui.radio_bt_A, gui.radio_bt_B, gui.radio_bt_C, gui.radio_bt_D, gui.radio_bt_E]
    for key, value in options_dict.items():
        for bt in radio_bt_list:
            if key == bt['value']:
                bt['text'] = key + '.' + value


def generate_question():
    '''以选中的题库生成100道测试题目'''

    pass


def next_question():
    '''下一题按钮绑定函数'''

    if global_var.count < len(global_var.ques_list)-1:
        global_var.count += 1
        gui.label_1['text'] = global_var.ques_list[global_var.count][0]
        generate_options(global_var.ques_list[global_var.count][1])


def pre_question():
    '''上一题按钮绑定函数'''

    if global_var.count > 0:
        global_var.count -= 1
        gui.label_1['text'] = global_var.ques_list[global_var.count][0]
        generate_options(global_var.ques_list[global_var.count][1])


def commit():
    '''交卷按钮绑定函数'''

    pass


if __name__ == "__main__":
    ques_list = import_data('病理选择15章.txt')
    for i in ques_list:
        print(i)

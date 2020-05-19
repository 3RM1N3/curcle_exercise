import gui
import funcs
import global_var


if __name__ == "__main__":
    global_var.count = 0
    global_var.ques_list = funcs.import_data('病理选择15章.txt')
    gui.label_1['text'] = global_var.ques_list[global_var.count][0]
    funcs.generate_options(global_var.ques_list[global_var.count][1])
    gui.top.mainloop()
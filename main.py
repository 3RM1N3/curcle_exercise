import gui, funcs, global_var


if __name__ == "__main__":

    global_var.ques_list = funcs.import_data('病理选择15章.txt')
    funcs.next_question()
    gui.top.mainloop()
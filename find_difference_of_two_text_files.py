def new_vs_old(first_text_path, second_text_path):
    new_text_path = first_text_path
    old_text_path = second_text_path
    newtrue_oldfalse = open('firstTrue_oldFalse.txt', 'w')
    new_txt = open(new_text_path, 'r')
    old_txt = open(old_text_path, 'r')

    for new_line in new_txt:
        line_match = False
        old_txt = open(old_text_path, 'r')
        for old_line in old_txt:
            old_line = old_line.rstrip()
            new_line = new_line.rstrip()
            if new_line == old_line:
                line_match = True
                break
        if line_match is False:
            newtrue_oldfalse.write('\n')
            newtrue_oldfalse.write(new_line)
    new_txt.close()
    old_txt.close()
    newtrue_oldfalse.close()

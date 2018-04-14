
import commands

'''
Could be constructed using regular expressions, but it was simple enough with normal equalities
'''
def parse(line, st = None, first_pass = False):
    line = line.replace(' ', '')
    line = line.replace('\n','')

    #check if there is a comment on the line and remove everythin after it
    if '//' in line:
        line = line[:line.find('//')]
    
    #if string now empty, it was a comment, or empty line
    if line == '':
        return commands.Comment("")

    elif line[0] == '@':
        if first_pass:
            st.increment_current_line()

        return commands.A_Command(line)

    elif line[0] == '(' and line[-1]:
        if first_pass:
            st.input_item(line[1:-1])
        else:
            return commands.Comment("") #We use this as a nop instruction for now...

    else: #everything else has to be a C command

        if first_pass:
            st.increment_current_line()

        return commands.C_Command(line)

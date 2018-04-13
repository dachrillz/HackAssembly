
import commands

'''
Could be constructed using regular expressions, but it was simple enough with normal equalities
'''
def parse(line):
    line = line.replace(' ', '')
    line = line.replace('\n','')

    #check if there is a comment on the line and remove everythin after it
    if '//' in line:
        line = line[:line.find('//')]
    
    #if string now empty, it was a comment, or empty line
    if line == '':
        return commands.Comment("")

    elif line[0] == '@':
        return commands.A_Command(line)


    elif line[0] == '(' and line[-1]:
        return commands.L_Command(line)

    else: #everything else has to be a C command
        return commands.C_Command(line)

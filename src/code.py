
import commands

def code(parsed_object):

    if isinstance(parsed_object, commands.A_Command):      
        temp = parsed_object.get_content()
        temp = bin(int(temp))[2:]
        temp = temp.zfill(16) #pad with zeros
        
        return temp


    elif isinstance(parsed_object, commands.C_Command):
        temp = parsed_object.get_content()

        if temp[2] == '=':

            temp = "111"  + table_of_code[temp[1]] + table_of_destination[temp[0]] + "000" #right now it is not possible to mix = and ,
            return temp

        elif temp[2] == ';':
            temp = "111"  + table_of_code[temp[0]] + "000" + table_of_jump[temp[1]]
            return temp


        raise Exception("C-command was neither = or ; " 
                        "This was the string: " + str(temp))
        


    elif isinstance(parsed_object, commands.L_Command):
        pass


table_of_code = {
    "0"     : "0101010",
    "1"     :  "0111111",
    "-1"    :  "0111010",
    "D"     :  "0001100",
    "A"     :  "0110000",
    "!D"    :  "0001101",
    "!A"    :  "0110001",
    "-D"    :  "0001111",
    "-A"    :  "0110011",
    "D+1"   :  "0011111",
    "A+1"   :  "0110111",
    "D-1"   :  "0001110",
    "A-1"   :  "0110010",
    "D+A"   :  "0000010",
    "D-A"   :  "0010011",
    "A-D"   :  "0000111",
    "D&A"   :  "0000000",
    "D|A"   :  "0010101",
    "M"     :  "1110000",
    "!M"    :  "1110001",
    "-M"    :  "1110011",
    "M+1"   :  "1110111",
    "M-1"   :  "1110010",
    "D+M"   :  "1000010",
    "D-M"   :  "1010011",
    "M-D"   :  "1000111",
    "D&M"   :  "1000000",
    "D|M"   :  "1010101"
}

table_of_destination = {
    ""      :  "000",
    "M"     :  "001",
    "D"     :  "010",
    "MD"    :  "011",
    "A"     :  "100",
    "AM"    :  "101",
    "AD"    :  "110",
    "AMD"   :  "111"
}

table_of_jump = {
    ""      :  "000",
    "JGT"   :  "001",
    "JEQ"   :  "010",
    "JGE"   :  "011",
    "JLT"   :  "100",
    "JNE"   :  "101",
    "JLE"   :  "110",
    "JMP"   :  "111"
}
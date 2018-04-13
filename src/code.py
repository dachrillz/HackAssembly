
import commands

def code(parsed_object):

    if isinstance(parsed_object, commands.A_Command):      
        temp = parsed_object.get_content()
        temp = bin(int(temp))[2:]
        temp = temp.zfill(16) #pad with zeros
        
        return temp


    elif isinstance(parsed_object, commands.C_Command):
        return parsed_object.get_content()


    elif isinstance(parsed_object, commands.L_Command):
        pass
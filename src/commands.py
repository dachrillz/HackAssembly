


class Commands():
    
    def __init__(self, content):
        self.content = content


    def __repr__(self):
        return self.content


    def get_content(self):
        return ""


    

class Comment(Commands):
    pass

class A_Command(Commands):
    def __init__(self, content):
        super(A_Command, self).__init__(content)
        self.symbol = self.content


    def get_content(self):
        return self.symbol[1:]

class C_Command(Commands):
    def __init__(self,content):
        super(C_Command, self).__init__(content)

        if '=' in content:
            self.type = '='
            self.des, self.com = content.split("=")
        else: #if it is not an equal statement it has to be a ; statement
            self.type = ';'
            self.des,self.com = content.split(';')

    def get_content(self):
        return (self.des,self.com,self.type)


    pass

class L_Command(Commands):
    pass


class number:
    '''
    Number input
    '''
    def __init__(self, message):
        self.value = None

        self.__input__(message)

        self.message = message or None

    def __input__(self, message):
        value = int(UI.input(message))

        self.value = value

    def max(self, max):
        while(self.value != None and self.value > max):

            self.__input__(self.message)

class UI:
    '''
    User interface
    '''

    def input(message):
        return input(message)

    def print(message):
        print(message)

    def paper(paper):
        '''
        Print visual sample of paper

        Parameters:
        paper (object): paper object
        '''

        text = '    '

        for i in range(paper.meta.width):
            text += str(i+1)

            for i2 in range(3 - len(str(i+1))):
                text += ' '

        text += "\n"

        row_index = 1

        for row in paper.map:
            text += f"{row_index}"

            for i in range(4 - len(str(row_index))):
                text += ' '

            row_index += 1

            for plot in row:
                if(plot.open == True):

                    if(plot.mine == True):
                        text += "\033[91mX\033[0m"

                    elif(plot.strength != None and plot.strength > 0):
                        text += f"\033[9{plot.strength+1}m{plot.strength}\033[0m"

                    else:
                        if(plot.open == True):
                            text += '/'
                        else:
                            text += '-'

                else:
                    text += ' '

                text += '  '

            text += "\n"

        print(text)
class BrainfuckMachine:
    """Brainfuck Turing machine"""

    def __init__(self, cells = 30000, code = ''):
        if(cells < 1):
            cells = 1 # Force having at least one cell 
        self.tape = [0] * cells
        self.cellPointer = 0
        self.codePointer = 0
        self.setCode(code)
        self.output = ''

    def setCode(self, code):
        """Pass code to the object"""
        self.code = code
        self.codeLength = len(self.code) - 1

    def addOutput(self, content):
        self.output += content
        return

    def getOutput(self):
        return self.output

    def run(self):
        """Execute whole brainfuck code string"""
        self.codePointer = 0
        while self.codePointer < self.codeLength:
            self.doStep()
        return self.output
    
    def doStep(self):
        """Parses current character, executes required command. If not 
        a command, skips the character"""
        c = self.code[self.codePointer]
        if(c == '+'):
            self.changeValue(1)
        elif(c == '-'):
            self.changeValue(-1)
        elif(c == '>'):
            self.movePointer(1)
        elif(c == '<'):
            self.movePointer(-1)
        elif(c == '.'):
            self.printPointer()
        elif(c == ','):
            self.getPointer()
        elif(c in ['[', ']']):
            self.loop()
        self.moveCodePointer(1)
        return 

    def movePointer(self, direction):
        """Moves pointer to the proper direction"""
        self.cellPointer += direction
        return self.cellPointer
    
    def moveCodePointer(self, direction):
        """Moves code pointer to proper direction"""
        self.codePointer += direction
        return self.codePointer

    def changeValue(self, action):
        """Increases or decreases current cell's value"""
        self.tape[self.cellPointer] += action
        return self.tape[self.cellPointer]

    def printPointer(self):
        """Adds current cell to the output"""
        self.addOutput(chr(self.tape[self.cellPointer]))
        return

    def getPointer(self):
        """Gets a single character of keyboard input and stores it as ord value"""
        c = raw_input("Enter a character: ")
        if len(c) <= 0: # Beware of being crashed
            c = ' '
        self.tape[self.cellPointer] = ord(c[0]) #Use only a single character
        return c

    def loop(self):
        """Do a single loop step"""
        if(self.code[self.codePointer] == '['):
            if(self.tape[self.cellPointer] == 0):
                self.codePointer = self.findMatchingBrace()
            elif(self.tape[self.cellPointer] != 0):
                return
        elif(self.code[self.codePointer] == ']'):
            if(self.tape[self.cellPointer] == 0):
                return
            elif(self.tape[self.cellPointer] != 0):
                self.codePointer = self.findMatchingBrace()
        return

    def findMatchingBrace(self):
        """Finds a matching brace on the same level and returns it's position"""
        position = self.codePointer
        level = 0
        if(self.code[position] == ']'):
            direction = -1
            markerTarget = '['
            markerSource = ']'
        else:
            direction = 1
            markerTarget = ']'
            markerSource = '['
        position += direction
        while self.code[position] != markerTarget or level != 0:
            if(position < 0):
                position = 0
                break
            if(self.code[position] == markerSource):
                level += 1
            elif(self.code[position] == markerTarget):
                level -= 1
            position += direction
        return position

if __name__ == "__main__":
    """If used directly, run from command line"""
    import sys
    machine = BrainfuckMachine()
    machine.setCode(sys.argv[1])
    machine.run()

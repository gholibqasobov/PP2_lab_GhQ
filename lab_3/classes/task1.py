class getData:
    name = None


    def getString(self, word):
        self.word = word

    def printString(self):
        print(self.word.upper())


student = getData()
student.getString('Murod')
student.printString()

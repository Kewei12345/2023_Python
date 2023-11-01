class human:

    def __init__(self, dob, nationality):
        self.dob = dob
        self.nationality = nationality
        self.height = 0.0
        self.weight = 0.0

    def printAll(self):
        print(self.dob)
        print(self.nationality)
        print(self.height)
        print(self.weight)
        print(self.stream)
        print(self.preSchool)
        

class student(human):
    
    def __init__(self, dob, nationality, stream, preSchool):
        super().__init__(dob, nationality)
        self.stream = stream
        self.preSchool = preSchool 

kewei = student(dob="01/01/1987",
                nationality="chinese",
                stream="haha",
                preSchool="someRandomSchool")

kewei.printAll()
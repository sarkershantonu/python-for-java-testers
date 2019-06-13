class Person:
    def __init__(self, first,last):
        self.first=first
        self.last=last
    def full_name(self):
        return self.first+' '+self.last
    def formal_name(self,title):
        return title+' '+ self.full_name()
        
person = Person('shantonu','sarker')
print(person.formal_name('Eng'))
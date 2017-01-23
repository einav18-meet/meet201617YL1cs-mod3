class Animal():
    def run(self):
        print('Im running')
    def eat(self):
        print('Im eating')

class Dog(Animal):
    def bark(self):
        print('Waf!')


z=Dog()
z.run()

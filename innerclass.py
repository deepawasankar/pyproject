#inner class
class Human:
    def __init__(self):
        self.name='Sunny'
        self.head=self.Head()
        self.brain=self.Brain()

    def display(self):
        print('Hello {}'.format(self.name))
     
    class Head:
        def talk(self):
            print('Talking...')

    class Brain:
        def think(self):
            print('Thinking...')


h=Human()
h.display()
h.head.talk()
h.brain.think()
 

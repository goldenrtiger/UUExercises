class Fish:
    def __init__(self):
        self.members = ['Inkfish', 'Jellyfish', 'Goldfish']

    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print('\t%s' % member)

import cmath

class City():
    '''
        Basic City class
    '''
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def point(self):
        return (self._x, self._y)

    @property
    def comp(self):
        return complex(self._x, self._y)

    @property
    def polar(self):
        return cmath.polar( self.comp )

import matplotlib.pyplot as plt
class MultiCity():
    '''
        a set of cities
    '''
    def __init__(self, listCity):
        try:
            assert( isinstance(listCity, list) )            
            self._sets = listCity
            self.points = []
            self.polars = []
        except:
            raise ValueError('listCity should be a list')

    @property
    def sets(self):
        return self._sets

    def getInfo(self, opt=[0]):    
        for item in opt:                
            if item == 0:
                self.points = [city.point for city in self._sets]
            elif item == 1:
                self.polar = [city.polar for city in self._sets]

        self.x, self.y = zip( *self.points )
        self.r, self.theta = zip( *self.polar )

    def scatter(self):
        try:
            assert( self.points )
            plt.scatter(self.x, self.y, marker='^', c='green')
        except:
            raise ValueError('self.points should not be empty')

    def scatterShow(self):
        self.scatter()
        plt.show()

import cmath
import math
import pandas as pd
import numpy as np
import operator

from sklearn import neighbors
from .city import *
from scipy.spatial.distance import squareform, cdist
import matplotlib.pyplot as plt

class Calcu():
    '''
        Calculation based on polar coordinates
        input: 
            multiCity: use MultiCity class from city package
    '''
    def __init__(self, multiCity):
        self.polar = []
        self.points = []
        try:
            assert( isinstance(multiCity, MultiCity) )
            self.multiCity = multiCity
        
        except:
            raise ValueError('multiCity should belong to MultiCity')

    def sort(self):
        enumR = enumerate( zip( self.multiCity.r, self.multiCity.points ) )
        enumTheta = enumerate( zip( self.multiCity.theta, self.multiCity.points ) )

        self.sortByR = sorted( enumR, key=operator.itemgetter(1) )
        self.sortByTheta = sorted( enumTheta, key=operator.itemgetter(1) )

        print('sortByR: \n', self.sortByR)
        print('sortByTheta: \n', self.sortByTheta)

    def dropPDByRowName(self, df, row):
        df.drop( labels=row, axis=0, inplace=True )

    '''
        use pandas library as a basic 
        idea: sort data by polar R and theta, seperately
              1. Select the first one (origin) in sortR as a basic
              2. Remove the origin in sortR and sortTheta
              3. compare the following three data in sortR and sortTheta to pick one shortest city. 
              

    '''
    def sortPD(self):
        rThetaPoints = list( zip( self.multiCity.r, self.multiCity.theta, self.multiCity.x, self.multiCity.y ) )
        pData = pd.DataFrame(rThetaPoints)
        pData.columns = ['R', 'Theta', 'PointX', 'PointY']
        self.pdSortR = pData.sort_values(by='R')
        self.pdSortTheta = pData.sort_values(by='Theta')

        pSortR = self.pdSortR.copy()
        pSortTheta = self.pdSortTheta.copy()

        print('pdSortR: \n', self.pdSortR)
        print('pdSortTheta: \n', self.pdSortTheta)

        # self.route = [ pdSortR.iloc[0] ]
        self.route = [ self.pdSortR.index[0] ]
        print('original row:', self.route[0])

        row = self.route[0]

        self.dropPDByRowName( pSortR, row )
        self.dropPDByRowName( pSortTheta, row )

        self.reDist = 0
        self.RDist = 0
        self.ThetaDist = 0

        for idx in range(0, self.pdSortR.shape[0] - 1):
            # base = [ route[0].PointX, route[0].PointY ] * 6
            b = pData.loc[[self.route[idx]]]
            base = np.stack((np.array([b.PointX] * 6), np.array([b.PointY] * 6)), axis=-1).reshape(6,2)
            neighborsX = np.append( pSortR.iloc[0:3, 2].values, pSortTheta.iloc[0:3, 2].values )
            neighborsY = np.append( pSortR.iloc[0:3, 3].values, pSortTheta.iloc[0:3, 3].values )
            neighbors = np.stack((neighborsX, neighborsY), axis=-1)
            dist = cdist(base, neighbors)
            minIdx = np.argmin( dist[0] )
            self.reDist += dist[0][minIdx]
            self.RDist += math.dist( self.pdSortR.iloc[[idx], [2,3]].values.tolist()[0], self.pdSortR.iloc[[idx + 1], [2,3]].values.tolist()[0])
            self.ThetaDist += math.dist( self.pdSortTheta.iloc[[idx], [2,3]].values.tolist()[0], self.pdSortTheta.iloc[[idx + 1], [2,3]].values.tolist()[0])

            row = pSortTheta.index[minIdx] if minIdx > 2 else pSortR.index[minIdx]
            self.dropPDByRowName( pSortR, row )
            self.dropPDByRowName( pSortTheta, row )

            self.route.append( row )

        print('reorder dist:\n', self.reDist)
        print('R dist:\n', self.RDist)
        print('Theta dist:\n', self.ThetaDist)
        self.rePData = pData.reindex(self.route)
        print(self.rePData)

    def getInfo(self, infoSet, opt=[0]):
        info = []
        for item in opt:
            if item == 0:
                info.append( infoSet[0] ) # index
            elif item == 1:
                info.append( infoSet[1][0] ) # polar.R or polar.theta
            elif item == 2:
                info.append( infoSet[1][1] ) # points
            else:
                pass
        return info            
    
    def shortest(self, opt=0):
        if opt == 0:
            plt.plot(self.rePData.loc[:].PointX.values, self.rePData.loc[:].PointY.values, 'bo')
            plt.plot(self.rePData.loc[:].PointX.values, self.rePData.loc[:].PointY.values, color='green', linewidth=2)
        elif opt == 1:
            plt.plot(self.pdSortR.loc[:].PointX.values, self.pdSortR.loc[:].PointY.values, 'bo')
            plt.plot(self.pdSortR.loc[:].PointX.values, self.pdSortR.loc[:].PointY.values, color='green', linewidth=2)
        elif opt == 2:
            plt.plot(self.pdSortTheta.loc[:].PointX.values, self.pdSortTheta.loc[:].PointY.values, 'bo')
            plt.plot(self.pdSortTheta.loc[:].PointX.values, self.pdSortTheta.loc[:].PointY.values, color='green', linewidth=2)
        else:
            pass
    
    def shortestShow(self, opt=0):
        self.shortest(opt)
        plt.savefig(str(opt))
        plt.show()



        
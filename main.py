import TSP
from source import source

multiCity = TSP.MultiCity(source.list())

#-- get points in MultiCity class then plot
multiCity.getInfo(opt=[0,1])
# multiCity.scatterShow()

calcu = TSP.Calcu(multiCity)
calcu.sortPD()
calcu.shortestShow(opt=0)
calcu.shortestShow(opt=1)
calcu.shortestShow(opt=2)





import TSP
import pandas as pd

class source():

    Stockholm = TSP.City(59.329, 18.069)
    Gothenburg = TSP.City(57.707, 11.967)
    Malmo = TSP.City(55.606, 13.001)
    Uppsala = TSP.City(59.859, 17.639)
    Sollentuna = TSP.City(59.428, 17.951)
    Vasteras = TSP.City(59.616, 16.553)
    Orebro = TSP.City(59.274, 15.207)
    Linkoping = TSP.City(58.411, 15.622)
    Helsingborg = TSP.City(56.047, 12.694)
    Jonkoping = TSP.City(57.781, 14.156)

    @staticmethod
    def list():
        return [source.Stockholm, source.Gothenburg, source.Malmo, source.Uppsala,
        source.Sollentuna, source.Vasteras, source.Orebro, source.Linkoping,
        source.Helsingborg, source.Jonkoping]

    @staticmethod
    def pd():
        return pd.DataFrame({
            'Stockholm':[(59.329, 18.069)],
            'Gothenburg':[(57.707, 11.967)],
            'Malmo':[(55.606, 13.001)],
            'Uppsala':[(59.859, 17.639)],
            'Sollentuna':[(59.428, 17.951)],
            'Vasteras':[(59.616, 16.553)],
            'Orebro':[(59.274, 15.207)],
            'Linkoping':[(58.411, 15.622)],
            'Helsingborg':[(56.047, 12.694)],
            'Jonkoping':[(57.781, 14.156)],
        })




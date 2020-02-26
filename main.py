from geoetl import GeoEtl
from persister import Persister

if __name__ == "__main__":
    getl = GeoEtl()
    getl.obtainData()
    getl.getDataKpis()

    persist = Persister(getl.dataframe)
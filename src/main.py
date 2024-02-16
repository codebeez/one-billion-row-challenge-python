import time

import duckdb
import pandas as pd


def the_lazy_way():
    # 144 sec :(
    start_time = time.time()
    df = pd.read_csv(
        "data/measurements.txt", delimiter=";", header=None, names=["station", "measurement"]
    )
    df = duckdb.query(
        "SELECT station, ROUND(MIN(measurement),1) as _min, ROUND(AVG(measurement),1) as _avg, ROUND(MAX(measurement),1) as _max, FROM df GROUP BY station"
    )
    print(df.to_dict(orient="records"))
    end = time.time() - start_time
    print(f"duration: {end} sec")


if __name__ == "__main__":
    the_lazy_way()

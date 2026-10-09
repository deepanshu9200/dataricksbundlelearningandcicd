import dlt

@dlt.table()
def get_data():
  return spark.range(1000)
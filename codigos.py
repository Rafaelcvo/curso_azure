%python

clientes = spark.read.format('csv').options(header='true', inferSchema='true', delimiter=';').load('/FileStore/tables/carga/clientes_cartao.csv')

display(clientes)
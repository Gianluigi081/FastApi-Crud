from sqlalchemy import create_engine, MetaData

#Crear conexión
engine = create_engine("mysql+pymysql://root:root@localhost:3306/task")

meta_data = MetaData()
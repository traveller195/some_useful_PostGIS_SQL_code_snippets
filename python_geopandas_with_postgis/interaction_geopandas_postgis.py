# dev environment
# is running in July 2022 
# is running in a docker container, having access to a mdillon/postgis docker container containing the database
# docker is running in Ubuntu 20.4 LTS
# python 3.10.4 - 64bit


#import packages
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon, LineString

#Spatial Join
from geopandas.tools import sjoin

# to include datetime / timestamp into output file name
# or on logfile / console
import time
from time import gmtime, strftime

import numpy as np

from sqlalchemy import create_engine

# !!! for .to_postgis() - Note: you will need psycopg2-binary, sqlalchemy2, and geoalchemy2 installed. !!!
# pip3 install GeoAlchemy
# pip3 install GeoAlchemy2


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++ database connection +++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

db_connection_url = "postgresql+psycopg2://postgres:postgres@db_name:5432/postgres"

con = create_engine(db_connection_url)  

print(str(strftime("%Y_%m_%d-%H_%M_%S", gmtime())) + '  create database connection')  


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++ load data from PostGIS DB +++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


data_study_area = gpd.read_postgis('SELECT * FROM schema_name.table.name;', con, geom_col='geometry')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++ load data to PostGIS DB +++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

data_study_area.to_postgis('new_table_name', con, schema='target_schema_name', if_exists='fail', index=False, index_label=None, chunksize=2000, dtype=None)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++ execute in database  ++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

con.execute("CREATE TABLE schema_name.table_name AS SELECT * FROM schema_name.table_name_2 LIMIT 10;")




# Parameters for .to_postgis()
#
#    namestr
#
#        Name of the target table.
#    consqlalchemy.engine.Connection or sqlalchemy.engine.Engine
#
#        Active connection to the PostGIS database.
#    if_exists{???fail???, ???replace???, ???append???}, default ???fail???
#
#        How to behave if the table already exists:
#
#            fail: Raise a ValueError.
#
#           replace: Drop the table before inserting new values.
#
#            append: Insert new values to the existing table.
#
#    schemastring, optional
#
#        Specify the schema. If None, use default schema: ???public???.
#    indexbool, default False
#
#        Write DataFrame index as a column. Uses index_label as the column name in the table.
#    index_labelstring or sequence, default None
#
#        Column label for index column(s). If None is given (default) and index is True, then the index names are used.
#    chunksizeint, optional
#
#        Rows will be written in batches of this size at a time. By default, all rows will be written at once.
#    dtypedict of column name to SQL type, default None
#
#        Specifying the datatype for columns. The keys should be the column names and the values should be the SQLAlchemy types.



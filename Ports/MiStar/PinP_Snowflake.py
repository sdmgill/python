from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import snowflake.connector
import pandas as pd
import geopandas as gp
import s3fs
import os
import snowflake_config
import time

s3 = s3fs.S3FileSystem(anon=False)

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

conn = snowflake.connector.connect(
    user= snowflake_config.user,
    password= snowflake_config.password,
    account=  snowflake_config.account,
    warehouse=  snowflake_config.warehouse,
    database= snowflake_config.database,
    schema= snowflake_config.schema,
    autocommit=True)

md_df = pd.read_sql_query('''SELECT POSITION1X,POSITION1Y,POSITION2X,POSITION2Y,POSITION3X,POSITION3Y,\
                    ROUND((POSITION1X - POSITION2X + POSITION3X), 2) AS POSITION4X,\
                    ROUND((POSITION1Y - POSITION2Y + POSITION3Y), 2) AS POSITION4Y,\
                    CASE WHEN LOT LIKE '%GR%' THEN SUBSTRING(lot, 1, 3)\
                            WHEN LOT LIKE '%RX%' THEN 'RX'\
                            WHEN LOT LIKE '%RF%' THEN 'RF'\
                            WHEN LOT LIKE '%RZ%' THEN 'RZ'\
                            ELSE LOT\
                    END AS LOT\
            from MAPDATA''', conn)

md_gdf=gp.GeoDataFrame(md_df)
geoms =[]
for index, row in md_gdf.iterrows():
    geom=Polygon([(row.POSITION1X,row.POSITION1Y),(row.POSITION2X,row.POSITION2Y),(row.POSITION3X,row.POSITION3Y),(row.POSITION4X,row.POSITION4Y)])
    geoms.append(geom)

md_gdf['geometry'] = geoms

md_gdf = md_gdf[['LOT','geometry']]

# print(md_gdf.head())


# pos_df = pd.read_sql_query('''SELECT TOP 1000 * FROM Position''',conn)
pos_df = pd.read_sql_query('''SELECT ROVERTIMESTAMP, MJID, LOCALX, LOCALY FROM POSITION WHERE LOT IS NULL AND LOCALX > 10 AND LOCALY > 10 ORDER BY ROVERTIMESTAMP DESC LIMIT 5000000''',conn)
pos_df['COMPUTEDLOCALX'] = pos_df['LOCALX'] / 10
pos_df['COMPUTEDLOCALY'] = pos_df['LOCALY'] / 10

pos_gdf = gp.GeoDataFrame(pos_df, geometry = gp.points_from_xy(pos_df.COMPUTEDLOCALX, pos_df.COMPUTEDLOCALY))

# print(pos_gdf.head())

pos_lot = gp.sjoin(pos_gdf,md_gdf, how="inner", op="intersects")

cts = time.strftime("%Y%m%d%H%M%S")

# print(pos_lot)
with s3.open('pa-snowflake-stages/python/mistar/position/' + str(cts) + '_position_lot.csv','w') as f:
    pos_lot.to_csv(f)

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import pymssql
import pandas as pd
import geopandas as gp

conn = pymssql.connect(
    host=r'10.50.10.124',
    user=r'sql_streamsets_p',
    password='1QTWHcdmd2Rr3yYMcI9f',
    database='stg_mistar_prd'
)

md_df = pd.read_sql_query('''SELECT position1x,position1y,position2x,position2y,position3x,position3y,\
                    ROUND((position1x - position2x + position3x), 2) AS position4x,\
                    ROUND((position1y - position2y + position3y), 2) AS position4y,\
                    CASE WHEN lot LIKE '%GR%' THEN SUBSTRING(lot, 1, 3)\
                            WHEN lot LIKE '%RX%' THEN 'RX'\
                            WHEN lot LIKE '%RF%' THEN 'RF'\
                            WHEN lot LIKE '%RZ%' THEN 'RZ'\
                            ELSE lot\
                    END AS lot\
            from MapData''', conn)

md_gdf=gp.GeoDataFrame(md_df)
geoms =[]
for index, row in md_gdf.iterrows():
    geom=Polygon([(row.position1x,row.position1y),(row.position2x,row.position2y),(row.position3x,row.position3y),(row.position4x,row.position4y)])
    geoms.append(geom)

md_gdf['geometry'] = geoms

md_gdf = md_gdf[['lot','geometry']]

# print(md_gdf.head())


# pos_df = pd.read_sql_query('''SELECT TOP 1000 * FROM Position''',conn)
pos_df = pd.read_sql_query('''SELECT TOP 1000 RoverTimestamp, mjid, LocalX, LocalY FROM Position''',conn)
pos_df['computedLocalX'] = pos_df['LocalX'] / 10
pos_df['computedLocalY'] = pos_df['LocalY'] / 10

pos_gdf = gp.GeoDataFrame(pos_df, geometry = gp.points_from_xy(pos_df.computedLocalX, pos_df.computedLocalY))

# print(pos_gdf.head())

pos_lot = gp.sjoin(pos_gdf,md_gdf, how="inner", op="intersects")

print(pos_lot)

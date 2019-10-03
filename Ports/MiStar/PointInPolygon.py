from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import pymssql

# AGR01 -- No
#point = Point(1536.5, 2118.6)
#polygon = Polygon([(1593.0970, 2085.8690), (1593.0980, 1966.8690), (1670.7410, 1966.8697), (1670.7420, 2085.8690)])
#print(polygon.contains(point))

#AGR
point = Point(1826.7, 2036.7)
polygon = Polygon([(1616.5630,2073.4210), (2013.9040,2072.3730), (2014.3220,1996.8830), (1616.9130,1983.5310)])
print(polygon.contains(point))

# C -- Yes
#point = Point(2863.3, 1278.5)
#polygon = Polygon([(2447.4240,1215.4070), (2446.2060,1502.4044), (2886.2980,1504.2721), (2884.0040,1217.4030)])
#print(polygon.contains(point))
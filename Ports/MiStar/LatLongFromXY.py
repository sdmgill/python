import math as ma


def LatLongFromXY(LocalXf,LocalYf):
    LocalXf = 58322
    LocalYf = 12965

    LocalZdf = 0
    dOriginLatitude = 40.689072222
    dOriginLongitude = -74.164294444
    dRotationalAngle = -39.1406
    height = -12.052
    A = 6378137.0
    B = 6356752.3143

    LocalX = (LocalXf / 10) * 0.3048
    LocalY = (LocalYf / 10) * 0.3048
    m_dtor = ma.pi / 180.0
    m_RotAngRad = dRotationalAngle * m_dtor
    dVec_llX = LocalX * ma.cos(m_RotAngRad) - LocalY * ma.sin(m_RotAngRad)
    dVec_llY = LocalX * ma.sin(m_RotAngRad) + LocalY * ma.cos(m_RotAngRad)
    dVec_llZ = 0
    cphi = ma.cos(dOriginLatitude * m_dtor)
    sphi = ma.sin(dOriginLatitude * m_dtor)
    clam = ma.cos(dOriginLongitude * m_dtor)
    slam = ma.sin(dOriginLongitude * m_dtor)

    etn00 = -slam
    etn01 = clam
    etn02 = 0.0

    etn10 = -(sphi * clam)
    etn11 = -(sphi * slam)
    etn12 = cphi

    etn20 = cphi * clam
    etn21 = cphi * slam
    etn22 = sphi

    EarthCenter_X = etn00 * dVec_llX + etn10 * dVec_llY + etn20 * dVec_llZ
    EarthCenter_Y = etn01 * dVec_llX + etn11 * dVec_llY + etn21 * dVec_llZ
    EarthCenter_Z = etn02 * dVec_llX + etn12 * dVec_llY + etn22 * dVec_llZ

    e2 = (A * A - B * B) / (A * A)
    n = A / ma.sqrt(1 - e2 * sphi * sphi)

    m_OriginEcefX = (n + height) * cphi * ma.cos(dOriginLongitude * m_dtor)
    m_OriginEcefY = (n + height) * cphi * ma.sin(dOriginLongitude * m_dtor)
    m_OriginEcefZ = (n * (1 - e2) + height) * sphi

    EarthCenterX = EarthCenter_X + m_OriginEcefX
    EarthCenterY = EarthCenter_Y + m_OriginEcefY
    EarthCenterZ = EarthCenter_Z + m_OriginEcefZ

    a2 = A * A
    b2 = B * B

    p = ma.sqrt(EarthCenterX * EarthCenterX + EarthCenterY * EarthCenterY)
    t1 = p * (1.0 - e2)

    OutputLamda = ma.atan2(EarthCenterY, EarthCenterX)
    OutputPhi = ma.atan2(EarthCenterZ, t1 * p)

    #breakme = 0
    while True:
        cp = ma.cos(OutputPhi)
        sp = ma.sin(OutputPhi)
        r = A / ma.sqrt(1.0 - e2 * sp * sp)
        OutputHeight = p / cp -r
        t_1 = 1.0 - e2 * r / (r + OutputHeight)
        phi_temp = ma.atan2(EarthCenterZ, (t_1 * p))
        if(abs(OutputPhi - phi_temp) < 1.0e-10):
            break

        OutputPhi = phi_temp

    pointy = OutputLamda * 180 / ma.pi
    pointx = OutputPhi * 180 / ma.pi
    Latitude = round(pointx,10)
    PI = ma.pi

    print(pointx,pointy)
program  Solar_elevation_angle
    use Solar_hour_angle
    use Declination_angle
    implicit none
    integer:: mon, day, hrs, min, del_TZ
    real(8):: dec_angle, sol_hur_angle, Lon, Lat, temp, SEA
    real, parameter                   :: pih = 3.1415926536
    mon = 12
    day = 31
    hrs = 10
    min = 32
    Lon = 114.062996
    Lat = 22.542883
    del_TZ = 8

    call cal_angle(mon, day, dec_angle)
    call solarhour_angle(mon, day, hrs, min, del_TZ, Lon, sol_hur_angle)

    temp = sin(Lat * pih / 180.0) * sin(dec_angle * pih / 180.0)
    temp = temp + cos(Lat * pih / 180.0) * cos(dec_angle * pih / 180.0) * cos(sol_hur_angle * pih / 180.0)

    SEA = ASIN(temp) * 180.0  / pih
    print*, 'the SEA is ', SEA
end program  Solar_elevation_angle
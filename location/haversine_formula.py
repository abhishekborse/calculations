from math import sin, cos, pi, atan2, sqrt


def haversine_formula(point1_details, point2_details):
    earth_radius = 6371

    point1_lat: float = float(point1_details.get('lat'))
    point1_long: float = float(point1_details.get('long'))

    point2_lat: float = float(point2_details.get('long'))
    point2_long: float = float(point2_details.get('lat'))

    lat_diff = point2_lat - point1_lat
    lat_diff = lat_diff * pi / 180
    long_diff = point2_long - point1_long
    long_diff = long_diff * pi / 180

    area = sin(lat_diff / 2) * sin(lat_diff / 2) + cos(point1_lat * pi / 180) * cos(point2_lat * pi / 180) * sin(
        long_diff / 2) * sin(long_diff / 2)
    c = 2 * atan2(sqrt(area), sqrt(1 - area))
    '''distance in km'''
    distance = c * earth_radius
    return distance


if __name__ == '__main__':
    point1 = {'lat': '', 'long': ''}
    point2 = {'lat': '', 'long': ''}
    haversine_formula(point1_details=point1, point2_details=point2)
from math import sin, cos, pi, atan2, sqrt
import logging
logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


def haversine_formula(point1_details, point2_details):
    earth_radius = 6371

    point1_lat: float = float(point1_details.get('lat'))
    point1_long: float = float(point1_details.get('long'))

    point2_lat: float = float(point2_details.get('lat'))
    point2_long: float = float(point2_details.get('long'))

    lat_diff = point2_lat - point1_lat
    lat_diff = lat_diff * pi / 180
    long_diff = point2_long - point1_long
    long_diff = long_diff * pi / 180

    area = sin(lat_diff / 2) * sin(lat_diff / 2) + cos(point1_lat * pi / 180) * cos(point2_lat * pi / 180) * sin(
        long_diff / 2) * sin(long_diff / 2)
    c = 2 * atan2(sqrt(area), sqrt(1 - area))
    '''distance in km'''
    return round(c * earth_radius, 3)


if __name__ == '__main__':
    point1 = {'lat': 21.146633, 'long': 79.088860}
    point2 = {'lat': 18.516726, 'long': 73.856255}
    distance = haversine_formula(point1_details=point1, point2_details=point2)
    logger.info('distance is {} km'.format(str(distance)))

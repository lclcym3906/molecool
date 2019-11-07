
import numpy as np

def calculate_distance(rA, rB):
    # This function calculates the distance between two points given as numpy arrays.
    distance_vec=(rA-rB)
    dist=np.linalg.norm(distance_vec)
    return dist


def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    dist_AB = rB - rA
    dist_BC = rB - rC
    theta=np.arccos(np.dot(dist_AB, dist_BC)/(np.linalg.norm(dist_AB)*np.linalg.norm(dist_BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta

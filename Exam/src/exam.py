#!/usr/bin/python3

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.externals import six
import numpy as np
import re


def toCoordinateList(coordinateLine):
    """
        Given a line of counties.dat containing coordinates as
        as string, this is converted to a pyhon array of tuples
        first split by the  ' ' char, then by the ';' char 

        Args:
            coordinateLine: String containing country coordinates

        Returns: Array of the form [(x1,y2),...,(xn,yn)], where xn and yn 
            are floats
    """


    output = []
    line = coordinateLine.split(' ')
    for coordinate in line:
        x, y = coordinate.split(';')
        output.append((float(x), float(y)))
    return output


def read_country_data(fname):
    """
        Reads fname line by line, using re_num to determine if the line is a
        name of a coordinate list. In case of a name, a entry with that 
        name as key is added to the output dictionary, with the initial value
        being an empty python array. In case of a coorindate line, toCoordinateList
        is used to convert it to a proper coorindate python array, which is then 
        appended to the associated country dictionary value.
        
        Args:
            fname: String describing path to file to be read

        Return; Dictionary, with country as key, and array as value, of form
            [[(x1, y_1),...,(xn,yn)],...,[(z1, q1),..., (zn,qn)]] where all
            touple content are floats
    """


    re_num = "[-0-9;. ]"
    output = {}


    with open(fname, "r") as f:
        country = None
        for line in f:
            # Remove Newline Characters
            line = line.strip('\n ')


            # Check for blank line, skip if it is
            if line == '':
                continue


            # Check if line is country or coordinate
            if re.match(re_num, line) == None:
                country = line
                output[country] = []
            else:
                coordinates = toCoordinateList(line)
                output[country].append(coordinates)

    return output


def find_center(coordinates):
    """
        Given a list of country shapes, in the form of x,y lists, 
        numpy is used to first concatenate all the sublists of the list, to get
        a list of form [(x1,y2),...,(xn,yn)], where xn and yn are floats.
        numpy is then used to get the mean of each column

        Args: 
            coordinates: list of form [[(x1, y_1),...,(xn,yn)],...,[(z1, q1),..., (zn,qn)]] 
            where all touple content are floats

        Returns: Touple of form (mean_x, mean_y), describing the mean of each
            column of the input

    """


    # Merge the lists inside coordinates, in case there are several
    coordinates = np.concatenate(coordinates)

    # Get the mean along the first axis, and convert to tuple
    return tuple(np.mean(coordinates, 0))

def draw_globe_map(view_center):
    """Draw a map in using an orthographic projection

    Args:
        view_center: A `tuple` with the latitude, longitude specifying
        where the map should be centered.

    Returns:
        A `Basemap` object.
    """

    # Set up orthographic map projection. Use low resolution coastlines.
    globe_map = Basemap(projection='ortho', resolution='l',
                        lat_0=view_center[0],
                        lon_0=view_center[1])
    # draw lat/lon grid lines every 30 degrees.
    globe_map.drawmeridians(np.arange(0,360,30), color='0.8')
    globe_map.drawparallels(np.arange(-90,90,30), color='0.8')

    # TODO: Draw coastlines, country outlines and colour the continents

    return globe_map



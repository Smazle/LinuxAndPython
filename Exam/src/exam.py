import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import re

# ===== Assignment 1 Function ===== #


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


# ===== Assignment 2 Functions ===== #

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

    # https://matplotlib.org/basemap/users/examples.html
    globe_map.drawcoastlines(linewidth=0.25, color="lightgray")
    globe_map.drawcountries(linewidth=0.25, color="lightgray")
    globe_map.fillcontinents(color="lightgray")

    return globe_map


def highlight_region(globe_map, coordinate_lists):
    """Add polygons in Basemap, based on provided
       lat,lon coordinates (in degrees)

    Args:
        globe_map: A `Basemap object`.
        coordinate_lists: A `list` of `list`s of
            coordinate pairs.
    """
    # Project lat,lon coordinates into x,y coordinates
    mapped_coordinates = []
    for coord_list in coordinate_lists:
        coord_array = np.array(coord_list)
        mapped_coordinates.append(
            np.stack(globe_map(coord_array[:, 1], coord_array[:, 0])).T)

    # Add polygons for each coordinate list
    patches = []
    for coord_list in mapped_coordinates:
        patches.append(
            matplotlib.patches.Polygon(np.array(coord_list), closed=True))
        plt.gca().add_patch(patches[-1])

    # Clip polygons to fit within polar plot
    # This call differs between versions of Basemap.
    try:
        globe_map._clipcircle(plt.gca(), patches)
    except AttributeError:
        globe_map._cliplimb(plt.gca(), patches)

def map_transition(center1, center2, highlight_coords, steps=10):
    """Create transition from one map center to another.
    
    Args:
        center1: `tuple` containing latitude, longitude coordinates. This
            is the starting point for the transition.
        center2: `tuple` containing latitude, longitude coordinates. This
            is the end point for the transition.
        highlight_coords: `list` of `list` of coordinate pairs, specifying
            a region to be highlighted.
        steps: `int` specifying how many steps should be taken.
    """

    # Convert start and end latitude,longitude into a single array
    center = np.array([center1, center2])

    # Calculate total distance in both latitude and longitude
    distance = center[1, :] - center[0, :]

    # Initialize to center1
    current_center = center[0, :]

    for i in range(steps):
        
        print("Transition step %d" % i)

        # Note: Currently i assume the first image, 
        # is the one where i have stepped one time. 
        # Thus the first plotted image, isn't on center 1. This could
        # be changed, by incrementing after plotting, and adding a step.
        # Thus the first image would be center1, followed by 10 step images.

        # Update current_center with appropriate distance
        for q in range(len(center)):
            current_center[q] += (distance[q]/steps)

        # Create new figure (to get rid of any old plots)
        plt.figure()

        # Draw new map and highlight region
        step_map = draw_globe_map(current_center)
        step_map_highlighted = highlight_region(step_map, highlight_coords)

        # Save plot to file
        plt.savefig("globe_map_%03d.png" % i) 

# ===== Assignment 3 Functions ===== #


def read_missile_data(data_filename, selected_columns):
    """
        Follows the steps described in task 3.1.
        Looks up data from data_filename, and filters out
        unwanted columns using the selected_columns list.
        
        Args:
            data_filename: String describing the path to file being
                read
            selected_columns: List of strings, describing the 
                columns names wanted in the final output
        Returns:
            A list of dictionaries, one dictionary per line in
            the data_filename file. The dictionaries contain
            one key per selected_columns, where the value
            is the one associated with the specific column
    """
    
    # Initialize variables
    readData = []
    missile_data = []
    column_names = []

    # a and b - Open and add to list
    with open(data_filename, "r") as f:
        for line in f:
            readData.append(line.strip('\n '))


    # c - Get column names, from the first line
    column_names = readData[0].split(";")

    # Remove, since extracted
    del(readData[0])

    # d - Get index of selected_column entries in column_names
    column_indices = []
    for i in selected_columns:
        if i in column_names:
            column_indices.append(column_names.index(i))

    # e - Convert read data to ";" seperated lists, and fliter out
    # unwanted columns
    for i in readData:
        # Create dictionary to be added into, and split data
        dictionary = {}
        data = i.split(";")

        
        # Uses loop variable nameIndex to lookup name in selected_columns
        # which is used as dictionary key
        # and its' index in data in column_indices
        for nameIndex in range(len(column_indices)):
            columns_index = column_indices[nameIndex]
            dictionary[selected_columns[nameIndex]] = data[columns_index]

        # Append dictionary to missile_data
        missile_data.append(dictionary)

    return missile_data

def plot_circle_on_globe(globe_map, center, radius,
                         edge_color='red', alpha=0.15):
    """Draw a circle on a sphere.

    Args:
        globe_map: A `Basemap object`.
        center: A `tuple` containing the latitude, longitude of the center
                of the circle.
        radius: A `float` specifying the radius of the circle as measured on
                the surface of the sphere.
        edge_color: A matplotlib-compatible color specification of the edge
                color of the circle.
        alpha: A `float` specifying the level of opacity of the circle.
    """

    radius_of_earth = 6371

    # Convert to radians
    lat = center[0]/180.*np.pi
    lon = center[1]/180.*np.pi

    # Radius in terms of angle (radians)
    angle_dist = radius / radius_of_earth

    # An angular grid
    rot_angle = np.arange(0, 2*np.pi, 0.1)

    # Transformed latitude, longitude values for all grid points
    lat_rad = np.arcsin(np.sin(lat) * np.cos(angle_dist) +
                        np.cos(lat) * np.sin(angle_dist) * np.cos(rot_angle))
    lon_rad = lon + np.arctan2(np.sin(rot_angle) * np.sin(angle_dist) *
                               np.cos(lat),
                               np.cos(angle_dist) - np.sin(lat) *
                               np.sin(lat_rad))

    # Convert to degrees
    lat_degrees = lat_rad / np.pi * 180.
    lon_degrees = lon_rad / np.pi * 180.

    # Map from lat,lon values to x,y values
    mapped_coordinates = np.stack(globe_map(lon_degrees, lat_degrees)).T

    # Create Polygon on map
    plt.gca().add_patch(matplotlib.patches.Polygon(mapped_coordinates,
                                                   ec=edge_color, fc="none",
                                                   alpha=alpha, closed=True,
                                                   zorder=2, linewidth=1.))
def plot_missile_data(basemap, missile_data):
    keys = ["Facility Latitude", "Facility Longitude","Distance Travelled"]

    for data in missile_data:
        converted_data = []
        try:
            for key in keys:
                val = data[key]
                converted_data.append(float(val.strip(' km').replace(",",".")))
            plot_circle_on_globe(basemap, tuple(converted_data[:2]), converted_data[-1])
        except ValueError:
            continue

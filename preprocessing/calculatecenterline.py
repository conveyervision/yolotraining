import numpy as np

def compute_center_y(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    y_values = []
    for line in lines:
        data = line.strip().split() # remove leading/trailing whitespaces and split the line into list of values
        if len(data) > 2:  # check if there are at least 3 values in the line
            y_values.append(float(data[2])) # Extract the Y value
        else:
            break # Stop processing this file, as we've reached a line without enough data

    center_y = np.mean(y_values) if y_values else 0  # Compute the average, default to 0 if no data
    return center_y

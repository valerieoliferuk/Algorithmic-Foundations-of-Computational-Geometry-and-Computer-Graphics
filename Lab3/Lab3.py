import pandas as pd
import matplotlib.pyplot as mpl
import math

data = pd.read_csv("DS8.txt", header=None, sep = '\s+', names = ["x", "y"])

origin_x, origin_y = 480, 480
angle_rad = math.radians(90)
cos_teta = math.cos(angle_rad)
sin_teta = math.sin(angle_rad)


def rotate_point(x, y, origin_x, origin_y, sin_teta, cos_teta):
    x_in_new_origin = x - origin_x
    y_in_new_origin = y - origin_y
    
    rotated_x = x_in_new_origin*cos_teta - y_in_new_origin*sin_teta
    rotated_y = x_in_new_origin*sin_teta + y_in_new_origin*cos_teta
    
    final_x = rotated_x + origin_x
    final_y = rotated_y + origin_y
    return final_x, final_y

data[["rotated_x", "rotated_y"]] = data.apply(lambda row: rotate_point(row["x"], row["y"], origin_x, origin_y, sin_teta, cos_teta), axis = 1, result_type= "expand")

fig, ax = mpl.subplots(figsize=(9.6, 9.6), dpi=100)

ax.scatter(data["rotated_x"], data["rotated_y"], c='blue')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Lab№3 result image')

mpl.savefig('lab3_affine_transform.png', dpi=100)
mpl.show()

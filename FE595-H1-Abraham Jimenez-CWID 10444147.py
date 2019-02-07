# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 10:48:03 2019

@author: ramra
"""

# FE 595: Python for Finance
# Homework 1
# Abraham Jimenez-Berlanga
# CWID 10444147
#


import numpy as np
import matplotlib.pyplot as plt

###################################################################################################
#################################                                 #################################
#################################        Python Refresher         #################################
#################################        Sine and Cosine          #################################
###################################################################################################


# Generate 100 points, from 0 to 2 and we multiply by Pi, so we get a period
axis_x = np.arange(0, 2, 0.02)
#Convert our points to radians (2pi is a period)
axis_x = axis_x * np.pi

#Calculating the Sine
sine = np.sin(axis_x)

#Calculating the Cosine
cosine = np.cos(axis_x)

#Calculating the Cosine - Venkata
tan = np.tan(axis_x)
#Creating a Top level container for all plot elements venkata
fig = plt.figure()



#Defining the object graph_viz so the graph can be formated as desired
fig, graph_viz = plt.subplots()

#ploting the sine and cosine
graph_viz.plot(axis_x, sine, 'r--', label="Sine Function")
graph_viz.plot(axis_x, cosine, 'bs', label="Cosine Function")
graph_viz.plot(axis_x, tan, label="Tangent Function")

#Define the X axis limits
graph_viz.set_xlim((0, 2 * np.pi))

#Define the Y axis limits
graph_viz.set_ylim((-1,1))

#Deinining the ticks in the x axis, dividin the period in 4
graph_viz.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])

#Labeling the X ticks to a better representation
graph_viz.set_xticklabels(['0', '$\pi$/2', '$\pi$', '3$\pi$/2', '2$\pi$'])


plt.legend()
plt.title("Sine and Cosine Graphs")
plt.show(block=True)

#Saving the graph localli
# we can set the path here based on where we wanted to save- by default it save in same location where the python script exist
fig.savefig('sine_cosine_tangent.png')
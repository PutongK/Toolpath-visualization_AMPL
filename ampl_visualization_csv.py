# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:53:19 2024

AMPL visuallization method for .csv file

@author: kangputong
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class AmplVisualizationCSV:

    @staticmethod
    def comet(x, y=None, time=0.001):
        """
        Displays a comet plot.
        """
        x = np.asarray(x)
        plt.ion()
        plt.xlim(x.min(), x.max())
        if y is not None:
            y = np.asarray(y)
            plt.ylim(y.min(), y.max())
        else:
            plt.ylim(0, len(x))
        
        plot = plt.plot(x[0], y[0])[0] if y is not None else plt.plot(x[0])[0]

        for i in range(len(x) + 1):
            plot.set_data(x[:i], y[:i] if y is not None else None)
            plt.draw()
            plt.pause(time)
        plt.ioff()

    @staticmethod
    def comet3(x, y, z):
        """
        Displays a 3D comet plot (similar to MATLAB's comet3).
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlim([min(x), max(x)])
        ax.set_ylim([min(y), max(y)])
        ax.set_zlim([min(z), max(z)])

        line, = ax.plot([], [], [], lw=2, marker='o')

        def update(num, x, y, z, line):
            line.set_data(x[:num], y[:num])
            line.set_3d_properties(z[:num])
            return line,

        ani = FuncAnimation(fig, update, frames=len(x), fargs=[x, y, z, line], interval=50, blit=False)
        plt.show()
        return ani

    @staticmethod
    def get_float_input(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number")

    def visualization(self, input_file_path, output_excel_path="toolpath.xlsx"):
        """
        Main function for visualization.
        """
        
        # Load the CSV file
        file_path = input_file_path
        df = pd.read_csv(file_path)

        # Extract columns
        x = df['X']
        y = df['Y']
        z = df['Z']
        
        # User input for comet visualization
        answer = input("Comet visualization? Please input: comet, comet3, or none (default is 'none'): ").strip().lower()
        if answer not in ['comet', 'comet3', 'none']:
            answer = 'none'
        if answer == 'comet':
            self.comet(x, y)
        elif answer == 'comet3':
            self.comet3(x, y, z)

        # Plot x and y
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label='xy view', color='blue')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('xy view of the forming region')
        plt.legend()
        plt.grid(True)
        plt.show()     

# Example usage
if __name__ == "__main__":
    path_head = r"YOUR PATH\\"
    file_name = "NUToolpath_topToolTipPnts.csv"
    file_path = path_head + file_name
    ampl_vis = AmplVisualizationCSV()
    ampl_vis.visualization(input_file_path=file_path)
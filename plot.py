import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def data_init():
    spreadsheet_file = pd.ExcelFile('data.xlsx')
    worksheets = spreadsheet_file.sheet_names
    island_coordinates = []
    island_numbers = []
    locationDF = pd.read_excel('data.xlsx', sheet_name="Locations", header=None, skiprows=1)
    for index, row in locationDF.iterrows():
        island_coordinates.append([row[1], row[2]])
        island_numbers.append(row[0])
    return [island_numbers, island_coordinates]


def storm_init():
    storms = []
    stormDF = pd.read_excel('data.xlsx', sheet_name="Storms", header=None, skiprows=2)
    for index, row in stormDF.iterrows():
        storms.append([row[0], row[1], row[2]])
    return storms


def main():
    island_numbers, island_coordinates = data_init()
    storms = storm_init()
    
    file = open("data.txt", "r")
    optimum_route_string = file.readline().strip()

    route = optimum_route_string.split("->")
    optimum_route = []
    for i in range(len(route)):
        island = route[i].strip()
        island_number = island.split(" ")[1]
        optimum_route.append(int(island_number))
    
    data = np.array(island_coordinates)
    x, y = data.T
    plt.scatter(x, y)

    for i in range(len(island_coordinates)):
        x = island_coordinates[i][0]
        y = island_coordinates[i][1]
        plt.plot(x, y, 'bo')
        plt.text(x * (1 + 0.01), y * (1 + 0.01), i + 1, fontsize=12)

    for i in range(len(island_coordinates) - 1):
        # i = 0 .... n-1
        plt.plot([island_coordinates[optimum_route[i] - 1][0], island_coordinates[optimum_route[i+1] - 1][0]],
                 [island_coordinates[optimum_route[i] - 1][1], island_coordinates[optimum_route[i+1] - 1][1]], 'green', linestyle=':', marker='')

    for i in range(len(storms)):
        x = storms[i][0]
        y = storms[i][1]
        r = storms[i][2]
        circle1 = plt.Circle((x, y), r, color='r', alpha=0.3, fill=False, label="storm:" + str(i + 1))
        label = plt.annotate(i + 1, xy=(x, y), fontsize=12,
                            verticalalignment='center', horizontalalignment='center')
        plt.gcf().gca().add_artist(circle1)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.draw()

    plt.show()
    plt.savefig('plot.png', dpi=100)


if __name__ == '__main__':
    main()
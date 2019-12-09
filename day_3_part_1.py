START = (0, 0)

with open("day_3_input.txt", "r") as f:
    input = f.read().split('\n')
    wire_1_path = input[0].split(',')
    wire_2_path = input[1].split(',')


def all_coords_traveled(start_coords, wire_path):
    all_coords = [start_coords]
    for i, path in enumerate(wire_path):
        new_coords = get_path_coords(all_coords[-1], path)
        all_coords.extend(new_coords)
    return all_coords


def get_path_coords(start_coords, path):
    dir = path[0]
    steps = int(path[1:]) + 1
    if dir == 'R':
        path_coords = [(start_coords[0] + i, start_coords[1])
                       for i in range(1, steps)]
    elif dir == 'L':
        path_coords = [(start_coords[0] - i, start_coords[1])
                       for i in range(1, steps)]
    elif dir == 'U':
        path_coords = [(start_coords[0], start_coords[1] + i)
                       for i in range(1, steps)]
    elif dir == 'D':
        path_coords = [(start_coords[0], start_coords[1] - i)
                       for i in range(1, steps)]
    return path_coords


def get_intersections(path_1_coords, path_2_coords):
    return list(set(path_1_coords) & set(path_2_coords))


def manhattan_distance(point_a, point_b):
    x = abs(point_a[0] - point_b[0])
    y = abs(point_a[1] - point_b[1])
    return x + y


def find_shortest_distance(start, intersections):
    distances = []
    for i in intersections:
        distances.append(manhattan_distance(start, i))
    return min(distances)


def find_steps_to_point(coords_traveled_in_order, point):
    return coords_traveled_in_order.index(point)


def find_closest_intersection_by_steps(points, paths):
    step_counts = []
    for point in points:
        wire_1_steps = find_steps_to_point(paths[0], point)
        wire_2_steps = find_steps_to_point(paths[1], point)
        total_steps = wire_1_steps + wire_2_steps


if __name__ == '__main__':
    wire_1_coords = all_coords_traveled(START, wire_1_path)
    wire_2_coords = all_coords_traveled(START, wire_2_path)

    intersections = get_intersections(wire_1_coords, wire_2_coords)
    intersections.remove(START)

    print(find_shortest_distance(START, intersections))

def VLoSPS(grid, path):
    if not path:
        return []

    integer_path = []
    for point in path:
        if isinstance(point, (list, tuple)):
            x = int(round(point[0]))
            y = int(round(point[1]))
            integer_path.append((x, y))
        else:
            continue

    if len(integer_path) < 3:
        return integer_path

    # Check if there's unobstructed line of sight between two points
    def has_line_of_sight(grid, p1, p2):
        if p1 == p2:
            return True

        # Horizontal line of sight
        if p1[0] == p2[0]:
            y1, y2 = min(p1[1], p2[1]), max(p1[1], p2[1])
            for y in range(y1, y2 + 1):
                if not (0 <= p1[0] < len(grid)) or not (0 <= y < len(grid[0])):
                    return False
                if grid[p1[0]][y] != 1:
                    return False
            return True

        # Vertical line of sight
        if p1[1] == p2[1]:
            x1, x2 = min(p1[0], p2[0]), max(p1[0], p2[0])
            for x in range(x1, x2 + 1):
                if not (0 <= x < len(grid)) or not (0 <= p1[1] < len(grid[0])):
                    return False
                if grid[x][p1[1]] != 1:
                    return False
            return True

        return False  # Only axis-aligned visibility supported

    # Find the farthest point from current that is visible
    def find_farthest_visible(start_idx):
        for j in range(len(integer_path) - 1, start_idx, -1):
            if has_line_of_sight(grid, integer_path[start_idx], integer_path[j]):
                return j
        return start_idx + 1

    # Greedily build simplified path using farthest visible points
    simplified_path = [integer_path[0]]
    current_index = 0

    while current_index < len(integer_path) - 1:
        farthest = find_farthest_visible(current_index)
        if farthest > current_index + 1:
            simplified_path.append(integer_path[farthest])
            current_index = farthest
        else:
            simplified_path.append(integer_path[current_index + 1])
            current_index += 1

    return simplified_path


import noise
import random
import math

def generate_land(size, type):
    """
    Generate an island map based on noise and heightmap.
    """
    params = terrain_parameters.get(type, terrain_parameters['island'])
    scale_x, scale_y = params['scale_x'], params['scale_y']
    land_map = [['O' for _ in range(size)] for _ in range(size)]
    heightmap = [[0 for _ in range(size)] for _ in range(size)]
    center_x, center_y = size / 2, size / 2
    has_town = False

    # Generate heightmap using Perlin noise
    base = random.randint(0, 10000)
    for y in range(size):
        for x in range(size):
            n = noise.pnoise2(x * scale_x, y * scale_y, octaves=params['octaves'], persistence=params['persistence'], lacunarity=params['lacunarity'], repeatx=1024, repeaty=1024, base=base)
            heightmap[y][x] = ((n + 1) / 2.0) * params['heightMultiplier']  # Normalize to range [0, 1]

    # Convert heightmap to terrain types
    for y in range(size):
        for x in range(size):
            distance_to_center = math.sqrt((x - center_x)**2 + (y - center_y)**2)
            if type == 'island':
                threshold = 0.3 + distance_to_center / size * 0.5
            else:
                threshold = params['threshold'] + (1 - distance_to_center / size) * 0.3

            if heightmap[y][x] < threshold or (type != 'island' and random.random() < 0.02):  # 2% chance for water in non-island terrains
                land_map[y][x] = 'O'
            else:
                land_map[y][x] = 'P' if heightmap[y][x] < 0.5 else ('H' if heightmap[y][x] < 0.55 else 'M')

    # Add forests
    for y in range(size):
        for x in range(size):
            if land_map[y][x] == 'P' and random.random() < 0.2:
                land_map[y][x] = 'F'

    # Add a town
    while not has_town:
        rand_x, rand_y = random.randint(0, size-1), random.randint(0, size-1)
        if type == 'island':
            if land_map[rand_y][rand_x] in ['P', 'H', 'F', 'M'] and is_adjacent_to_water(rand_x, rand_y, land_map):
                land_map[rand_y][rand_x] = 'T'
                has_town = True
        else:
            if land_map[rand_y][rand_x] in ['P', 'H', 'F', 'M']:
                land_map[rand_y][rand_x] = 'T'
                has_town = True

    adjust_border_tiles(land_map, 0.6, type=type)

    return land_map

##Utilities
terrain_parameters = {
    'island': {
        'scale_x': 0.1,
        'scale_y': 0.1,
        'octaves': 2,
        'persistence': 0.5,
        'lacunarity': 2.0,
        'threshold': 0.3
        ,
        'heightMultiplier': 1
    },
    'flat': {
        'scale_x': 0.1,
        'scale_y': 0.1,
        'octaves':  3,
        'persistence': 0.2,
        'lacunarity': 2,
        'threshold': 0.03,
        'heightMultiplier': 0.9
    },
    'hilly': {
        'scale_x': 0.1,
        'scale_y': 0.1,
        'octaves':  3,
        'persistence': 0.2,
        'lacunarity': 2,
        'threshold': 0.03,
        'heightMultiplier': .95
    },
    'mountainous': {
        'scale_x': 0.1,
        'scale_y': 0.1,
        'octaves':  3,
        'persistence': 0.2,
        'lacunarity': 2,
        'threshold': 0.03,
        'heightMultiplier': 1.1
    }
}

def save_to_file(land_map, filename):
    """
    Save the given island map to a file.
    """
    with open(filename, 'w') as f:
        for row in land_map:
            f.write(''.join(row) + '\n')

def adjust_border_tiles(land_map, chance_to_transform=0.75, type='island'):
    """
    Adjust the border tiles of the island based on a given chance.
    """
    height, width = len(land_map), len(land_map[0])
    
    for y in range(height):
        for x in range(width):
            if x in [0, width-1] or y in [0, height-1]:
                if type == 'island':
                    if random.random() < chance_to_transform and land_map[y][x] != 'O':
                        land_map[y][x] = 'O'
                else:
                    if land_map[y][x] == 'O' and not is_adjacent_to_water(x, y, land_map):
                        if random.random() < chance_to_transform:
                            land_map[y][x] = 'P'

def is_adjacent_to_water(x, y, land_map):
    """
    Check if a tile is adjacent to a water tile.
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(land_map[0]) and 0 <= new_y < len(land_map):
            if land_map[new_y][new_x] == 'O':
                return True
    return False
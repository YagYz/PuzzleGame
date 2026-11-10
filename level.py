
# Example 
# # = Wall . = Floor  P = Player B = Box T = Target
LEVELS = [
    [
        "########",
        "#......#",
        "#.P.B.T#",
        "#......#",
        "########"
    ],
    [
        "########",
        "#P#...##",
        "#.#.B.T#",
        "#...##.#",
        "########"
    ]
]

def parse_level(level_map):
    walls = set()
    targets = set()
    boxes = set()
    playerPos = (0, 0)
    
    for y, row in enumerate(level_map):
        for x, char in enumerate(row):
            if char == '#':
                walls.add((x,y))
            elif char == 'T':
                targets.add((x,y))
            elif char == 'B':
                boxes.add((x,y))
            elif char == 'P':
                playerPos = (x,y)
                
    return walls, targets, boxes, playerPos
def try_move(player, boxes, walls, dx, dy):
    nx, ny = player[0] + dx, player[1] + dy
    
    # Collision Check
    if (nx, ny) in walls:
        return player, boxes, "blocked"
    
    # Check Boxes
    if (nx, ny) in boxes:
        bx, by = nx + dx, ny + dy
        if (bx, by) in walls or (bx, by) in boxes:
            return player, boxes, "blocked"
        new_boxs = set(boxes)
        new_boxs.remove((nx,ny))
        new_boxs.add((bx,by))
        return (nx, ny), new_boxs, "pushed"
    return (nx, ny), boxes, "moved"

def is_level_completed(boxes, targets):
    return boxes == targets
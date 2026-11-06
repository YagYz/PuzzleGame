def try_move(player, boxes, walls, dx, dy):
    nx, ny = player[0] + dx, player[1] + dy
    
    # Collision Check
    if (nx, ny) in walls:
        return player, boxes
    
    # Check Boxes
    if (nx, ny) in boxes:
        box_nx, box_ny = nx + dx, ny + dy
        if (box_nx, box_ny) in walls or (box_nx, box_ny) in boxes:
            return player, boxes
        
        boxes.remove((nx, ny))
        boxes.add((box_nx, box_ny))
        
    return (nx, ny), boxes

def is_level_completed(boxes, targets):
    return boxes == targets
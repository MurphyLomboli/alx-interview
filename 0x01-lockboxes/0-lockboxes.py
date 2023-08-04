# 0-lockboxes.py

def canUnlockAll(boxes):
    if not boxes or not isinstance(boxes, list):
        raise ValueError("Input should be a non-empty list of lists.")

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)


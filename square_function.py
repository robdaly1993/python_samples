def squared(square):
    try:
        square = int(square)
        return square * square
    except ValueError:
        return square * len(square)
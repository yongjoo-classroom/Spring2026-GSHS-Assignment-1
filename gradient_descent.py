def gradient_f(x: float, y: float) -> tuple:
    return (2*x + 2, 2*y + 4)

def gradient_descent(starting_values: tuple, learning_rate: float, num_iterations: int) -> tuple:
    x, y = starting_values

    for _ in range(num_iterations):
        dx, dy = gradient_f(x, y)
        x -= learning_rate * dx
        y -= learning_rate * dy

    return (x, y)
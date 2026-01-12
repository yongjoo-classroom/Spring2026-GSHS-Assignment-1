def gradient_f(x: float, y: float) -> tuple:
    dfdx = 2 * x + 2
    dfdy = 2 * y + 4
    return (dfdx, dfdy)

def gradient_descent(starting_values: tuple, learning_rate: float, num_iterations: int) -> tuple:
    x, y = starting_values
    for _ in range(num_iterations):
        dfdx, dfdy = gradient_f(x, y)
        x = x - learning_rate * dfdx
        y = y - learning_rate * dfdy
    return (x, y)

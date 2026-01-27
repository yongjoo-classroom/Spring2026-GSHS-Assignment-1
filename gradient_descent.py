def gradient_f(x: float, y: float) -> tuple:
    '''
    Compute the gradients of the function f(x,y) = x^2 + y^2 + 2x + 4y + 5
    for given coordinate x, y

    Returns:
        - A tuple (∂f/∂x, ∂f/∂y)
    '''
    # f(x,y) = x^2 + y^2 + 2x + 4y + 5
    # ∂f/∂x = 2x + 2
    # ∂f/∂y = 2y + 4
    return (2 * x + 2, 2 * y + 4)


def gradient_descent(starting_values: tuple, learning_rate: float, num_iterations: int) -> tuple:
    '''
    Perform gradient descent optimization.
    Returns:
        - (x, y) after num_iterations
    '''
    x, y = starting_values

    for _ in range(num_iterations):
        dx, dy = gradient_f(x, y)
        x = x - learning_rate * dx
        y = y - learning_rate * dy

    return (x, y)

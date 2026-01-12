
def gradient_f(x: float, y: float) -> tuple:
    '''
    Compute the gradients of the function f(x,y) = x^2 + y^2 + 2x + 4y + 5
    for given coordinate x, y

    Parameters:
        - x: The x-coordinate of the point.
        - y: The y-coordinate of the point.

    Returns:
        - A tuple (∂f/∂x, ∂f/∂y) for the given values of x and y.
    '''
    # Your code here
    dfdx = 2*x + 2
    dfdy = 2*y + 4
    return (dfdx, dfdy)

def gradient_descent(starting_values: tuple, learning_rate: float, num_iterations: int) -> tuple:
    '''
    Perform gradient descent optimization.
    
    Parameters:
        - starting_values: A tuple (x, y) representing the initial point.
        - learning_rate: The step size for each iteration.
        - num_iterations: The number of iterations to perform.
    
    Returns:
        - A tuple (x, y) representing the optimized point after gradient descent.
    '''
    # Your code here
    x, y = starting_values
    for _ in range(num_iterations):
        dfdx, dfdy = gradient_f(x, y)
        x = x - learning_rate * dfdx
        y = y - learning_rate * dfdy
    return (x, y)

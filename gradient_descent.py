
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
    return(2*x+2, 2*y+4)
    
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
    res = starting_values
    for i in range(num_iterations) :
        res = (res[0]-learning_rate*gradient_f(res[0], res[1])[0], res[1]-learning_rate*gradient_f(res[0], res[1])[1])
    return res

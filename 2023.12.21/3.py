def math_function_resolver(func_obj: 'function', *args: float, res_to_str = False):
    """Функция высшего порядка, которая вычисляет округлённые значения для различных математических функций """
    
    results = []
    
    for item in args:
        results.append(round(func_obj(item)))
    if res_to_str:
        results = [str(thing) for thing in results]
    return results

   
# >>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
# [2, 3, 4, 4, 4, 5, 6, 6, 6]
# >>> math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10))
# [2, 1, 0, 0, 0, -1, -2, -2, -2]
# >>> math_function_resolver(lambda x: 2.72**x, *range(1, 10), res_to_str=True)
# ['3', '7', '20', '55', '149', '405', '1101', '2996', '8149']
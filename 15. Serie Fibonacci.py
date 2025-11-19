15. Serie Fibonacci
def fibonacci(n):
    serie = [0, 1]
    while len(serie) < n:
        serie.append(serie[-1] + serie[-2])
    return serie

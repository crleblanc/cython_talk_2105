import numpy as np
import time

dx = 0.1
dy = 0.1
dx2 = dx*dx
dy2 = dy*dy

def run_all(laplace_funcs, array_shapes, niter=20, maxtime=2):
    results = []
    for name, laplace_func in laplace_funcs:

        time_diff = 0
        times = []
        shapes = []
        for array_shape in array_shapes:
            if time_diff > maxtime:
                continue

            work_array = np.zeros([array_shape, array_shape], dtype=np.float64)
            work_array[0] = 1.0

            t1 = time.time()
            laplace_func(work_array, dx2, dy2, niter)
            t2 = time.time()

            time_diff = (t2-t1)/niter
            times.append(time_diff)
            shapes.append(work_array.size)
            print(name, array_shape, time_diff)

        results.append({'name':name, 'array_shapes':shapes, 'times':times})
        print(name, shapes, times)

    return results
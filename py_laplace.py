# 2d Laplace from http://technicaldiscovery.blogspot.co.nz/2011/06/speeding-up-python-numpy-cython-and.html

def py_update(u, dx2, dy2):
    nx, ny = u.shape
    for i in xrange(1,nx-1):
        for j in xrange(1, ny-1):
            u[i,j] = ((u[i+1, j] + u[i-1, j]) * dy2 +
                      (u[i, j+1] + u[i, j-1]) * dx2) / (2*(dx2+dy2))

def py_run(work_array, dx2, dy2, niter):
    for x in xrange(niter):
        py_update(work_array, dx2, dy2)
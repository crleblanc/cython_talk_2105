// C implementation of the 2D laplace equation.  Modifies array in-place. i is the row, j is the column in the array.
#include <stdlib.h>
#include <string.h>

void c_update(double *u, int nx, int ny, double dx2, double dy2) {
    int i, j, idx;
    size_t array_size = nx*ny*sizeof(double);
    double *u_tmp = (double *) malloc(array_size);
    memcpy(u_tmp, u, array_size);

    for (i=1; i<ny-1; i++) {
        for (j=1; j<nx-1; j++) {
            idx = i*nx + j;
            u_tmp[idx] = ((u[idx+nx] + u[idx-nx]) * dy2 +
                       (u[idx+1] + u[idx-1]) * dx2) / (2*(dx2+dy2));
        }
    }

    memcpy(u, u_tmp, array_size);
    free(u_tmp);
}

// C implementation of the 2D laplace equation.  Modifies array in-place. i is the row, j is the column in the array.
void c_update(double *u, int nx, int ny, double dx2, double dy2) {
    int i, j, idx;
    for (i=1; i<ny-1; i++) {
        for (j=1; j<nx-1; j++) {
            idx = i*nx + j;
            u[idx] = ((u[idx+nx] + u[idx-nx]) * dy2 +
                       (u[idx+1] + u[idx-1]) * dx2) / (2*(dx2+dy2));
        }
    }
}

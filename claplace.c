// C implementation of the 2D laplace equation.  Modifies array in-place.
void c_update(double *u, int nx, int ny, double dx2, double dy2) {
    int i, j, elem;
    for (i=1; i<nx-1; i++) {
        for (j=1; j<ny-1; j++) {
            elem = j*ny + i;
            u[elem] = ((u[elem+1] + u[elem-1]) * dy2 +
                       (u[elem+nx] + u[elem-nx]) * dx2) / (2*(dx2+dy2));
        }
    }
}

#include <stdio.h>

double **create_matrix(int m, int n)
{
    double **p;
    int i;
    
    p = (double **)malloc(m * sizeof(double *));
    if(p!= NULL)
        for(i=o;i<m;++i)
            p[i] = (double *)malloc(n*sizeof(double));
    return p;
}

void mult(int *p1, int *p2)
{
	printf("in mult funtion");
}

void set_weights(int *p1)
{
	printf("in mult funtion");
}

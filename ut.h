#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

double **create_matrix(int m, int n)
{
    double **p, *q;
    int i;
    assert(m>0 && n>0);

    p = (double **)malloc(m * sizeof(double *));
    if(p == NULL) return p;
    q = (double *)malloc(m * n * sizeof(double ));
    if(q==NULL){
        free(p);
        return NULL;
    }
    for(i=0; i<m; ++i, q+=n)
        p[i] = q;

    return p;
}

void destroy_matrix(double **p, int m, int n)
/* Destroy an (m x n) matrix. Notice, the n variable
* is not used, it is just there to assist using the function. */
{
    int i;
    assert(m>0 && n>0);

    for (i = 0; i < m; ++i)
    free(p[i]);
    free(p);
}



void dot_mult(double **p1, double **p2)
{
	printf("in mult funtion");
}



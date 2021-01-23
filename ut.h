#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

double **create_matrix(int m, int n)
{
    double **p;
    int i;
    assert(m>0 && n>0);
    p = (double **)malloc(m * sizeof(double *));
    if(p == NULL) return p;
    for(i=0;i<m;++i)
    {
        p[i] = (double *)malloc(n*sizeof(double));
        if(p[i] == NULL)
            goto failed;
    }
    return p;

failed:
    for(--i;i>=0;--i)
        free(p[i]);
    free(p);
    return NULL;
}

void mult(int *p1, int *p2)
{
	printf("in mult funtion");
}

void set_weights(int *p1)
{
	printf("in mult funtion");
}

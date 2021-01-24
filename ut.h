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

void populate_matrix(double **p, int m, int n)
{
 // code to populate matrix here
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

/* The return type is actually `int (*)[r]`,
but C doesn't like that. Call this function with
int (*a)[2] = (int (*)[2])f_MatTrans(2, 3, x); */
double* transpose(int r, int c, double mat[][c]) {
    double (*a)[r] = malloc(c*sizeof(*a));
    for(int i=0; i<r; i++) {
        for(int j=0; j<c; j++) {
            a[j][i]=mat[i][j];
        }
    }
    for(int i=0; i<r; i++) {
        for(int j=0; j<c; j++) {
            printf("X[%d][%d]=%f\n",i,j,mat[i][j]);
            printf("A[%d][%d]=%f\n",i,j,a[i][j]);
        }
    }
    return *a;
}


void dot_mult(double **p1, double **p2)
{
	printf("in mult funtion");
}



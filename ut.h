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
    {
        p[i] = q;
    }
    //printf("Psize= %d,%d\n",sizeof(p),sizeof(p[0]));
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

/* The return type is actually `int (*)[r]`,
but C doesn't like that. Call this function with
int (*a)[2] = (int (*)[2])f_MatTrans(2, 3, x); */
void printM(double **p) {
	int r = sizeof(p[0])/sizeof(p[0][0]);
	int c = sizeof(p[0][0]);
	for(int i=0; i<r; i++) {
        for(int j=0; j<c; j++) {
            printf("matrix is r=%d c=%d [%d][%d] = %f\n",
            	r,c,i,j,p[i][j]);
        }
    } 
}

void prefill_matrix(double **p,int r,int c,double d)
{
	for(int i=0;i<r;++i)
	{
		for(int j=0;j<c;++j)
		{
			p[i][j] = d;
			//printf("p[%d][%d]=%f\n",i,j,p[i][j]);
		}
	}
}


double **dot_mult(double **p1, double **p2)
{
	
	int r = sizeof(p1)/sizeof(p1[0]);
	int c = sizeof(p1[0]);
	int x = sizeof(p2)/sizeof(p2[0]);
	int y = sizeof(p2[0]);
	assert(c = x);
	double **p = create_matrix(r, y);
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<r;j++)
		{
			for(int k=0;k<y;k++)
			{
				p[i][k] += p1[i][j] * p2[j][k];
			}
		}
	}
	
	return p;
}



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


void printM(double **p, int r, int c) {
	int d1 = sizeof(p)/sizeof(p[0]);
	int d2 = sizeof(p[0]);
	for(int i=0; i<r; i++) {
        for(int j=0; j<c; j++) {
            printf("matrix is r=%d c=%d [%d][%d] = %f d1=%d d2=%d\n",
            	r,c,i,j,p[i][j],d1,d2);
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


double **dot_mult(double **p1, int r, int c,
                    double **p2, int x, int y)
{
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

void transposeM(double **q,int r,int c)
{
	double **p = create_matrix(c, r);
	for(int i=0;i<r;++i)
	{
		for(int j=0;j<c;++j)
		{
			p[j][i] = q[i][j];
			//printf("p[%d][%d]=%f\n",i,j,p[i][j]);
		}
	}
	return p;
}


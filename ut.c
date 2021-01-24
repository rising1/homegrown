#include "ut.h"

#define INPUTS_R 1
#define INPUTS_C 3
#define HIDDEN_SIZE 4
#define OUTPUTS 2



void set_up_model()
{

}

int main(int argc, char* argv[]){

    printf("argc %d\n",argc);
    for(int i=0;i<argc;i++)
    {
    	printf("argv[%d]= %s\n",i,argv[i]);
    }

    set_up_model();

    double **weights1 =
        create_matrix(INPUTS_C,HIDDEN_SIZE);
    double **bias1 =
        create_matrix(HIDDEN_SIZE,1);
    double **hidden =
        create_matrix(HIDDEN_SIZE,1);
    double **weights2 =
        create_matrix(HIDDEN_SIZE,OUTPUTS);
    double **bias2 =
        create_matrix(OUTPUTS,1);
    double **outputs =
        create_matrix(OUTPUTS,1);
    double **weights1adj =
        create_matrix(INPUTS_C,HIDDEN_SIZE);
    double **bias1adj =
        create_matrix(HIDDEN_SIZE,1);
    double **weights2adj =
        create_matrix(HIDDEN_SIZE,OUTPUTS);
    double **bias2adj =
        create_matrix(OUTPUTS,1);



} 

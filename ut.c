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
 
    prefill_matrix(weights1,INPUTS_C,HIDDEN_SIZE,0.5);
    // printM(weights1,INPUTS_C,HIDDEN_SIZE);
    double **bias1 =
        create_matrix(HIDDEN_SIZE,1);
    prefill_matrix(bias1,HIDDEN_SIZE,1,0.5);
    /*double **hidden =
        create_matrix(HIDDEN_SIZE,1);
    prefill_matrix(hidden,HIDDEN_SIZE,1,0.0);*/
    double **weights2 =
        create_matrix(HIDDEN_SIZE,OUTPUTS);
    prefill_matrix(weights2,HIDDEN_SIZE,OUTPUTS,0.5);
    double **bias2 =
        create_matrix(OUTPUTS,1);
    prefill_matrix(bias2,OUTPUTS,1,0.5);
    double **outputs =
        create_matrix(OUTPUTS,1);
    prefill_matrix(outputs,OUTPUTS,1,0.0);
    double **weights1adj =
        create_matrix(INPUTS_C,HIDDEN_SIZE);
    prefill_matrix(weights1adj,INPUTS_C,HIDDEN_SIZE,0.0);
    double **bias1adj =
        create_matrix(HIDDEN_SIZE,1);
    prefill_matrix(bias1adj,HIDDEN_SIZE,1,0.0);    
    double **weights2adj =
        create_matrix(HIDDEN_SIZE,OUTPUTS);
    prefill_matrix(weights2adj,HIDDEN_SIZE,OUTPUTS,0.0);
    double **bias2adj =
        create_matrix(OUTPUTS,1);
    prefill_matrix(bias2adj,OUTPUTS,1,0.0);

    double inputs[][3] = {{1.0, 1.0, 0.0}}; 
    double targets[][1] = {{1.0},{0.0}};
    double **inputsT =
        create_matrix(INPUTS_C,INPUTS_R);   
    
    for(int i=0;i<1;i++)
    {
    	for(int j=0;j<3;j++)
    	{
    	inputsT[j][i] = inputs[i][j];
    	printf("inputs %d%d\t %f\n",i,j,inputs[i][j]);
    	}
    }
    //printM(weights1);
    double **hidden = dot_mult(inputsT,1,3, weights1,3,4);
    // printM(hidden,1,4);
} 

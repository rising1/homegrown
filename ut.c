# include <stdio.h>
/*#include <ut.h>*/

#define INPUTS_R 1
#define INPUTS_C 3
#define HIDDEN_SIZE 4
#define OUTPUTS 2

double hidden[HIDDEN_SIZE];
double weights1[INPUTS_C][HIDDEN_SIZE];
double weights2[HIDDEN_SIZE][OUTPUTS];
double output[OUTPUTS];
double bias1[HIDDEN_SIZE];
double bias2[OUTPUTS];
double weights1adj[INPUTS_C][HIDDEN_SIZE];
double weights2adj[HIDDEN_SIZE][OUTPUTS];
double bias1adj[HIDDEN_SIZE];
double bias2adj[OUTPUTS];

int *phidden = &hidden;
int *pweights1 = &weights1;
int *pweights2 = &weights2;
int *pweights1adj = &weights1adj;
int *pweights2adj = &weights2adj;
int *pbias1 = &bias1;
int *pbias2 = &bias2;
int *pbias1adj = &bias1adj;
int *pbias2adj = &bias2adj;




int main(int argc, char* argv[]){

    printf("argc %d\n",argc);
    for(int i=0;i<argc;i++)
    {
    	printf("argv[%d]= %s\n",i,argv[i]);
    }

   int inputs[][3] = [[1,1,0]];
   int *pinputs = &inputs;
   int outputs[][2] = {[1,0]};
   int *poutputs = &outputs;



   mult( phidden, pweights1);

} 

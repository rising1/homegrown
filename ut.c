#include "ut.h"

#define INPUTS_R 1
#define INPUTS_C 3
#define HIDDEN_SIZE 4
#define OUTPUTS_R 1
#define OUTPUTS_C 2

int main(int argc, char* argv[]){

	double lr = 0.01;
	int no_of_iterations = 1000;
	double starting_value = 1;

	double **hidden;
	double **outputs;
	double **error;
	double **dA_dZ;
	double **dH_dZ;
	double **act_err;
	double **weights1adj;
	double **bias2adj;
	double **weights2adj;
	double **bias1adj;
	double **mseP;


	double batch[][3] =  {{1.0, 1.0, 0.0},
						  {1.0, 0.0, 0.0},
						  {1.0, 0.0, 1.0},
						  {1.0, 1.0, 1.0},
						  {0.0, 0.0, 0.0}
						  };
    double targets[][2] = {{1.0, 0.0},
    					   {0.0, 0.0},
    					   {0.0, 0.0},
    					   {1.0, 0.0},
    					   {0.0, 0.0}
    					  };
    double test[][3] = {{0.0, 1.0, 0.0}};

    printf("argc %d\n",argc);
    for(int i=0;i<argc;i++)
    {
    	printf("argv[%d]= %s\n",i,argv[i]);
    }

    double **weights1 =
        create_matrix(INPUTS_C,HIDDEN_SIZE);
    prefill_matrix(weights1,INPUTS_C,HIDDEN_SIZE,starting_value);
    // printM(weights1,INPUTS_C,HIDDEN_SIZE);
    double **bias1 =
        create_matrix(HIDDEN_SIZE,1);
    prefill_matrix(bias1,HIDDEN_SIZE,1,starting_value);
    double **weights2 =
        create_matrix(HIDDEN_SIZE,OUTPUTS_C);
    prefill_matrix(weights2,HIDDEN_SIZE,OUTPUTS_C,starting_value);
    double **bias2 =
        create_matrix(OUTPUTS_C,1);
    prefill_matrix(bias2,OUTPUTS_C,1,starting_value);

    double **inputsT =
        create_matrix(INPUTS_C,INPUTS_R);
    double **testT =
        create_matrix(INPUTS_C,INPUTS_R);
    double **targetsT =
        create_matrix(OUTPUTS_C,OUTPUTS_R);
    double **inputs =
        create_matrix(INPUTS_R,INPUTS_C);
    double **target =
        create_matrix(OUTPUTS_R,OUTPUTS_C);  
    
    
    dA_dZ = create_matrix(OUTPUTS_C,OUTPUTS_R);
    dH_dZ = create_matrix(INPUTS_C,HIDDEN_SIZE);

    // The learning loop
    for(int n=0;n<no_of_iterations;n++)
    {
  
    for(int w=0;w<5;w++)
    {	
    	for(int x=0;x<3;x++)
    	{
    	inputs[0][x] = batch[w][x];
    	}
    	for(int y=0;y<2;y++)
    	{
    	target[0][y] = targets[w][y];
    	}
    
    	
    for(int i=0;i<1;i++)
    {
    	for(int j=0;j<3;j++)
    	{
    	inputsT[j][i] = inputs[i][j];
    	//printf("inputs %d%d\t %f\n",i,j,inputs[i][j]);
    	}
    }
    for(int i=0;i<1;i++)
    {
    	for(int j=0;j<2;j++)
    	{
    	targetsT[j][i] = target[i][j];
    	testT[j][i] = test[i][j];
    	//printf("targets %d%d\t %f\n",i,j,targets[i][j]);
    	}
    }   	
    	
    	
    	  	
    // Feed forward
    hidden = dot_mult(inputsT,1,3, weights1,3,4);
    //printM(hidden, 1, 4);
    outputs = dot_mult(transposeM(
              hidden,1,4),1,4,weights2,4,2);
    //printM(outputs, 1, 2);

	// Calc error
    error = math('-',
    		transposeM(targetsT,1,2),2,1,
            transposeM(outputs, 1, 2),2,1);
	mseP = mse(error,OUTPUTS_C,1);
    printf("mse= %f\n",mseP[0][0]);

    // Backpropagation

    for(int i=0;i<1;i++)
    {
    	for(int j=0;j<2;j++)
    	{
    	if(outputs[i][j] >= 0)
    	{
    		dA_dZ[i][j] = 1;
    	} else
    	 {
    	 	dA_dZ[i][j] = 0;
    	 }
    	//printf("dA_dZ %d%d\t %f\n",i,j,dA_dZ[i][j]);
    	}
    }


    for(int i=0;i<1;i++)
    {
    	for(int j=0;j<4;j++)
    	{
    	if(hidden[i][j] >= 0)
    	{
    		dH_dZ[i][j] = 1;
    	} else
    	 {
    	 	dH_dZ[i][j] = 0;
    	 }
    	//printf("dH_dZ %d%d\t %f\n",i,j,dH_dZ[i][j]);
    	}
    }

    act_err = math('x',dA_dZ,2,1,error,2,1);
    //printM(act_err, 2, 1);

    weights2adj = times(plain_mult(
    				transposeM(hidden, 1, 4),4,1,
    				transposeM(act_err,2,1),1,2),4,2,
    				lr);
   bias2adj = times(transposeM(act_err,2,1),1,2,lr);
   // printM(bias2adj, 1, 2);

   weights1adj = times(plain_mult(
    	  inputsT, 3, 1,
    		math('x',dH_dZ, 1, 4,
    		plain_mult(
          	transposeM(act_err,2,1),1,2,
          	transposeM(weights2, 4, 2), 2, 4),1,4),
    		1,4),3,4,lr);

   //printM(weights1adj, 3, 4);

   bias1adj	=  times(
    	math('x',dH_dZ,1,4,
    	plain_mult(
          transposeM(act_err,2,1),1,2,
          transposeM(weights2, 4, 2), 2, 4),1,4)
    		,1,4,lr);
    //printM(bias1adj, 	1, 4);

    weights1 = math('+',weights1,INPUTS_C,HIDDEN_SIZE,
    				weights1adj,INPUTS_C,HIDDEN_SIZE);
    bias1 = math('+',bias1,1,HIDDEN_SIZE,
    				bias1adj,1,HIDDEN_SIZE);
    weights2 = math('+',weights2,HIDDEN_SIZE,OUTPUTS_C
                        ,weights2adj,HIDDEN_SIZE,OUTPUTS_C);
    bias2 = math('+',bias2,1,OUTPUTS_C,
    				bias2adj,1,OUTPUTS_C);

    } // end of batch
    } // end of learning loop

    // Feed forward test
    hidden = dot_mult(testT,1,3, weights1,3,4);
    outputs = dot_mult(transposeM(
       hidden,1,4),1,4,weights2,4,2);
    printM(outputs, 1, 2);

    
   destroy_matrix(weights1); 
   destroy_matrix(weights1adj);
   destroy_matrix(weights2);
   destroy_matrix(weights2adj);   
   destroy_matrix(bias1); 
   destroy_matrix(bias1adj);
   destroy_matrix(bias2);
   destroy_matrix(bias2adj);
   destroy_matrix(inputsT);
   destroy_matrix(targetsT);
   destroy_matrix(dA_dZ);
   destroy_matrix(dH_dZ);
   destroy_matrix(error);
   destroy_matrix(mseP);
   destroy_matrix(act_err);
   destroy_matrix(hidden);
   destroy_matrix(outputs);
} 

# include <stdio.h>

/* function to load weights and bias matrices */
int *load_matrix(int a, int b) {
	
	static double matrix[a][b];
	
	for(int i=0;i<a;i++){
 		for(int j=0;j<b;j++){
 			matrix[i][j] = 0.5;
 			printf("%f\n",matrix[i][j]);
 		}
 	}
   
   return matrix;
}

int main(int argc, char **argv[]){
 	
 	double hidden[4][1] = {[0.0],[0.0],[0.0],[0.0]};
 	double final[2][1] = {[0.0],[0.0]};
 	
 	int *weights1;
 	int *weights2;
 	int *bias1;
 	int *bias2;
 	
 	weights1 = load_matrix(3, 4); 
 	weights2 = load_matrix(4, 2);	
 	bias1 = load_matrix(4, 1);
 	bias2 = load_matrix(2, 1);
 	
 	
    printf("argc = %d\n", argc);
   for(int ndx = 0; ndx != argc; ndx++)
        printf("argv[%d] --> %s\n", ndx,argv[ndx]);
    
 	
    printf("char %d \n",sizeof('x'));
    printf("string %d\n",sizeof("x"));
 	printf("int %d",weights2); 
} 

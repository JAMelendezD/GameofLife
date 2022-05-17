// -----------------------------------------------------------------------------
// conways.c : Conways game of life in C (9.35)
// -----------------------------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int mod(int a, int b) {
    return ((a % b) + b) % b;
}

void write_file(char name[], int rows, int cols, int world[rows][cols]) {   
    
    FILE *fp;
    fp = fopen(name, "w+");
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; j++) {
            fprintf(fp, "%d ", world[i][j]);
        }
        fprintf(fp, "\n");
    }
    fclose(fp);
}

void init_world(int rows, int cols, int world[rows][cols]) {    
    
    srand(time(0));
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; j++) {
            world[i][j] = rand() % 2;
        }
    }
}

void update_world(int rows, int cols, int world[rows][cols]) {    
    
    int old_world[rows][cols];
    memcpy(old_world, world, sizeof (int) * rows * cols);
    
    for (int i=0; i<rows; ++i) {
        for (int j=0; j<cols; j++) {
            int state = old_world[i][j];                 
            int neis = old_world[mod(i, rows)][mod(j + 1, rows)]
                      +old_world[mod(i, rows)][mod(j - 1, rows)]
                      +old_world[mod(i + 1, rows)][mod(j, rows)]
                      +old_world[mod(i - 1, rows)][mod(j, rows)]
                      +old_world[mod(i + 1, rows)][mod(j + 1, rows)]
                      +old_world[mod(i - 1, rows)][mod(j - 1, rows)]
                      +old_world[mod(i + 1, rows)][mod(j - 1, rows)]
                      +old_world[mod(i - 1, rows)][mod(j + 1, rows)];
            
            if (state == 1) {
                if (neis != 2 && neis != 3) {
                    world[i][j] = 0;
                }
            }
            else {
                if (neis == 3) {
                    world[i][j] = 1;
                }  
            }
        }
    }
}

int main (int argc, char **argv) {
    
    int rows = atoi(argv[1]);
    int cols = atoi(argv[2]);
    int frames = atoi(argv[3]);
    char *name = (char*)malloc(100 * sizeof(char));

    int world[rows][cols];
    
    //int **world = malloc(sizeof*world*rows);
    //for (int i = 0; i < rows;i++)
        //world[i] = malloc(sizeof**world*cols);

    init_world(rows, cols, world);

    printf("Started simulation\n");
    clock_t start = clock();
    for (int frame = 0; frame < frames + 1; frame++) {
        sprintf(name, "%06d.txt", frame);
        write_file(name, rows, cols, world);
        update_world(rows, cols, world);  
    }
    printf("Finished simulation in: %6.2f seconds\n",
            ((double)clock() - start)/CLOCKS_PER_SEC);
    free(name);
    
} 
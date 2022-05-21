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

void write_file(char name[], int rows, int cols, int *world) {   
    
    FILE *fp;
    fp = fopen(name, "w+");
    
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; j++) {
            fprintf(fp, "%d ", *(world + i * cols + j));
        }
        fprintf(fp, "\n");
    }
    fclose(fp);
}

int * init_world(int rows, int cols) {    
    
    int *world = (int *)malloc(rows * cols * sizeof(int)); 
    srand(time(0));

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; j++) {
            *(world + i * cols + j) = rand() % 2;
        }
    }
    return world;
}

void update_world(int rows, int cols, int *world) {    
    
    int *old_world = (int *)malloc(rows * cols * sizeof(int));
    memcpy(old_world, world, sizeof (int) * rows * cols);
    
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; j++) {
            int state = *(old_world + i * cols + j);                 
            int neis = *(old_world + mod(i, rows) * cols + mod(j - 1, rows)) +
                       *(old_world + mod(i, rows) * cols + mod(j + 1, rows)) +
                       *(old_world + mod(i + 1, rows) * cols + mod(j, rows)) +
                       *(old_world + mod(i - 1, rows)*cols + mod(j, rows)) +
                       *(old_world + mod(i + 1, rows) * cols + mod(j + 1, rows)) +
                       *(old_world + mod(i - 1, rows) * cols + mod(j - 1, rows)) +
                       *(old_world + mod(i + 1, rows) * cols + mod(j - 1, rows)) +
                       *(old_world + mod(i - 1, rows) * cols + mod(j + 1, rows));

            if (state == 1) {
                if (neis != 2 && neis != 3) {
                    *(world + i * cols + j) = 0;
                }
            }
            else {
                if (neis == 3) {
                    *(world + i * cols + j) = 1;
                }  
            }
        }
    }
    free(old_world);
}

int main (int argc, char **argv) {
    
    int rows = atoi(argv[1]);
    int cols = atoi(argv[2]);
    int frames = atoi(argv[3]);
    char *name = (char*)malloc(100 * sizeof(char));
    int *world;
    world = init_world(rows, cols);

    sprintf(name, "%06d.txt", 0);
    write_file(name, rows, cols, world);  

    printf("Started simulation\n");
    clock_t start = clock();
    for (int frame = 1; frame < frames + 1; frame++) {
        update_world(rows, cols, world);
        sprintf(name, "%06d.txt", frame);
        write_file(name, rows, cols, world);  
    }
    printf("Finished simulation in: %6.2f seconds\n",
            ((double)clock() - start)/CLOCKS_PER_SEC);
    free(name);
    free(world);
} 
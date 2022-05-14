// ---------------------------------------------------------------------------------------
// conways.c : Conways game of life in C (9.35)
// ---------------------------------------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void write_file(char name[],int rows, int cols, int world[rows][cols])
{   
    FILE *fp;
    fp = fopen(name, "w+");
    for (int i=0; i<rows; ++i)
    {
        for (int j=0; j<cols; j++)
        {
            fprintf(fp, "%d ", world[i][j]);
        }
        fprintf(fp, "\n");
    }
}

void init_world(int rows, int cols, int world[rows][cols])
{    
    srand(time(0));

    for (int i=0; i<rows; ++i)
    {
        for (int j=0; j<cols; j++)
        {
            world[i][j] = rand() % 2;
        }
    }
}

void update_world(int rows, int cols, int world[rows][cols])
{    
    int old_world[rows][cols];
    memcpy(old_world, world, sizeof (int) * rows * cols);
    
    for (int i=0; i<rows; ++i)
    {
        for (int j=0; j<cols; j++)
        {
            int state = old_world[i][j];                 // Check neighbors
            int neis = old_world[i%rows][(j+1)%cols]
                      +old_world[i%rows][(j-1)%cols]
                      +old_world[(i+1)%rows][j%cols]
                      +old_world[(i-1)%rows][j%cols]
                      +old_world[(i+1)%rows][(j+1)%cols]
                      +old_world[(i-1)%rows][(j-1)%cols]
                      +old_world[(i+1)%rows][(j-1)%cols]
                      +old_world[(i-1)%rows][(j+1)%cols];
            
            if (state == 1)                             // Kill if alive and nei !2 or !3
            {
                if (neis != 2 && neis != 3)
                {
                    world[i][j] = 0;
                }
            }
            else                                        // Alive if death and nei 3
            {
                if (neis == 3)
                {
                    world[i][j] = 1;
                }  
            }                                           // Otherwise stay dead or alive 
        }
    }
}

int main (int argc, char **argv)
{
    int rows = atoi(argv[1]);
    int cols = atoi(argv[2]);
    int frames = atoi(argv[3]);

    int world[rows][cols];
    init_world(rows,cols,world);
    clock_t start = clock();
    printf("Started simulation\n");
    for (int frame=0; frame<frames+1; frame++)
    {
        char *name = (char*)malloc(20*sizeof(char));
        sprintf(name, "%06d.txt", frame);
        write_file(name,rows,cols,world);
        update_world(rows,cols,world);
        free(name);  
    }
    printf("Finished simulation in: %6.2f seconds\n",((double)clock()-start)/CLOCKS_PER_SEC);
} 
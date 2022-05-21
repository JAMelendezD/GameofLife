// -----------------------------------------------------------------------------
// conways.java : Conways game of life in Java
// -----------------------------------------------------------------------------

import java.io.*;

class Conways {
    
    public static int mod(int a, int b) {
        return ((a % b) + b) % b;
    }

    public static void write_file(String name, int[][] world) {

        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < world.length; i++) {
            for (int j = 0; j < world[0].length; j++) {
                builder.append(world[i][j]+"");
                if (j < world.length - 1)
                    builder.append(" ");
            }
            builder.append("\n");
        }

        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter(name));
            writer.write(builder.toString());
            writer.close();
        }
        catch(IOException e) {

        }
    }

    public static int[][] init_world(int rows, int cols) {

        int[][] world = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                world[i][j] = ((int) (Math.random() * 2));
            }
        }
        return world;
    }

    public static void update_world(int[][] world) {

        int rows = world.length;
        int cols = world[0].length;

        int [][] old_world = new int[rows][];
        for(int i = 0; i < rows; i++) {
            old_world[i] = world[i].clone();
        }

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int state = old_world[i][j];
                int neis = old_world[mod(i, rows)][mod(j + 1, cols)]
                          +old_world[mod(i, rows)][mod(j - 1, cols)]
                          +old_world[mod(i + 1, rows)][mod(j, cols)]
                          +old_world[mod(i - 1, rows)][mod(j, cols)]
                          +old_world[mod(i + 1, rows)][mod(j + 1, cols)]
                          +old_world[mod(i - 1, rows)][mod(j - 1, cols)]
                          +old_world[mod(i + 1, rows)][mod(j - 1, cols)]
                          +old_world[mod(i - 1, rows)][mod(j + 1, cols)];

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

    public static void main(String[] args) {
        
        int rows = Integer.parseInt(args[0]); 
        int cols = Integer.parseInt(args[1]); 
        int frames = Integer.parseInt(args[2]); 
        int[][] world = init_world(rows, cols);

        String name = String.format("%06d.txt", 0);
        write_file(name, world);

        System.out.println("Started simulation");
        long start = System.nanoTime();
        for (int frame = 1; frame < frames + 1; frame++) {
            update_world(world);
            name = String.format("%06d.txt", frame);
            write_file(name, world);  
        }
        long end = System.nanoTime(); 
        double time =  ((end - start) / 1e9);
        System.out.format("Finished simulation in: %6.2f seconds\n", 
            (double) time);
    }
}
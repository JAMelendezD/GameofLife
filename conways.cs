// -----------------------------------------------------------------------------
// conways.cs : Conways game of life in C# (1 min 13 sec)
// -----------------------------------------------------------------------------

using System;
using System.IO;
using System.Collections.Generic;

namespace ConwaysCS {
    class Conway {
        public static int mod(int a, int b) {
            return (a % b + b) % b;
        }
        public static int[,] init_world(int rows, int cols) {
            
            int[,] world = new int[rows, cols];
            Random r = new Random();
            
            for (int i = 0; i < rows; i++) {
                    for (int j = 0; j < cols; j++) {
                        world[i,j] = r.Next(0, 2);
                    }
                }
            return world;
        }

        public static void update_world(int[,] world) {
            
            int rows = world.GetLength(0);
            int cols = world.GetLength(1);
            int[,] old_world = world.Clone() as int[,];

            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
            
                    int state = old_world[i,j];
                    int neis = old_world[mod(i, rows), mod( j + 1, cols)]
                              +old_world[mod(i, rows), mod(j - 1, cols)]
                              +old_world[mod(i + 1, rows), mod(j, cols)]
                              +old_world[mod(i - 1, rows), mod(j, cols)]
                              +old_world[mod(i + 1, rows), mod(j + 1, cols)]
                              +old_world[mod(i - 1, rows), mod(j - 1, cols)]
                              +old_world[mod(i + 1, rows), mod(j - 1, cols)]
                              +old_world[mod(i - 1, rows), mod(j + 1, cols)];   
                    
                    if (state == 1) {
                        if (neis != 2 && neis != 3) {
                            world[i,j] = 0;
                        }
                    }
                    else {
                        if (neis == 3) {
                            world[i,j] = 1;
                        }  
                    }
                }
            }
        }

        public static void write_file(string name, int[,] world) {
            
            int rows = world.GetLength(0);
            int cols = world.GetLength(1);
            
            using (var sw = new StreamWriter(name)) {
                for (int i = 0; i < rows; i++) {
                    for (int j = 0; j < cols; j++) {
                        sw.Write(world[i,j] + " ");
                    }
                    sw.Write("\n");
                }
                sw.Flush();
                sw.Close();
            }
        }

        static void Main(string[] args) {
            
            int rows = Int32.Parse(args[0]);
            int cols = Int32.Parse(args[1]);
            int frames = Int32.Parse(args[2]);
            int[,] world = init_world(rows, cols);
            
            Console.WriteLine("Started simulation");
            var tStart = DateTime.UtcNow;
            for (int frame = 0; frame < frames+1; frame++) {
                string name = frame.ToString("D6") + ".txt";
                write_file(name, world);
                update_world(world);
            }
            var tD = DateTime.UtcNow - tStart;
            string time = tD.TotalSeconds.ToString("0.##"); 
            Console.WriteLine("Finished simulation in: " + time + " seconds");
        }
    }
}
// -----------------------------------------------------------------------------
// conways.rc : Conways game of life in Rust
// -----------------------------------------------------------------------------

extern crate rand;
extern crate array2d;

use rand::Rng;
use std::env;
use array2d::Array2D;
use std::fs::File;
use std::io::{BufWriter, Write};
use std::time::*;

fn write_file(name:&String, rows:usize, cols:usize, world: &mut Array2D<i32>) {
    let f = File::create(name).expect("Unable to create file");
    let mut f = BufWriter::new(f);
    for i in 0..rows {
        for j in 0..cols {
            let to_write = format!("{} ",  world[(i,j)]);
            f.write(to_write.as_bytes()).expect("Unable to write data");
        }
        let to_write = format!("{}",  "\n");
        f.write_all(to_write.as_bytes()).expect("Unable to write data");
    }
}

fn init_world(rows:usize,cols:usize,world: &mut Array2D<i32>) {
    let mut rng = rand::thread_rng();
    for i in 0..rows {
        for j in 0..cols {
            world[(i, j)] = rng.gen_range(0..2);
        }
    }
}

fn update_world(rows:usize,cols:usize,world: &mut Array2D<i32>) {    
    
    let old_world = world.clone();
    
    for i in  0..rows {
        for j in  0..cols {
            let state = old_world[(i, j)];                 
            let neis = old_world[((i).rem_euclid(rows), (j + 1).rem_euclid(cols))]
                      +old_world[((i).rem_euclid(rows), (j - 1).rem_euclid(cols))]
                      +old_world[((i + 1).rem_euclid(rows), (j).rem_euclid(cols))]
                      +old_world[((i - 1).rem_euclid(rows), (j).rem_euclid(cols))]
                      +old_world[((i + 1).rem_euclid(rows), (j + 1).rem_euclid(cols))]
                      +old_world[((i - 1).rem_euclid(rows), (j - 1).rem_euclid(cols))]
                      +old_world[((i + 1).rem_euclid(rows), (j - 1).rem_euclid(cols))]
                      +old_world[((i - 1).rem_euclid(rows), (j + 1).rem_euclid(cols))];
            
            if state == 1 {
                if neis != 2 && neis != 3 {
                    world[(i, j)] = 0;
                }
            }
            else {
                if neis == 3 {
                    world[(i, j)] = 1;
                }  
            } 
        }
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let rows: usize = args[1].parse().unwrap();
    let cols: usize = args[2].parse().unwrap();
    let frames: usize = args[3].parse().unwrap();    
    
    let world = &mut Array2D::filled_with(0, rows, cols);
    init_world(rows, cols, world);

    let name = format!("{:06}.txt", 0);
    write_file(&name, rows, cols, world);

    println!("Started simulation");
    let now = Instant::now();
    for frame in 1..frames + 1
    {
        update_world(rows, cols, world);
        let name = format!("{:06}.txt", frame);
        write_file(&name, rows, cols, world);
    }
    let elapsed_time = now.elapsed();
    println!("Finished simulation in: {:6.2} seconds", 
    elapsed_time.as_millis() as f32/1000.0);
}
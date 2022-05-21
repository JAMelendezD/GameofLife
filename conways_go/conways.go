package main

import (
    "fmt"
    "os"
    "strconv"
    "math/rand"
    "time"
)

func mod(a, b int) int {
    return ((a % b) + b) % b
}

func write_file(name string, rows int, cols int, world []int) {

    f, _ := os.Create(name)
    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            fmt.Fprintf(f, "%d ", world[i * cols + j])
        }
        fmt.Fprintf(f, "\n")
    }
}

func init_world(rows int, cols int) []int {

    s1 := rand.NewSource(time.Now().UnixNano())
    r1 := rand.New(s1)
    world := make([]int, rows*cols)

    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            world[i * cols + j] = r1.Intn(2)
        }
    }
    return world
}

func update_world(rows int, cols int, world []int) {

    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            old_world := world
            state := old_world[i * cols + j];                 
            neis := old_world[mod(i, rows) * cols + mod(j - 1, rows)] + 
                    old_world[mod(i, rows) * cols + mod(j + 1, rows)] + 
                    old_world[mod(i + 1, rows) * cols + mod(j, rows)] + 
                    old_world[mod(i - 1, rows) * cols + mod(j, rows)] +
                    old_world[mod(i + 1, rows) * cols + mod(j + 1, rows)] +
                    old_world[mod(i - 1, rows) * cols + mod(j - 1, rows)] +
                    old_world[mod(i + 1, rows) * cols + mod(j - 1, rows)] +
                    old_world[mod(i - 1, rows) * cols + mod(j + 1, rows)]

            fmt.Println(neis)

            if state == 1 {
                if neis != 2 && neis != 3 {
                    world[i * cols + j] = 0
                }
            } else {
                if neis == 3 {
                    world[i * cols + j] = 1
                }  
            }
        }
    }
}

func main() {

    rows, _ := strconv.Atoi(os.Args[1])
    cols, _ := strconv.Atoi(os.Args[2])
    frames, _ := strconv.Atoi(os.Args[3])
    world := init_world(rows, cols)

    fmt.Printf("Started simulation\n")
    start := time.Now()
    for frame := 0; frame < frames; frame++ {
        name := fmt.Sprintf("%06d.txt", frame)
        write_file(name, rows, cols, world)
        //fmt.Println(world)
        update_world(rows, cols, world)
        //fmt.Println(world)
    }
    duration := time.Since(start)
    fmt.Printf("Finished simulation in: %6.2f seconds\n", duration.Seconds())
}
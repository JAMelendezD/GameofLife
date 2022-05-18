# ------------------------------------------------------------------------------
# conways.cs : Conways game of life in R (16 min 11 sec)
# ------------------------------------------------------------------------------

update_world <- function(world) {

    shape <- dim(world)
    rows <- shape[1]
    cols <- shape[2]
    old_world <- cbind(world)

    for (i in  1:rows) {
        for (j in  1:cols) {
            state <- old_world[i,j]
            neis <- old_world[(i - 1) %% rows + 1, j %% cols + 1] +
                    old_world[(i - 1) %% rows + 1, (j - 2) %% cols + 1] +
                    old_world[i %% rows + 1, (j - 1) %% cols + 1] +
                    old_world[(i - 2) %% rows + 1, (j - 1) %% cols + 1] +
                    old_world[i %% rows + 1, j %% cols + 1] +
                    old_world[(i - 2) %% rows + 1, (j - 2) %% cols + 1] +
                    old_world[i %% rows + 1, (j - 2) %% cols + 1] +
                    old_world[(i - 2) %% rows + 1, j %% cols + 1]

            if (state == 1) {
                if ((neis != 2) & (neis != 3)) {
                    world[i,j] <- 0
                }
            }
            else {
                if (neis == 3) {
                    world[i,j] <- 1
                }
            }
        }
    }
    return(world)
}

main <- function() {

    args <- commandArgs(trailingOnly = TRUE)
    rows <- strtoi(args[1])
    cols <- strtoi(args[2])
    frames <- strtoi(args[3])

    world <- round(matrix(runif(rows * cols), rows, cols))

    print("Started simulation")
    start_time <- Sys.time()
    for (frame in 0:frames) {
        name <- sprintf("%06d.txt", frame)
        write(world, file = name, ncolumns = cols)
        world <- update_world(world)
    }
    td <- difftime(Sys.time(), start_time, units = "secs")
    sprintf("Finished simulation in: %6.2f seconds", td)
}

main()
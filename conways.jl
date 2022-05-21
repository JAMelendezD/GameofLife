# ------------------------------------------------------------------------------
# conways.jl : Conways game of life in R 
# ------------------------------------------------------------------------------

using Random
using DelimitedFiles
using Printf

function update_world(rows, cols, world)

	old_world = copy(world)

	for i in 1:rows
		for j in 1:cols
			state = old_world[i, j]
			neis = old_world[mod(i - 1, rows) + 1, mod(j, cols) + 1] +
                   old_world[mod(i - 1, rows) + 1, mod(j - 2, cols) + 1] +
                   old_world[mod(i, rows) + 1, mod(j - 1, cols) + 1] +
                   old_world[mod(i - 2, rows) + 1, mod(j - 1, cols) + 1] +
                   old_world[mod(i, rows) + 1, mod(j, cols) + 1] +
                   old_world[mod(i - 2, rows) + 1, mod(j - 2, cols) + 1] +
                   old_world[mod(i, rows) + 1, mod(j - 2, cols) + 1] +
                   old_world[mod(i - 2, rows) + 1, mod(j, cols) + 1]	            

			if (state == 1)								
				if (neis != 2 && neis != 3)
                    world[i, j] = 0
                end
			else
				if (neis == 3)								
					world[i, j] = 1
                end
            end
        end
    end
end

function main()

    rows = parse(Int64, ARGS[1])
    cols = parse(Int64, ARGS[2])
    frames = parse(Int64, ARGS[3])
    world = rand(0:1, rows, cols)

    open(lpad(0, 6, "0")*".txt", "w") do io
        writedlm(io, world, ' ')
    end

    println("Started simulation")
    t = @elapsed begin
    for frame in 1:frames
        update_world(rows, cols, world)
        open(lpad(frame, 6, "0")*".txt", "w") do io
            writedlm(io, world, ' ')
        end
    end
    end
    @printf "Finished simulation in: %6.2f seconds\n" t
end
    
main()
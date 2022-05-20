using Random
using DelimitedFiles

function update_world(world)
    

function main()

    rows = parse(Int64, ARGS[1])
    cols = parse(Int64, ARGS[2])
    frames = parse(Int64, ARGS[3])
    

    world = rand(0:1, rows, cols)
    open("delim_file.txt", "w") do io
        writedlm(io, world, ' ')
    end;


end
    
main()
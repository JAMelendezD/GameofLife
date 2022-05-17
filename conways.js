// -----------------------------------------------------------------------------
// conways.js : Conways game of life in Java Script (46.46)
// -----------------------------------------------------------------------------

function mod(a, b) {
    return ((a % b) + b) % b;
}

function init_world(rows, cols) {
    
    world = new Array(cols);

    for (var i = 0; i < rows; i++) {
        world[i] = [];
        for ( var j = 0; j < cols; j++) {
            world[i][j] = Math.floor(Math.random()*2);
        }
    }   
}

function update_world(world) {

    rows = world.length;
    cols = world[0].length;

    var old_world = world.map(function(arr) {
        return arr.slice();
    });

    for (var i = 0; i < rows; i++) {
        for ( var j = 0; j < cols; j++) {
            state = old_world[i][j];
            neis = old_world[mod(i, rows)][mod(j + 1, cols)]
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

function main() {

    const Args = process.argv.slice(2);
    const rows = parseInt(Args[0]);
    const cols = parseInt(Args[1]);
    const frames = parseInt(Args[2]); 
    const fs = require('fs');

    init_world(rows, cols);

    console.log("Started simulation");
    var start = new Date().getTime();
    for (let frame = 0; frame < frames + 1; frame++) {
        var name = `${frame}.txt`.padStart(10,'0');
        fs.writeFileSync(name, world.join('\n').replaceAll(',',' '));
        update_world(world);
    }
    var end = new Date().getTime();
    var time = (end - start) / 1000;
    console.log(`Finished simulation in: ${time.toFixed(2)} seconds`)
}

if (require.main === module) {
    main();
}
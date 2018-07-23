// sumber link test https://www.hackerrank.com/challenges/2d-array/problem


'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}



function main() {
    let arr = Array(6);

    for (let i = 0; i < 6; i++) {
        arr[i] = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));
    }

    // console.log(arr)
    var sumarr = [];
    
    var h = 0;
    for (var i = 0; i < 4; i++) {
        for (var j = 0; j < 4; j++) {
            sumarr[h] = arr[i][j] + arr[i][j+1] + arr[i][j+2]
                    + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1]
                    + arr[i+2][j+2];
            h++;
        }
    }

    sumarr.sort();
    // console.log(sumarr)
    
    var max = -99999;
    for (var x = 0; x < 16; x++){
        if (sumarr[x] > max)
            max = sumarr[x];
    }
    
    console.log(max);
}

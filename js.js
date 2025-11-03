//  const matrizDinamica = [];
//  for (let i = 0; i < 3; i++) {
//      const linha = [];
//      for (let j = 0; j < 3; j++) {
//          linha.push(0);
//      }
//      matrizDinamica.push(linha);
//  }
//  console.log(matrizDinamica)

// matriz = [1, 2, 3]

// for (let i = 0; i < matriz.length; i++) {
//     for (let j = 0; j < matriz[i].length; j++) {
//         console.log(`Elemento [${i}][${j}] = ${matriz[i][j]}`);
//     }
// }

const matrizDinamica = [];
for (let i = 0; i < 3; i++) {
    const linha = [];
    for (let j = 0; j < 3; j++) {
        linha.push(0);
    }
    matrizDinamica.push(linha);
}

console.log(matrizDinamica);

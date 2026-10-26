#!/usr/bin/node
const values = [];

if (process.argv.length >= 4) {
  for (let i = 2; i < process.argv.length; i++) {
    values.push(Number(process.argv[i]));
  }

  const result = [0, 0];
  values.forEach(element => {
    if (element > result[0]) {
      if (element > result[1]) {
        result[1] = result[0];
      }
      result[0] = element;
    } else if (element > result[1]) {
      result[1] = element;
    }
  });

  console.log(`${result[1]}`);
} else {
  console.log('0');
}

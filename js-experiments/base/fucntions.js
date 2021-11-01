import defaultFunc, { mysqrt } from './file_import.js';
import * as testImport from './file_import.js';

testImport.mysqrt(4);
mysqrt(5);
defaultFunc(5);

// Old format

const oldFormat = function (value) {
  return value;
};

// Simple format
function NewFormat(value) {
  return value;
}

// New arrow format
const square = (number) => number * number;
const sumOfSquares = (number) => square(number) * square(number);
const squareSumOfSquares = (number) => square(sumOfSquares(number));

const surfaceAreaCalculatorX2 = (radius) => {
  const result = 4 * 3.14 * radius * radius;
  return result * 2;
};

const abs = (num) => {
  if (num === 0 || num > 0) {
    return num;
  }
  return -num;
};

const getAbs = (num) => ((num >= 0) ? num : -num);

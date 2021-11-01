const num = 3;
let answer;

if (num === 1) {
  answer = 'One';
} else if (num === 2) {
  answer = 'Two';
} else {
  answer = 'Nothing';
}

// switch
switch (num) {
  case 1: // if (num === 1)
    answer = 'One';
    break;

  case 2: // if (num === 2)
    answer = 'Two';
    break;

  default:
    answer = 'Nothing';
    break;
}
// iteration
const factorial1 = (n) => {
  let result = 1;

  // initialization↓    condition↓     update↓
  for (let counter = 1; counter <= n; counter += 1) {
    result *= counter;
  }

  return result;
};

const factorial2 = (n) => {
  let counter = 1;
  let result = 1;

  while (counter <= n) {
    result *= counter;
    counter += 1;
  }

  return result;
};

let counter = 1;
for (;;) {
  if (counter <= n) break;
  // любой код
  counter += 1;
}

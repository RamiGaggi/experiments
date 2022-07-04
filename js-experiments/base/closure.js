const createPrinter = () => {
  const name = 'King';

  const ramil = () => {
    console.log(name);
  };

  return printName;
};

const myPrinter = createPrinter();
myPrinter(); // King

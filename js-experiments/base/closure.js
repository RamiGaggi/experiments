const createPrinter = () => {
  const name = 'King';

  const printName = () => {
    console.log(name);
  };

  return printName;
};

const myPrinter = createPrinter();
myPrinter(); // King

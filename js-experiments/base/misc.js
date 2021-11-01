const compare = (first, second) => {
  const firstCount = bigLettersCount(first);
  const secondCount = bigLettersCount(second);
  if (firstCount > secondCount) {
    return 1;
  } if (firstCount < secondCount) {
    return -1;
  }
  return 0;
};

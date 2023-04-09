#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(num => {
    if (searchElement === num) {
      count++;
    }
  });
  return count;
};

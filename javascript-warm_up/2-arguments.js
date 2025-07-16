#!/usr/bin/node

function checkForArgument (...arg) {
  if (arg.length === 0) {
    console.log('No argument');
  } else if (arg.length === 1) {
    console.log('Argument found');
  } else {
    console.log('Argument found');
  }
}

// Example usage:
checkForArgument(); // No argument
checkForArgument('test'); // Argument found
checkForArgument(1, 2, 3); // Arguments found

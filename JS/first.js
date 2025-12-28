function  factorial ( n ) {
   if (n == 0 ) {
     return  1 ;
  } else {
     return factorial(n - 1 ) * n;
  }
}

console.log(factorial(8))

let userInput = prompt("Enter passcode");

if (userInput === "123") {
    alert("Welcome to website");
} else {
    alert("Incorrect passcode, please try again");
}

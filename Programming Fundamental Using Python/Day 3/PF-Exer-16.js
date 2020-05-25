//Write a JavaScript program to find and display least common multiple of two whole numbers.
//Least Common Multiple of two numbers, say num1 and num2, is the smallest positive number that is divisible by both num1 and num2.


//PF-Exer-16

num1=5
num2=10

//Write your code here
if(num2>num1){
    i = num2
    while(i%num1!=0){
        i+=num2
    }
}
else {
    i=num1
    while(i%num2!=0){
        i+=num1
    }
}
console.log(i)

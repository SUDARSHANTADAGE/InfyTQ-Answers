//PF-Exer-12
//This verification is based on string match.
//Day 2
package main
import ("fmt")
func main(){
    //Write your program logic here
    var Num1 int = 3;
    var Num2 int = 4;
    var Num3 int = 1;
    if(Num1>Num3 && Num1>Num2){
        fmt.Println(Num1);
    }else if(Num2>Num1 && Num2>Num3){
        fmt.Println(Num2);
    }else{
        fmt.Println(Num3)
    }
}

//PF-Exer-8
//This verification is based on string match.

package main
import ("fmt")
func main(){
    var finalFee float32
    //Write your program logic here
    //Populate the variable: finalFee
    var marks float32= 70
    var percent float32 = marks/2
    var extrafees float32 = 1500
    var fees float32 = 25000
    var sc float32 = (fees * percent)/100
    finalFee = (fees - sc)+extrafees
     //Do not modify the below print statement for verification to work
     fmt.Println(finalFee) 
}

package main

import (
  "fmt" 
  "os"
  "strconv"
)

const MAX int = 1000000


func doit(a []int64, from int, to int, c chan int64) {
  fmt.Println("doing  ", from, "--  ", to)
  var i int64
  // TODO display a message of which portion of the array you are processing 
  for i = 0; i<int64(MAX);i++ {
    a[i] = i+1 
  }
  var sum int64
  sum = 0
  for j := from; j<= to;j++{
    sum += a[j]
  }
  c <- sum
  return
  // TODO define and initialize ito 0 an int64 variable
  // TODO in a for loop, traverse your portion of array, setting the values of 
  // TODO the items to the value of the index+1 (i.e. the item with index 27 will have
  // TODO value of 28), and cumulate the total in the variable
  // TODO send the resulting value to the channel c
}


func main(){
  // TODO define an array of size MAX of int64
  var array = [MAX]int64{}

  // TODO check the number of command line ruments, if not 2, display error
  if len(os.Args) != 2 {
    fmt.Println("usage: program <number-of-goroutines>")
    return
  }
  // TODO and terminate  -- you need the package os for that
  number_of_goroutines, err := strconv.Atoi(os.Args[1])
  if err != nil { //err not equal to a zero value (no error)
    fmt.Println("Wrong command line argument")
    return
  }
  if number_of_goroutines > MAX {
    fmt.Println("# of goroutines too big! It should be less than 1000000!")
    return
  }
  if number_of_goroutines <=0 {
    fmt.Println("# of goroutines too small! It should be greater than 0!")
    return
  }
  // TODO convert the second command line argument to number_of_goroutines
  // TODO you need the package strconv for that
  // TODO if the second command line argument is not a number, error message and
  // TODO terminate
  fmt.Println("number of goroutines = ",number_of_goroutines)
  slice := MAX/number_of_goroutines
  reminder := MAX % number_of_goroutines
  fmt.Println("slice = ",slice)
  // TODO if the second command line argument were a number, disoplay a message of'
  // TODO how many gooroutines is used
  // TODO compute the "slice" of the array for each goroutine
  // TODO and display it
  c := make(chan int64)
  var from int
  var to int
  var total_sum int64
  total_sum = 0
  for i:=0;i<number_of_goroutines;i++{
    if i == 0{
      from = 0
    }else{
      if reminder == 0{
        from = i*slice
        }else {from = i * slice + reminder}
    }
    to = (i+1) * slice + reminder -1
    go doit(array[0:],from,to,c)
  }
  for i:=0; i<number_of_goroutines;i++{
    total_sum += <- c
  }
  fmt.Println(total_sum)
  // TODO in a loop as long as there is a goroutine dispatched, dispatch the required 
  // TODO number of goroutines with the info, receive their result, and sume the result 
  // TODO together, and display the result
}

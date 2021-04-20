import os
import sys

from kotlin_compiler import program


def main() -> None:
    prog4 = 'int i; i = 5;'
    prog5 = '''
        int input_int(string name) {
            if (name != "") {
                print("Введите " + name + ": ");
            }
            return to_int(read());

            // bool a() { }
        }
        int input_int2(string name, int a, int name2) {
            if (name != "") {
                print("Введите " + name + ": ");
            }
            return "";
        }
    '''
    prog6 = '''
        var a : Int = 10
        var b : Int
        val c = 10
        if(a == 10) {
            println("a равно 10");
        }
    '''
    prog7 = '''
        fun func(a: Int, c: Int) : Double{
            var res = a*b
            return 
        }
    '''
    prog8 = '''
            val b = 1 .. 2  // false
            val c = 1 until 3 step 1 // true
            val d = 5 downTo 3  // true
        '''

    prog9 = '''
                for (i in seq) {
                    println(i);
                    println(2*i);
                }
                while(true) {
                    println("hello")
                }
                do {
                    println(1)
                    println(1)
                } while(true)
            '''
    prog10 = '''
            val numbers: Array<Array<Int>> = arrayOf(1, 2, 3, 4, 5)
    '''
    prog11 = '''
        fun factorial(n: Int) {
            if(n < 1){
                println("Incorrect input parameter")
                return
            }
            var result = 1;
            for(d in 1 .. n){
                result = d
            }
            println("Factorial of $n is equal $result")
        }
        '''

    program.execute(prog11)


if __name__ == "__main__":
    main()

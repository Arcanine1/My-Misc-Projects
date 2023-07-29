use std::io;
use std::time::Instant;

fn main() {

    //gets input
    let mut string_num: String = String::new();
    io::stdin().read_line(&mut string_num).unwrap();
    let mut num: i128 =string_num.trim().parse::<i128>().unwrap();

    //starts timer
    let now: Instant = Instant::now();

    //defines vector
    let mut primes: Vec<i128> = Vec::new();
    primes.push(2);

    let mut factor: i128=2;
    loop {
        //checks if factor is greater than number
        let root: i128 = ((num as f64).sqrt() as i128) + 1;
        if factor > root {
            break;
        }  

        //if factor is a divisor divivde else keep it as the same factor
        if num%factor ==0 {
            num=num/factor;
            print!("{}, ", factor);
        }
        else{
            factor = next_prime(&mut primes);
        }
    }

    print!("{} \n", num);

    //benchmarks
    let elapsed: std::time::Duration = now.elapsed();
    println!("Total Elapsed: {:.2?}", elapsed);

}

//creates vector of primes under square root (n)
fn next_prime(primes:&mut Vec<i128>) -> i128{

    let mut checking: i128 = primes.last().unwrap() +2;

    if checking==4{
        checking =3
    }

    let mut root: i128;
    let mut factor: i128 = primes[0];
    let mut boolean = true;

    let mut a =0;
    loop {

        root = ((checking as f64).sqrt() as i128) +1;
        while root > factor {

            if checking%factor ==0 {
                boolean=false;
                break;
            }
    
            a=a+1;
            factor=primes[a]
        }

        if boolean {
            primes.push(checking);
            return checking;
        }

        checking = checking +2;
        a=0;
        boolean=true;
        
    }

}

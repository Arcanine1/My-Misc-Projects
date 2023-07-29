use std::io;

fn main() {
    //gets input
    let mut string_num: String = String::new();
    io::stdin().read_line(&mut string_num).unwrap();
    let mut num: i128 =string_num.trim().parse::<i128>().unwrap();

    //gets primes vector
    let primes: Vec<i128> = primes_under_sqrt_n(num);

    let mut a: usize= 0;
    while a < primes.len() {
        //checks if factor is greater than number
        let factor: i128 =primes[a];
        if factor >= num {
            break;
        }  

        //if factor is a divisor divivde else keep it as the same factor
        if num%factor ==0 {
            num=num/factor;
            print!("{} \n", factor);
        }
        else{
            a=a+1;
        }


    }

    print!("{}", num);
}

//creates vector of primes under square root (n)
fn primes_under_sqrt_n(n: i128) -> Vec<i128>{
    let mut primes: Vec<i128> = Vec::new();
    primes.push(2);
    primes.push(3);

    let bigroot: i128 =  ((n as f64).sqrt() as i128) +1;
    let mut checking: i128 = 5;
    let mut root: i128 = ((checking as f64).sqrt() as i128) +1;
    let mut factor: i128 = 3;
    let mut boolean: bool = true;

    while checking< bigroot {

        while root > factor {

            if checking%factor == 0{
                boolean = false;
                break;
            }
            factor = factor +2;
        }

        if boolean {
            primes.push(checking)
        }

        factor =3;
        checking = checking+2;
        root = ((checking as f64).sqrt() as i128) +1;
        boolean = true;
    }

    primes
    
}

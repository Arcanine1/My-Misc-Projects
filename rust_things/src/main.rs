fn main() {
    
    let mut checking: i32 = 5;
    let mut factor: i32=3;
    let upper: i32 = 1000000;
    let mut prime: bool = true;

    while checking<upper {

        let root: i32    = (checking as f64).sqrt() as i32 + 1;

        while factor<root {
            if checking%factor==0 {
                prime = false
            }
            factor=factor+2
        }

        if prime {
            println!("{}", checking)
        }   

        factor =3;
        prime = true;
        checking = checking+2;
    }

}

use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("day1.txt")?;
    let reader = BufReader::new(file);
    let mut sm = 0;

    for line in reader.lines() {
        let sen = match line {
            Ok(sen) => sen,
            Err(e) => return Err(e),
        };
        let mut first_index = sen.len();
        let mut found = false;
        let mut last_index = 0;
        let mut tens = 0;
        let mut ones = 0;

        // let words = ["1","2","3","4","5","6","7","8","9","0"];
        // let vals = [1,2,3,4,5,6,7,8,9,0];
        let words = ["1","2","3","4","5","6","7","8","9","0","one","two","three","four","five","six","seven","eight","nine","zero"];
        let vals = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0];
        let mut iter = 0;
        for word in words {
            match sen.find(word) {
                Some(index) => {
                    if index < first_index {
                        first_index = index;
                        tens = iter;
                    }
                },
                None => {},
            };
            match sen.rfind(word) {
                Some(index) => {
                    if !found {
                        last_index = index;
                        ones = iter;
                        found = true;
                    }
                    else if index > last_index {
                        last_index = index;
                        ones = iter;
                    }
                },
                None => {},
            };
            iter += 1;
        }
        println!("sentence '{}' tens={}, ones={}", sen, vals[tens], vals[ones]);
        sm += vals[tens] * 10 + vals[ones];
    }
    println!("{}", sm);

    Ok(())
}
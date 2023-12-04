use std::io;
use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;

fn main() -> io::Result<()> {
    let f = File::open("sample.txt")?;
    let reader = BufReader::new(f);

    let mut finalsum = 0;

    for line in reader.lines() {
        let input = line?;
        let cards:Vec<&str>= input.split("|").collect();
        let winning = cards[1].split_whitespace().collect::<Vec<&str>>();
        let mycard:Vec<&str>= cards[0].split(":").collect();
        let mynums = mycard[1].split_whitespace().collect::<Vec<&str>>();

        let mut matchcount = 0;
        for val in winning.iter() {
            let intval = val.parse::<i32>().unwrap();
            for myval in mynums.iter() {
                let intmyval = myval.parse::<i32>().unwrap();
                if intmyval == intval {
                    matchcount += 1;
                }
            }
        }
        if matchcount > 0 {
            finalsum += i32::pow(2, matchcount - 1);
        }
    }
    println!("{}", finalsum);
    Ok(())
}

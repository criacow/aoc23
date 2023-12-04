use std::io;
use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;

fn main() -> io::Result<()> {
    let f = File::open("sample.txt")?;
    let reader = BufReader::new(f);

    let mut totalcards = 0;
    let mut cardcount: Vec<usize> = vec![0; 250];
    let mut linecount = 0;

    for line in reader.lines() {
        let input = line?;

        totalcards += cardcount[linecount] + 1;

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
            for val in (linecount + 1) .. (linecount + matchcount + 1) {
                cardcount[val] += cardcount[linecount] + 1;
            }
        }
        linecount += 1;
    }
    println!("{}", totalcards);
    Ok(())
}

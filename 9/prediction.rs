use std::io;
use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;

fn main() -> io::Result<()> {
    let f = File::open("test.txt")?;
    let reader = BufReader::new(f);

    let mut finalsum = 0;

    for line in reader.lines() {
        let input = line?;
        let readings = input.split_whitespace().collect::<Vec<&str>>();
        let mut read_vector = Vec::new();
        for val in readings.iter() {
          read_vector.push(val.parse::<i32>().unwrap());
        }
	let next_item = recurse_solution(read_vector.clone());	
        finalsum += next_item + read_vector[read_vector.len() - 1];
    }
    println!("{}", finalsum);
    Ok(())
}

fn recurse_solution(row: Vec<i32>) -> i32 {
    let mut sub_vector = Vec::new();
    for x in 1..row.len() {
       sub_vector.push(row[x] - row[x-1]);
    }
    let mut not_zero = 0;
    for x in &sub_vector {
       if x != &0 { not_zero = 1; }
    }
    if not_zero == 0 {
      return 0;
    } else {
      let downval = recurse_solution(sub_vector.clone());
      return downval + sub_vector[sub_vector.len() - 1];
    }
}   

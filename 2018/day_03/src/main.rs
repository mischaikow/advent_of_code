use std::fs;
use regex::Regex;

fn main() {
    let filename = "input.txt";

    let contents = fs::read_to_string(filename)
        .expect("Should have been able to read file.");

    let claims = contents; //.split("\n");

    let mut cloth = [[0; 1000]; 1000];
    
    let re = Regex::new(r"#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)").unwrap();
    let mut claims_vector = vec![];
    for (_, [id, top_left_i, top_left_j, size_i, size_j]) in re.captures_iter(&claims).map(|c| c.extract()) {
        claims_vector.push((top_left_i.parse::<usize>().expect("not a number?"),
                            top_left_j.parse::<usize>().expect("not a number?"),
                            size_i.parse::<usize>().expect("not a number?"),
                            size_j.parse::<usize>().expect("not a number?"),
                            id.parse::<u16>().expect("not a number?")))
    }

    for claim in claims_vector.clone() {
        for i in claim.0..claim.0+claim.2 {
            for j in claim.1..claim.1+claim.3 {
                cloth[i][j] += 1
            }
        }
    }

    let mut ans = 0;
    for i in 0..1000 {
        for j in 0..1000 {
            if cloth[i][j] > 1 {
                ans += 1;
            }
        }
    }

    println!("Part 1: {ans}");

    for claim in claims_vector {
        let mut test_claim = true;
        'one_claim: for i in claim.0..claim.0+claim.2 {
            for j in claim.1..claim.1+claim.3 {
                if cloth[i][j] != 1 {
                    test_claim = false;
                    break 'one_claim;
                }
            }
        }
        if test_claim {
            println!("Part 2: {}", claim.4);
            return
        }
    }
}

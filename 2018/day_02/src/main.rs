use std::fs;
use std::collections::HashMap;

fn main() {
    let filename = "input.txt";

    let contents = fs::read_to_string(filename)
        .expect("Should have been able to read file.");

    let serial_numbers = contents.split("\n");

    let mut two_count = 0;
    let mut three_count = 0;

    for serial in serial_numbers {
        let serial = serial.chars();
        let mut letter_counts: HashMap<char, u8> = HashMap::new();
        for a_char in serial {
            letter_counts.entry(a_char).and_modify(|counter| *counter += 1).or_insert(1);
        }

        let mut has_two = false;
        let mut has_three = false;
        for count in letter_counts.values() {
            if *count == 2 {
                has_two = true;
            }
            if *count == 3 {
                has_three = true;
            }
        }
        if has_two {
            two_count += 1;
        }
        if has_three {
            three_count += 1;
        }
    }

    println!("Part 1: {}", two_count * three_count);

    let mut serial_numbers = contents.split("\n");

    loop {
        let first = serial_numbers.next().expect("Out of serial numbers").chars();

        let comparators = serial_numbers.clone();
        for serial in comparators {
            let serial_chars = serial.chars();
            let mut delta_count = 0;
            let mut ans = String::from("");
            let first_instance = first.clone();
            for (basec, thisc) in first_instance.zip(serial_chars) {
                if basec == thisc {
                    ans.push(basec);
                } else {
                    delta_count += 1;
                }
            }
            if delta_count == 1 {
                println!("Part 2: {ans}");
                return
            }
        }
    }
}

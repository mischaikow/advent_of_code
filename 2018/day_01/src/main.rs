use std::fs;
use std::collections::HashSet;

fn main() {
    let filename = "input.txt";

    let contents = fs::read_to_string(filename)
        .expect("Should have been able to read file.");

    let freq_changes = contents.split("\n");

    let mut ans = 0;
    let mut seen_freq = HashSet::new();

    let mut has_looped = false;

    loop {
        for change in freq_changes.clone() {
            if change.len() > 0 {
                let change: i32 = change.trim().parse().expect("This is no number");
                ans += change;
                if seen_freq.contains(&ans) {
                    println!("Part 2: {ans}");
                    return
                } else {
                    seen_freq.insert(ans);
                }
            }
        }

        if !has_looped {
            println!("Part 1: {ans}");
            has_looped = true;
        }
    }
}

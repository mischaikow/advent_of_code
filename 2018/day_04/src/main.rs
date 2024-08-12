use std::fs;
use std::collections::HashMap;
use regex::Regex;

fn main() {
    let filename = "input.txt";
    let contents = fs::read_to_string(filename)
        .expect("Should have been able to read file."); 
    
    let re_entry = Regex::new(r"\[1518\-([0-9]{2})\-([0-9]{2}) ([0-9]{2}):([0-9]{2})\] (.*)").unwrap();
    let mut entries = vec![];
    for (_, [month, date, hour, minute, record]) in re_entry.captures_iter(&contents).map(|c| c.extract()) {
        entries.push((month.parse::<u16>().expect("not a number?"),
                      date.parse::<u16>().expect("not a number?"),
                      hour.parse::<u16>().expect("not a number?"),
                      minute.parse::<u16>().expect("not a number?"),
                      record))
    }

    entries.sort_by(|a, b| if a.0 != b.0 {
        a.0.cmp(&b.0)
    } else if a.1 != b.1 {
        a.1.cmp(&b.1)
    } else if a.2 != b.2 {
        a.2.cmp(&b.2)
    } else {
        a.3.cmp(&b.3)
    });

    let re_guard_check = Regex::new(r"Guard #(?<guard_id>[0-9]+).*").unwrap();
    let re_sleep_check = Regex::new(r"falls.*").unwrap();
    let re_wake_check = Regex::new(r"wakes.*").unwrap();

    let mut guards = HashMap::new();

    let mut current_guard: u16 = 0;
    let mut minute_start: u16 = 0;

    for log in entries.clone() {
        if re_guard_check.is_match(log.4) {
            current_guard = re_guard_check.captures(log.4).unwrap().name("guard_id").unwrap().as_str().parse::<u16>().expect("not a number?");
        } else if re_sleep_check.is_match(log.4) {
            minute_start = log.3;
        } else if re_wake_check.is_match(log.4) {
            let nap_time = log.3 - minute_start;
            guards.entry(current_guard).and_modify(|s| *s += nap_time).or_insert(nap_time);
        }
    }

    let mut max_guard: u16 = 0;
    let mut max_time: u16 = 0;
    for (guard, time) in guards.iter() {
        if *time > max_time {
            max_time = *time;
            max_guard = *guard;
        }
    }

    let mut guard_naps = HashMap::new();
    
    for log in entries {
        if re_guard_check.is_match(log.4) {
            current_guard = re_guard_check.captures(log.4).unwrap().name("guard_id").unwrap().as_str().parse::<u16>().expect("not a number?");
        } else if re_sleep_check.is_match(log.4) {
            minute_start = log.3;
        } else if re_wake_check.is_match(log.4) {
            if !guard_naps.contains_key(&current_guard) {
                guard_naps.insert(current_guard, vec![0; 60]);
            }
            guard_naps.entry(current_guard).and_modify(|nap_record| for i in minute_start..log.3 {
                nap_record[usize::from(i)] += 1;
            });
        }
    }

    let mut peak_guard = 0;
    let mut peak_nap_count = 0;
    let mut peak_nap_minute = 0;
    let mut part_one_time = 0;
    let mut part_one_max_nap = 0;
    for (guard_number, nap_record) in guard_naps.iter() {
        for i in 0..nap_record.len() {
            if nap_record[i] > peak_nap_count {
                peak_guard = *guard_number;
                peak_nap_count = nap_record[i];
                peak_nap_minute = i;
            }
            if *guard_number == max_guard && nap_record[i] > part_one_max_nap {
                part_one_max_nap = nap_record[i];
                part_one_time = i;
            }
        }
    }

    println!("Part 1: {}", u32::from(max_guard) * u32::try_from(part_one_time).expect("What??"));
    println!("Part 2: {}", u32::from(peak_guard) * u32::try_from(peak_nap_minute).expect("What part 2??"));
}
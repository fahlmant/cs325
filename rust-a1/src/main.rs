use std::cmp;

fn alg1(array: &[i32]) {

    let length = array.len() + 1;
    let mut max_num: i32 = 0;

    for x in 0..length {
        for y in x..length {
            let mut num: i32 = 0;
            for z in x..y {
                num = num + array[z];
                max_num = cmp::max(num, max_num);
            }
        }
    }

    println!("Alg 1, max num {}", max_num);
}

fn alg2(array: &[i32]) {
    
    let length = array.len() + 1;
    let mut max_num: i32 = 0;

    for x in 1..length {
        let mut num: i32 = 0;
        for y in x..length {
            num = num + array[y-1];
            max_num = cmp::max(num, max_num);
        }
    }

    println!("Alg 2, max num {}", max_num);
}

fn alg3(array: &[i32]) {
    
    let length = array.len();
    let mut max_num: i32 = 0;
    let mut num: i32 = 0;

    for x in 0..length {
        num = cmp::max(0, num+array[x]);
        max_num = cmp::max(num, max_num);
    }

    println!("Alg 3, max num {}", max_num);
}

fn main() {

    let array = [22, -27, 38, -34, 49, 40, 13, -44, -13, 28, 46, 7, -26, 42, 29, 0, -6, 35, 23, -37, 10, 12, -2, 18, -12, -49, -10, 37, -5, 17, 6, -11, -22, -17, -50, -40, 44, 14, -41, 19, -15, 45, -23, 48, -1, -39, -46, 15, 3, -32, -29, -48, -19, 27, -33, -8, 11, 21, -43, 24, 5, 34, -36, -9, 16, -31, -7, -24, -47, -14, -16, -18, 39, -30, 33, -45, -38, 41, -3, 4, -25, 20, -35, 32, 26, 47, 2, -4, 8, 9, 31, -28, 36, 1, -21, 30, 43, 25, -20, -42];
    alg1(&array);
    alg2(&array);
    alg3(&array);
}

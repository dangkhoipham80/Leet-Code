package main

func plusOne(digits []int) []int {
	carry := 1

	for i := len(digits) - 1; i >= 0; i-- {
		x := digits[i] + carry
		if x < 10 {
			digits[i] = x
			return digits
		} else {
			digits[i] = 0
			carry = 1
		}
	}

	// Nếu đến đây nghĩa là toàn bộ đều là 9
	if digits[0] == 0 {
		digits = append([]int{1}, digits...)
	}

	return digits
}

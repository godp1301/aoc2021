.PHONY: day1 all

day1:
	pytest ./aoc/day1/part1
	PYTHONPATH=. python ./aoc/day1/part1/main.py
	pytest ./aoc/day1/part2
	PYTHONPATH=. python ./aoc/day1/part2/main.py

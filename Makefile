.PHONY: day1 all

day1:
	pytest ./aoc/day1/am
	PYTHONPATH=. python ./aoc/day1/am/main.py
	pytest ./aoc/day1/pm
	PYTHONPATH=. python ./aoc/day1/pm/main.py

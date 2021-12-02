import requests


def get_puzzle(day):
    response = requests.get(url=f'https://adventofcode.com/2021/day/{day}/input',
                            cookies={'session': 'REDACTED'})
    return [n for n in response.text.split('\n') if n != '']

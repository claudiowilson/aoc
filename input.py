import urllib.request

def get_input(day):
    a_request = urllib.request.Request(f'https://adventofcode.com/2023/day/{day}/input')
    a_request.add_header("cookie", "session=53616c7465645f5f77991c9ab390f5571b6df08dbfe927fbdec046ebe3b4c63f34265308f0c395972bae1f4b7849022b780e6029923832b5877414bf0986fb0e")
    return urllib.request.urlopen(a_request).read().decode()

def get_split_input(day):
    inputs = get_input(day).split('\n')
    return list(filter(lambda x: len(x) > 0, inputs))


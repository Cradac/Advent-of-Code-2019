noun = 0
verb = 0
output = 0

while output != 19690720:
    f = open("Day2input.txt", "r")
    data = f.readline()
    data = list(map(int, data.split(',')))

    data[1] = noun
    data[2] = verb

    i = 0

    def add(first, second, location):
        data[location] = data[first] + data[second]

    def mult(first, second, location):
        data[location] = data[first] * data[second]

    while True:
        try:
            if data[i] == 1:
                add(data[i+1], data[i+2], data[i+3])
            elif data[i] == 2:
                mult(data[i+1], data[i+2], data[i+3])
            elif data[i] == 99:
                print(f"NOUN: {noun}, VERB: {verb} - VALUE: {data[0]}")
                output = data[0]
                break
            else:
                print("Something went wrong.")
                break
            i += 4

        except IndexError:
            print("IndexError, no value.")
            break
        finally:
            f.close()

    noun += 1
    if noun > 99:
        verb += 1
        noun = 0
        if verb > 99:
            print("NO VALUE FOUND")
            exit(0)

print(f"The value is: {100*(noun-1)+verb}.")
    
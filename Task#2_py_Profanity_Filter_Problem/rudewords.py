import string
rude_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]


def bleeper(word):
    strippedWord = word.strip(string.punctuation)
    if strippedWord.lower() in rude_words:
        word = word.replace(strippedWord, "*"*len(strippedWord))
    return word #


def check_line(line):
    rude_count = 0
    words = line.split(" ")
    line = ""
    for word in words:
        if word.strip(string.punctuation).lower() in rude_words:
            rude_count += 1
            print(f"Found rude word: {word}")
            line += bleeper(word)
        else:
            line += word
        line += " "
    return line, rude_count


def check_file(filename):
    with open(filename) as myfile:
        rude_count_total = 0 # with statement doesn't create a new scope for itself ::)) so this counter belongs to the function scope
        lines = []
        for line in myfile:
            line, rude_count_line = check_line(line.strip("\n"))
            lines.append(line)
            rude_count_total += rude_count_line
    
    fileWrite = open("bleeped_copy.txt", "w")
    for line in lines:
        fileWrite.write(line)
        fileWrite.write("\n")
    fileWrite.close()
    
    if rude_count_total == 0:
        print("Congratulations, your file has no rude words.")
        print("At least, no rude words I know.")


if __name__ == '__main__':
    check_file("story_1.txt")
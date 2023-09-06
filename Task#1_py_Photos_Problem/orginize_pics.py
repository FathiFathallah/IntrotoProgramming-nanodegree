import os


def extract_place_slice(filename):
    firstUnderScore = filename.find("_")
    filename = filename[firstUnderScore+1:]
    secondUnderScore = filename.find("_")
    return filename[:secondUnderScore]


def extract_place(filename):
    return filename.split("_")[1]


def make_place_directories(places):
    for place in places:
        os.mkdir(place)


def organize_photos(directory):
    os.chdir(directory)
    originals = os.listdir(".")
    places = []
    for original in originals:
        place = extract_place(original)
        if place not in places:
            places.append(place)
    make_place_directories(places)
    for original in originals:
        os.rename(os.path.join(".", original),
                  os.path.join(extract_place(original), original))


if __name__ == "__main__":
    organize_photos(input())

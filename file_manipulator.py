import os, shutil

def read_files(input_dir):
    files = os.listdir(input_dir)
    return files


def write_files(input_dir, output_dir, files):
    for i, image in enumerate(files):
        shutil.copy("{}/{}".format(input_dir, image), "{}pos261223-{}.png".format(output_dir, i))


if __name__ == "__main__":
    print(os.getcwd())
    # input_dir = "../../Pictures/Training images/Cars"
    # output_dir = "data/car/p/"
    input_dir = "../../Pictures/Training images/People"
    output_dir = "data/people/p/"

    files = read_files(input_dir)
    write_files(input_dir, output_dir, files)
    
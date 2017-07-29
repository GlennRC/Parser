import pandas as pd


def append_data_arff(data, category, path):
    with open(path, mode='a') as f:
        f.write("@DATA\n")
        for index, row in data.iterrows():
            f.write("{}, {}\n".format(",".join(map(str, row)), category))


def main():
    swing_csv_path = "swing2pos.csv"
    swing_arff_path = "swing2.arff"

    # TODO: Write a function that reads in column info from json
    column_names = ['frame', 'sacrum_x', 'sacrum_y']
    data = pd.read_csv(swing_csv_path, skipinitialspace=True, usecols=column_names)

    relation = "swing2_labeled"
    classes = ["running", "walking", "jumping", "varied"]

    with open(swing_arff_path, mode='w') as f:
        f.write("@RELATION {}\n".format(relation))

        for c in data.columns:
            if c == "frame":
                f.write("@ATTRIBUTE UNIQUE_ID REAL\n")
            else:
                f.write("@ATTRIBUTE {} REAL\n".format(c))

        f.write("@ATTRIBUTE class {}{}{}\n".format("{", ",".join(classes), "}"))


if __name__ == "__main__":
    main()

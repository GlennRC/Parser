import pandas as pd

# the classes should match the folder names that contain the training sets
def construct_csv_paths(parent, classes):



def main():
    import json
    config_path = "config.json"

    with open(config_path) as f:
        config_info = json.load(f)

    relation = config_info["relation"]
    classes = config_info["classes"]
    levels_path = config_info["levels"]["path"]

    with open(levels_path) as f:
        levels_data = json.load(f)

    for tier, desc in levels_data:
        output = "{}_{}.arff".format(relation, tier)

        columns = []
        for j in desc["joint"]:
            for a in desc["attr"]:
                columns.append("{}_{}".format(j, a))

        with open(output, mode='w') as f:
            f.write("@RELATION {}\n".format(relation))

            for c in columns:
                if c == "frame":
                    f.write("@ATTRIBUTE UNIQUE_ID REAL\n")
                else:
                    f.write("@ATTRIBUTE {} REAL\n".format(c))

            f.write("@ATTRIBUTE class {}{}{}\n".format("{", ",".join(classes), "}"))


        with open(path, mode='a') as f:
            for p, cl in input_info:
                m_data = pd.read_csv(p, skipinitialspace=True, usecols=columns)
                f.write("@DATA\n")
                for index, row in data.iterrows():
                    f.write("{},{}\n".format(",".join(map(str, row)), category))




if __name__ == "__main__":
    main()

import pandas as pd


def main():
    import json
    import glob
    config_path = "config.json"

    # read in the config file
    with open(config_path) as f:
        config_info = json.load(f)
        relation = config_info["relation"]
        classes = config_info["classes"]
        levels_path = config_info["levels"]["path"]
        parent = config_info["parent"]

    # Get all csv file paths
    input_files = {}
    for c in classes:
        input_files.update({c: glob.glob("./{}/{}/*.csv".format(parent, c))})

    # Load in the tier data to generate columns
    with open(levels_path) as f:
        levels_data = json.load(f)

    # Write an arff file for each tier
    for tier, desc in levels_data.iteritems():
        output = "{}_{}.arff".format(relation, tier)

        # Generate the columns which depends on the current tier
        columns = []
        for j in desc["joint"]:
            for a in desc["attr"]:
                columns.append("{}_{}".format(j, a))

        with open(output, mode='w') as f:
            f.write("@RELATION {}_{}\n".format(relation,tier))

            f.write("@ATTRIBUTE UNIQUE_ID NUMERIC\n")
            for c in columns:
                f.write("@ATTRIBUTE {} NUMERIC\n".format(c))

            f.write("@ATTRIBUTE class {}{}{}\n".format("{", ",".join(classes), "}"))

            count = 0
            for cl, files in input_files.iteritems():
                for i in files:
                    m_data = pd.read_csv(i, skipinitialspace=True, usecols=columns)
                    f.write("@DATA\n")
                    for index, row in m_data.iterrows():
                        f.write("{},{},{}\n".format(count, ",".join(map(str, row)), cl))
                        count += 1


if __name__ == "__main__":
    main()

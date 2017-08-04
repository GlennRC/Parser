import pandas as pd
import json
import glob
import argparse as ap


def main():
    parser = ap.ArgumentParser()
    parser.add_argument("config_path")
    args = parser.parse_args()

    # read in the config file
    with open(args.config_path) as f:
        info = json.load(f)
        config = info["config"]
        tiers = info["tiers"]
        relation = config["relation"]
        classes = config["classes"]
        parent_in = config["input"]
        parent_out = config["output"]

    # Get all csv file paths
    input_files = {}
    for c in classes:
        input_files.update({c: glob.glob("./{}/{}/*.csv".format(parent_in, c))})

    # Write an arff file for each tier
    for tier, desc in tiers.items():
        output = "{}/{}_{}.arff".format(parent_out, relation, tier)

        # Generate the columns which depends on the current tier
        columns = []
        for j in desc["joint"]:
            for a in desc["attr"]:
                columns.append("{}_{}".format(j, a))

        # begin writing the arff file
        with open(output, mode='w') as f:
            f.write("@RELATION {}_{}\n".format(relation,tier))

            f.write("@ATTRIBUTE UNIQUE_ID NUMERIC\n")
            for c in columns:
                f.write("@ATTRIBUTE {} REAL\n".format(c))

            f.write("@ATTRIBUTE class {}{}{}\n".format("{", ",".join(classes), "}"))

            # write the data for each file
            # count represents the unique_id
            f.write("@DATA\n")
            count = 0
            for cl, files in input_files.items():
                for i in files:
                    m_data = pd.read_csv(i, skipinitialspace=True, usecols=columns)
                    for _, row in m_data.iterrows():
                        f.write("{},{},{}\n".format(count, ",".join(map(str, row)), cl))
                        count += 1


if __name__ == "__main__":
    main()

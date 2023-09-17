def get_data(type_of_data):
    with open("helpers/{}.txt".format(type_of_data), "r") as data:
        lines = data.readlines()

        aggregated_data = []

        for line in lines:
            aggregated_data.append(line.replace("\n", ''))
        print(aggregated_data)

    return aggregated_data



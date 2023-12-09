if __name__ == '__main__':
    with open('input') as reader:
        lines = reader.readlines()

        predicted_part_one = []
        predicted_part_two = []
        for line in lines:
            history = list(map(int, line.strip().split(' ')))
            sequences = [history]

            while set(sequences[-1]) != {0}:
                sequences.append([ sequences[-1][i+1] - sequences[-1][i] for i in range(len(sequences[-1]) - 1) ])
            
            sequences[-1].append(0)
            for i in range(len(sequences) - 1, 0, -1):
                sequences[i-1].append(sequences[i-1][-1] + sequences[i][-1])
            
            sequences[-1].insert(0, 0)
            for i in range(len(sequences) - 1, 0, -1):
                sequences[i-1].insert(0, sequences[i-1][0] - sequences[i][0])

            predicted_part_one.append(sequences[0][-1])
            predicted_part_two.append(sequences[0][0])

        print(sum(predicted_part_one))
        print(sum(predicted_part_two))
import numpy as np



def line2bit_array(line):
    # convert string in numpy array seperated by character 
    return np.array([int(number) for number in line.strip()])


# Main function
def main(fn: str) -> None:
    
    with open(fn, 'r') as fp:

        # convert input in numpy array
        ff = False
        for line in fp:
            bit_array = line2bit_array(line=line)
            if not ff:
                report = bit_array
                ff = True
            else:
                report = np.vstack([report, bit_array])

        # constants
        _, n_bits = report.shape

        # iterate through the report columns and 
        # cut out all rows with the most common bit value
        # the iteration process will be stopped if only one 
        # row in subreport remains  
        sub_report = np.copy(report)
        oxy_gen_rating_bin = []
        for n in range(n_bits):

            idx_ones = np.where(sub_report[:, n] > 0)[0]
            idx_zeros = np.where(sub_report[:, n] == 0)[0]

            if idx_ones.shape[0] >= idx_zeros.shape[0]:
                sub_report = sub_report[idx_ones]
                oxy_gen_rating_bin.append(1)
            else:
                sub_report = sub_report[idx_zeros]
                oxy_gen_rating_bin.append(0)

            if sub_report.shape[0] == 1:
                oxy_gen_rating_bin = list(sub_report[0])
                break

        
        # same procedure as before but cut out the rows with 
        # the least common bit value 
        sub_report = np.copy(report)
        co2_scrubber_rating_bin = []
        for n in range(n_bits):

            idx_ones = np.where(sub_report[:, n] > 0)[0]
            idx_zeros = np.where(sub_report[:, n] == 0)[0]

            if idx_ones.shape[0] < idx_zeros.shape[0]:
                sub_report = sub_report[idx_ones]
                co2_scrubber_rating_bin.append(1)
            else:
                sub_report = sub_report[idx_zeros]
                co2_scrubber_rating_bin.append(0)

            if sub_report.shape[0] == 1:
                co2_scrubber_rating_bin = list(sub_report[0])
                break

        co2_scrubber_rating_dec = 0
        for digit in co2_scrubber_rating_bin:
            co2_scrubber_rating_dec = (co2_scrubber_rating_dec << 1) | digit

        oxy_gen_rating_dec = 0
        for digit in oxy_gen_rating_bin:
            oxy_gen_rating_dec = (oxy_gen_rating_dec << 1) | digit

        print(f'Oxygen generator rating: {oxy_gen_rating_bin} = {oxy_gen_rating_dec}')
        print(f'CO2 scrubber rating:     {co2_scrubber_rating_bin} = {co2_scrubber_rating_dec}')
        print(f'Puzzle result: {co2_scrubber_rating_dec * oxy_gen_rating_dec}')



if __name__ == '__main__':
    
    file_name = '03.txt'
    main(file_name)

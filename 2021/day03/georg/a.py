import numpy as np


def line2bit_array(line: str) -> np.ndarray: 
    # convert string in numpy array seperated by character
    return np.array([int(number) for number in line.strip()], dtype=np.float32)


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

        _, n_bits = report.shape 

        gamma_rate_dec = 0
        gamma_rate_bin = np.zeros(n_bits, dtype=np.int8)
        
        epsilon_rate_dec = 0
        epsilon_rate_bin = np.zeros(n_bits, dtype=np.int8)

        # calculate sum of all rows and 
        # compare sum with report length to get most common bits 
        n_ones = np.sum(report, axis=0)
    
        gamma_rate_bin[n_ones > report.shape[0] // 2] = 1
        epsilon_rate_bin[n_ones <= report.shape[0] // 2] = 1

        # convert binary array to decimal number
        for i in range(n_bits):
            gamma_rate_dec = (gamma_rate_dec << 1) | gamma_rate_bin[i]
            epsilon_rate_dec = (epsilon_rate_dec << 1) | epsilon_rate_bin[i]

        print(f'gamma rate: {gamma_rate_dec}')
        print(f'epsilon rate: {epsilon_rate_dec}')
        print(f'Puzzle result: {gamma_rate_dec * epsilon_rate_dec}')


if __name__ == '__main__':
    
    file_name = '03.txt'
    main(file_name)

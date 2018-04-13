
import sys

import parser
import commands
import code


if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2] #should be optional

    output_file = open(output_file, 'w') 

    with open(input_file, 'r') as f:
        for line in f:
            
            #parse line
            parsed_object = parser.parse(line)

            #Look up corresponding code
            if not isinstance(parsed_object,commands.Comment):
                
            
            #Write to the file
                coded_instruction = code.code(parsed_object)
                print(coded_instruction)
            #output_file.write(parsed_object)

    output_file.close()

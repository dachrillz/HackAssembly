
import sys

import parser
import commands
import code
import symbol_table


def run(first_pass = True, st = None):
    
    if first_pass:
        st = symbol_table.symbol_table()

    input_file = sys.argv[1]
    output_file = sys.argv[2] #should be optional
    output_file = open(output_file, 'w') 

    with open(input_file, 'r') as f:
        for line in f:
            
            if first_pass:
                current_line = parser.parse(line, st, first_pass)


            else:
                #parse line
                parsed_object = parser.parse(line, first_pass)

                #Look up corresponding code
                if not isinstance(parsed_object,commands.Comment):    
                
                #Write to the file
                    coded_instruction = code.code(parsed_object, st)
                    output_file.write(coded_instruction + '\n')

    output_file.close()

    if first_pass:
        run(first_pass=False, st = st)


if __name__ == '__main__':
    run()


#! /bin/python3

# Appending parent directory to the path
import sys, os
sys.path.append( os.path.dirname( os.path.realpath(__file__) ) )

# Import ListHandler
from ListHandler import ListHandler

# Import base64 table from lib/base64_list.py
from base64_list import base64_table

# Import base64 table
table = base64_table


class Encoder:

    def __init__(self, string=None, desired_chars=None, all_chars=False):

        global table

        self.string    = string if string else sys.exit(1)
        self._result  = {}
        desired_chars += ";\\&=+$, <>}{][@'\""

        # Create a list of characters that should be encoded.
        self.list = ListHandler(self.string, desired_chars, all_chars).get_list()
        

        self._result[self.string] = {}
        temp_result = {
                        'hex': '',
                        'bin': '',
                        'url': '',
                        'html_dec': '',
                        'html_hex': '',
                        'unicode': '',
        }

        for char in self.string:

            if char in self.list:

                html_template = '&#_TEMP_;'
                unicode_template = r'\u_TEMP_'

                # Hex value of current character
                x = self.char2hex(char)

                temp_result['hex']      += x
                temp_result['bin']      += self.hex2bin(x[0]) + self.hex2bin(x[1])
                temp_result['url']      += f'%{x}'
                temp_result['html_dec'] += html_template.replace( '_TEMP_', str(self.char2dec(char)) )
                temp_result['html_hex'] += html_template.replace( '_TEMP_', f'x{x}' )
                temp_result['unicode']  += unicode_template.replace( '_TEMP_', x.zfill(4) )

            else:
                # Hex value of current character
                x = self.char2hex(char)

                temp_result['hex']      += x
                temp_result['bin']      += self.hex2bin(x[0]) + self.hex2bin(x[1])
                temp_result['url']      += char
                temp_result['html_dec'] += char
                temp_result['html_hex'] += char
                temp_result['unicode']  += char


            self._result[self.string] = temp_result.copy()


        # Base64 encoding
        self.base64()


    # Return decimal value of character
    def char2dec(self, char):
        return ord(char)


    # Return hex value of character
    def char2hex(self, char):
        return str( hex( self.char2dec(char) )[2:] )


    # Return binary value of hexadecimal number
    def hex2bin(self, x):
        return str( bin( int(x, base=16) )[2:].zfill(4) )


    # Implementation of Base64 encoding based on rfc4648
    def base64(self):

        """
             If Base64 encoded string does not exist,
            perform encoding; otherwise return encoded result
        """
        for line in self._result:

            base64 = ''
            binary = self._result[line]['bin']

            # Padding with 0
            remainer = len(binary) % 6
            if remainer != 0:
                zeros = (6 - remainer) * '0'
                binary += zeros

            """
                # Spilt into 6-bit binary group
                # Calculate decimal value of each binary number in six_bit_group
                # Find the number of equal signs (=) that will be appended at the end of base64.
            """
            six_bit_group = [ binary[i:i+6] for i in range(0, len(binary), 6) ]
            decimal_values = [ str(int(i, base=2)) for i in six_bit_group ]
            remainer = len(decimal_values) % 4

            # Mapping decimal number to its standard format
            for dec in decimal_values:
                base64 += table[ dec ]

            # Padding with equal sign (=)
            if remainer != 0:
                base64 += (4 - remainer) * '='

            self._result[line]['base64'] = base64


    # Getter method
    def get_result(self):
        return self._result

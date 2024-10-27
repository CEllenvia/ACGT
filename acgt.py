"""
This module will  transforms binary data into 4 printable characters.
As the name of the project, now only support the hardcoded characters, a.k.a the A, C, G & T.
May add the function to custom, but will at some indeterminate moment.
"""

from textwrap import wrap

class acgt:

    def __init__(self,inp) -> None:
        self.inp = inp
        pass

    def encode(self):
        # Convert the imported thing into string-stored binary so can divided into 2 bit
        bins = format(int(self.inp.encode().hex(), base=16), 'b')
        print(bins)
        # Transform it every 2 bit
        in_lis = wrap(bins, width=2)
        out_lis = []
        for bin in in_lis:
            if bin == '00':
                out_lis.append("A")
            elif bin == '01':
                out_lis.append("C")
            elif bin == '10':
                out_lis.append("G")
            elif bin == '11':
                out_lis.append("T")
            else:
                return 1
        # give output
        out =  ''.join(out_lis)
        return out
    
    def decode(self):
        # Transform the imported thing every 1 bit
        in_lis = wrap(self.inp, width=1)
        out_lis = []
        for bin in in_lis:
            if bin == 'A':
                out_lis.append("00")
            elif bin == 'C':
                out_lis.append("01")
            elif bin == 'G':
                out_lis.append("10")
            elif bin == 'T':
                out_lis.append("11")
            else:
                return 1
        # Convert the long binary into utf-8
        out_raw =  ''.join(out_lis)
        out = bytes.fromhex('%x' % int(out_raw, 2)).decode('utf-8')
        return out
    

        

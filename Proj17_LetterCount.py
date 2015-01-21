"""
Project Euler 17
================================================================
If the numbers 1 to 5 are written out in words: one, two, three,
four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used
in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342
(three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of
"and" when writing out numbers is in compliance with
British usage.
"""

ones_track = {
                '0'   :0,
                '1'   :3,
                '2'   :3,
                '3'   :5,
                '4'   :4,
                '5'   :4,
                '6'   :3,
                '7'   :5,
                '8'   :5,
                '9'   :4,
                'and' :3}
teens_track = {
                '10'  :3,
                '11'  :6,
                '12'  :6,
                '13'  :8,
                '14'  :8,
                '15'  :7,
                '16'  :7,
                '17'  :9,
                '18'  :8,
                '19'  :8}

tens_track = {
                '0'  :0,
                '2'  :6,
                '3'  :6,
                '4'  :5,
                '5'  :5,
                '6'  :5,
                '7'  :7,
                '8'  :6,
                '9'  :6,
                'hundred' :7,
                'thousand':8}

def CountLetters(ones_track, teens_track, tens_track):
    letter_count = 0

    for i in xrange(1,1000):
        #print i
        current_number = list(str(i))

        if len(current_number) == 1:
            letter_count += ones_track[str(i)]

        elif len(current_number) >= 2:
            #import pdb; pdb.set_trace()
            if int(''.join(current_number[-2:])) in range(10,20):
                letter_count += teens_track[''.join(current_number[-2:])]

            else:
                #import pdb; pdb.set_trace()
                letter_count += tens_track[current_number[-2]]
                letter_count += ones_track[current_number[-1]]

            if len(current_number) > 2:
                letter_count += ones_track[current_number[-3]]
                letter_count += tens_track['hundred']
                if ''.join(current_number[-2:]) != '00':
                    letter_count += ones_track['and']

    letter_count += tens_track['thousand']
    letter_count += ones_track['1']

    print letter_count

CountLetters(ones_track, teens_track, tens_track)
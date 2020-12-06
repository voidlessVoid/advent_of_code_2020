from misc_hacki import misc
import numpy as np
import pandas as pd

class BinSeating:

    def __init__(self,
                 b_pass_ls,
                 rows,
                 cols,
                 ):
        self.b_pass_ls = b_pass_ls
        self.rows = rows
        self.cols = cols

    def seat_ID(self, b_pass):

        b_pass = list(b_pass)
        region, seat = b_pass[:-3], b_pass[-3:]

        def bin_divide(char_ls, num, upper_half):
            b_pass_index = 0
            seat_index = []
            seats_ls = np.arange(
                start=0,
                stop=num+1,
                step=1,
                dtype=int
            ).tolist()
            while b_pass_index <= len(char_ls)-1:
                seat_index = int(
                    np.ceil(
                        np.divide(
                            seats_ls.index(seats_ls[-1])
                            ,2
                        )
                    )
                )

                if char_ls[b_pass_index] == upper_half:
                    seats_ls = seats_ls[seat_index:]
                else:
                    seats_ls = seats_ls[:seat_index]

                b_pass_index += 1

            if seats_ls == []:
                seats_ls = np.nan

            return seats_ls


        row_num = bin_divide(
            char_ls=region,
            num=self.rows,
            upper_half='B'
        )
        col_num = bin_divide(
            char_ls=seat,
            num=self.cols,
            upper_half='R'
        )
        seat = np.multiply(row_num, self.cols+1)+col_num


        return {
            'row' : row_num[0],
            'col' : col_num[0],
            'seat': seat[0]
        }

    def ID_ls(self):

        return [self.seat_ID(b_pass=i) for i in self.b_pass_ls]


f_name = 'puzzle_input'
#f_name = 'test_puzzle'
in_ls = misc.load_input_to_list(f_name)
row_n = 127
col_n = 7
seat_ID_ls = BinSeating(
    b_pass_ls=in_ls,
    rows=row_n,
    cols=col_n
).ID_ls()

# noinspection PyTypeChecker
def extract_seat_info(ID_ls, cols):

    cols += 1
    seat_ID_df = pd.DataFrame(ID_ls)
    seats = seat_ID_df['seat']
    plane_seats = np.arange(
        start = cols, stop=max(seats)+1, step = 1)
    empty_seats = sorted(
        set(plane_seats)-set(seats)
    )
    missing_seats = []
    for i in empty_seats:
        j = 1
        while (i-j)%cols != 0: # module
            import random
            j = random.randint(0, 7)
        missing_seats.append([int((i-j)/cols), j, i])

    missing_seats_df = pd.DataFrame(
        missing_seats,
        columns=['row', 'col', 'seat']
    )
    own_seat = missing_seats_df.query('row >10 and row <100')
    all_seats = seat_ID_df.append(missing_seats_df)

    return {
        'empty_seats' : missing_seats_df,
        'plane_seats' : all_seats.sort_values(by=['seat']),
        'own_seat_ID' : own_seat['seat'],
    }


seats = extract_seat_info(
    ID_ls=seat_ID_ls,
    cols=col_n
)

plane_seats = seats['plane_seats']
own_seat_ID = seats['own_seat_ID'].values[0]

print(own_seat_ID, plane_seats[plane_seats['seat'].between(own_seat_ID-1,own_seat_ID+1)])

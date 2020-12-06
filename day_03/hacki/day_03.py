from misc_hacki import misc
import numpy as np

in_ls = misc.load_input_to_list(
    misc.path_to_dir('puzzle_input')
)

toboggan_slope = {
    'right': [1, 3, 5, 7, 1],
    'down': [1, 1, 1, 1, 2]
}


def slide(
        geology,
        horizontal,
        vertical
):
    tree_count = 0
    tree_index = 0
    v_down = np.arange(
        start=0,
        stop=len(geology),
        step=vertical
    ).astype(int)

    for i in v_down:

        tree_line = geology[i]

        if tree_line[
            tree_index % len(tree_line)
        ] == '#':  # thanks for the module hint Gerrit!!!
            tree_count += 1
        tree_index += horizontal

    return tree_count


tree_count_ls = []

for r, d in zip(
        toboggan_slope['right'],
        toboggan_slope['down']
):
    tree_count_ls.append(
        slide(
            geology=in_ls,
            horizontal=r,
            vertical=d
        )
    )

print(
    np.prod(
        tree_count_ls
    )
)

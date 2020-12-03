# -*- coding: utf-8 -*-
# Author: redTribune
# License: MIT
# Language: julia
#
# This code was created for the 'Advent Of Code' advent challenge 2020. Please feel free to use or modify it.
# I can NOT in any way guarantee that it is doing what it was supposed to do. Or even running... XD
##############################################################################################################
##############################################################################################################

using DelimitedFiles

function treeRadar(forest, lc, cc)
    trees = 0
    l = 1
    c = 1
    while l <= length(forest)
        if string(forest[l][c]) == "#"
            trees += 1
        end
        l += lc
        c += cc
        if c > length(forest[1])
            c = c - length(forest[1])
        end
    end
    return trees
end

forest = open("input.txt") do file
    readdlm(file)
end

answer1 = treeRadar(forest, 1, 3)

slopes = [[1,1],[1,3],[1,5],[1,7],[2,1]]

answer2 = 1
for run in slopes
    global answer2
    answer2 *= treeRadar(forest, run[1], run[2])
end

println(answer1)
println(answer2)

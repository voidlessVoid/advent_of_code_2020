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
using StatsBase

groups = String[]
pssngrs = Int64[]
oldln = ""
idx = 0

qst = open("input.txt") do file

for ln in eachline(file)
global oldln, idx

	if ln == ""
    push!(groups, oldln)
    push!(pssngrs, idx)
    oldln = ""
    idx = 0
    else
    idx += 1    
	oldln = oldln * ln
    end

end

push!(groups, oldln)
push!(pssngrs, idx)
   
y = Int64[]
yall = 0
cnt = 1

for ans in groups
note = countmap(ans)
push!(y, length(note))

	for q in keys(note)
	
		if note[q] == pssngrs[cnt]
		yall += 1
		end	
			
	end	

cnt += 1	
end

#############
sol1 = sum(y)
sol2 = yall
#############

print("Answer 1: ")
println(sol1)
print("Answer 2: ")
print(sol2)

end


using CSV
using DataFrames
using PyPlot

EigenData = DataFrame!(CSV.File("EigenData.csv"));

for j=1:4
	Min_EigenData = minimum(EigenData[:,j+2]);
	Max_EigenData = maximum(EigenData[:,j+2]);
	figure(figsize=(5,5))
	#grid("on")
	axis("equal")
	title("EigenFrequencies $j")
	for i=1:size(EigenData)[1]
		ColorScale = Int(floor(99*(EigenData[i,j+2]-Min_EigenData)/(Max_EigenData-Min_EigenData)));
		ColorCode = string("#",ColorScale,ColorScale,ColorScale);
		scatter(EigenData[i,1],EigenData[i,2],s=9000*0.015,marker="s",color=ColorCode)
	end
	savefig("EigenFrequencies_$j.png")
end


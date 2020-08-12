using CSV
using DataFrames
using PyPlot

EigenData = DataFrame!(CSV.File("EigenData.csv"));

# Parameters
a1 = 0.15;
a2 = 0.30;
a3 = 0.25;
cell = 0.015;
pose = 1;
PicSize = 40;

# Polt
for j=1:4
	Min_EigenData = minimum(EigenData[:,j+2]);
	Max_EigenData = maximum(EigenData[:,j+2]);
	figure(figsize=(PicSize,PicSize))
	#grid("on")
	axis("equal")
	title("EigenFrequencies $j")
	for i=1:size(EigenData)[1]
		ColorScale = Int(floor(80*(EigenData[i,j+2]-Min_EigenData)/(Max_EigenData-Min_EigenData)));
		ColorScaleString = string(ColorScale, base=10, pad=2);
		ColorCode = string("#",ColorScaleString,ColorScaleString,ColorScaleString);
		scatter(EigenData[i,1],EigenData[i,2],s=3500*PicSize*cell,marker="s",color=ColorCode);
		EigenFreq = EigenData[i,j+2];
		annotate("$i\n$EigenFreq", xy=(EigenData[i,1],EigenData[i,2]),ha="center",va="center",color="white",fontsize="x-small");
	end
	#plot( [0 EigenData[pose,1] ], [a1 EigenData[pose,2] ])
	savefig("EigenFrequencies_$j.png")
end

print("*************************************************\n");
print("*                  Finished                     *\n");
print("*************************************************\n");

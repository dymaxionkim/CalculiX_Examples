###########################################
#
# Eigenmodes for Industrial Robot Manipulator
# 20200806
# Dymaxion.kim@gmail.com
#
###########################################

# Parameters
a1 = 0.15;
a2 = 0.30;
a3 = 0.25;
cell = 0.015;

# Domain
J2 = [0.00 a1;];
Maxi = Int(floor((a2+a3)/cell));
Maxj = Int(floor((a1+a2+a3)/cell));
J5 = zeros(Maxi*Maxj,2);
global count = 1;
for i=1:Maxi
	tempX = i*cell;
	for j=1:Maxj
		tempY = j*cell;
	    temp = 1-(((tempX-J2[1])^2+(tempY-J2[2])^2-a2^2-a3^2)/(2*a2*a3))^2;
		if temp>0.0
			J5[count,1] = tempX;
			J5[count,2] = tempY;
			global count = count+1;
		end
	end
end
J5 = J5[1:count-1,:];

# IK, FK
# http://www.sml.ee.upatras.gr/UploadedFiles/InverseKinematics.pdf
ANGLE = zeros(size(J5));
J3 = zeros(size(J5));
J5E = zeros(size(J5));
for i=1:size(J5)[1]
	# IK
	J5E[i,1] = J5[i,1]-J2[1];
	J5E[i,2] = J5[i,2]-J2[2];
    cos_theta3 = (J5E[i,1]^2 + J5E[i,2]^2 - a2^2 - a3^2)/(2*a2*a3);
   	sin_theta3 = -sqrt(1-cos_theta3^2);
    beta = atan(a3*sin_theta3/(a2+a3*cos_theta3));
    gamma = atan(J5E[i,2]/J5E[i,1]);
    ANGLE[i,1] = gamma - beta;
	ANGLE[i,2] = acos(cos_theta3);
	# FK
    J3[i,1] = J2[1]+a2*sin(ANGLE[i,1]-pi/2);
    J3[i,2] = J2[2]+a2*cos(ANGLE[i,1]-pi/2);
    # FEM
    POSTURE = i;
    ANGLE2 = ANGLE[i,1]-pi/2;
    ANGLE3 = ANGLE[i,2]-pi/2;
    J2X = J2[1];
    J2Z = J2[2];
    J3X = J3[i,1];
    J3Z = J3[i,2];
    # FEM
    command=`./robot.sh $POSTURE $ANGLE2 $ANGLE3 $J2X $J2Z $J3X $J3Z`;
    run(command);
end

# EigenValues
function ReadEigenData(FileName)
	f = open(FileName);
	EigenData = readlines(f)
	EigenData = EigenData[8:11];
	for i=1:length(EigenData)
		EigenData[i] = SubString(EigenData[i],43,55)
	end
	EigenData = parse.(Float64,EigenData);
	EigenData = EigenData'
	close(f);
	return EigenData
end

EigenData = zeros(size(J5)[1],6);
for i=1:size(EigenData)[1]
	EigenData[i,1] = J5[i,1];
	EigenData[i,2] = J5[i,2];
	for j=1:4
		EigenData[i,j+2] = ReadEigenData("$i/eigen.dat")[j];
	end
end

# Save
using CSV, DataFrames
CSV.write("EigenData.csv",  DataFrame(EigenData), writeheader=false);

print("*************************************************\n");
print("*                  Finished                     *\n");
print("*************************************************\n");

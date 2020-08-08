#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.4.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'./')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
robot = geompy.ImportSTEP("../robot.stp", False, True)
[L2,L1,L3] = geompy.ExtractShapes(robot, geompy.ShapeType["SOLID"], True)
FIX = geompy.CreateGroup(L1, geompy.ShapeType["FACE"])
geompy.UnionIDs(FIX, [45])
L1_MASTER = geompy.CreateGroup(L1, geompy.ShapeType["FACE"])
geompy.UnionIDs(L1_MASTER, [99])
L2_SLAVE = geompy.CreateGroup(L2, geompy.ShapeType["FACE"])
geompy.UnionIDs(L2_SLAVE, [71])
L2_MASTER = geompy.CreateGroup(L2, geompy.ShapeType["FACE"])
geompy.UnionIDs(L2_MASTER, [73])
L3_SLAVE = geompy.CreateGroup(L3, geompy.ShapeType["FACE"])
geompy.UnionIDs(L3_SLAVE, [63])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( robot, 'robot' )
geompy.addToStudyInFather( robot, L2, 'L2' )
geompy.addToStudyInFather( robot, L1, 'L1' )
geompy.addToStudyInFather( robot, L3, 'L3' )
geompy.addToStudyInFather( L1, FIX, 'FIX' )
geompy.addToStudyInFather( L1, L1_MASTER, 'L1_MASTER' )
geompy.addToStudyInFather( L2, L2_SLAVE, 'L2_SLAVE' )
geompy.addToStudyInFather( L2, L2_MASTER, 'L2_MASTER' )
geompy.addToStudyInFather( L3, L3_SLAVE, 'L3_SLAVE' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

NETGEN_1D_2D_3D = smesh.CreateHypothesis('NETGEN_2D3D', 'libNETGENEngine.so')
try:
  pass
except:
  print('ExportUNV() failed. Invalid file name?')
try:
  pass
except:
  print('ExportUNV() failed. Invalid file name?')
try:
  pass
except:
  print('ExportUNV() failed. Invalid file name?')
robot_1 = smesh.Mesh(robot)
NETGEN_3D_Parameters_1 = smesh.CreateHypothesis('NETGEN_Parameters', 'NETGENEngine')
NETGEN_3D_Parameters_1.SetMaxSize( 0.01 )
NETGEN_3D_Parameters_1.SetMinSize( 0.002 )
NETGEN_3D_Parameters_1.SetSecondOrder( 1 )
NETGEN_3D_Parameters_1.SetOptimize( 1 )
NETGEN_3D_Parameters_1.SetFineness( 2 )
NETGEN_3D_Parameters_1.SetChordalError( -1 )
NETGEN_3D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_3D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_3D_Parameters_1.SetFuseEdges( 1 )
NETGEN_3D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_3D_Parameters_1.SetCheckChartBoundary( 72 )
status = robot_1.AddHypothesis(NETGEN_1D_2D_3D,L1)
status = robot_1.AddHypothesis(NETGEN_3D_Parameters_1,L1)
L2_1 = robot_1.GetSubMesh( L2, 'L2' )
status = robot_1.AddHypothesis(NETGEN_1D_2D_3D,L2)
status = robot_1.AddHypothesis(NETGEN_3D_Parameters_1,L2)
L3_1 = robot_1.GetSubMesh( L3, 'L3' )
status = robot_1.AddHypothesis(NETGEN_1D_2D_3D,L3)
status = robot_1.AddHypothesis(NETGEN_3D_Parameters_1,L3)
L2_2 = robot_1.GroupOnGeom(L2,'L2',SMESH.VOLUME)
L1_1 = robot_1.GroupOnGeom(L1,'L1',SMESH.VOLUME)
L3_2 = robot_1.GroupOnGeom(L3,'L3',SMESH.VOLUME)
L2_3 = robot_1.GroupOnGeom(L2,'L2',SMESH.NODE)
L1_2 = robot_1.GroupOnGeom(L1,'L1',SMESH.NODE)
L3_3 = robot_1.GroupOnGeom(L3,'L3',SMESH.NODE)
L2_SLAVE_1 = robot_1.GroupOnGeom(L2_SLAVE,'L2_SLAVE',SMESH.FACE)
L2_MASTER_1 = robot_1.GroupOnGeom(L2_MASTER,'L2_MASTER',SMESH.FACE)
L2_SLAVE_2 = robot_1.GroupOnGeom(L2_SLAVE,'L2_SLAVE',SMESH.NODE)
L2_MASTER_2 = robot_1.GroupOnGeom(L2_MASTER,'L2_MASTER',SMESH.NODE)
FIX_1 = robot_1.GroupOnGeom(FIX,'FIX',SMESH.FACE)
L1_MASTER_1 = robot_1.GroupOnGeom(L1_MASTER,'L1_MASTER',SMESH.FACE)
FIX_2 = robot_1.GroupOnGeom(FIX,'FIX',SMESH.NODE)
L1_MASTER_2 = robot_1.GroupOnGeom(L1_MASTER,'L1_MASTER',SMESH.NODE)
L3_SLAVE_1 = robot_1.GroupOnGeom(L3_SLAVE,'L3_SLAVE',SMESH.FACE)
L3_SLAVE_2 = robot_1.GroupOnGeom(L3_SLAVE,'L3_SLAVE',SMESH.NODE)
isDone = robot_1.Compute()
[ L2_2, L1_1, L3_2, L2_3, L1_2, L3_3, L2_SLAVE_1, L2_MASTER_1, L2_SLAVE_2, L2_MASTER_2, FIX_1, L1_MASTER_1, FIX_2, L1_MASTER_2, L3_SLAVE_1, L3_SLAVE_2 ] = robot_1.GetGroups()
robot_1.RotateObject( L2_1, SMESH.AxisStruct( J2X, 0, J2Z, 0, 1, 0 ), J2_ANGLE, 0 )
robot_1.RotateObject( L3_1, SMESH.AxisStruct( J2X, 0, J2Z, 0, 1, 0 ), J2_ANGLE, 0 )
robot_1.RotateObject( L3_1, SMESH.AxisStruct( J3X, 0, J3Z, 0, 1, 0 ), J3_ANGLE, 0 )
try:
  robot_1.ExportUNV( r'robot.unv' )
  pass
except:
  print('ExportUNV() failed. Invalid file name?')
L1_3 = robot_1.GetSubMesh( L1, 'L1' )


## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D_3D, 'NETGEN 1D-2D-3D')
smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
smesh.SetName(L2_1, 'L2')
smesh.SetName(L3_1, 'L3')
smesh.SetName(L1_3, 'L1')
smesh.SetName(robot_1.GetMesh(), 'robot')
smesh.SetName(L3_SLAVE_2, 'L3_SLAVE')
smesh.SetName(L1_MASTER_2, 'L1_MASTER')
smesh.SetName(FIX_2, 'FIX')
smesh.SetName(L2_MASTER_2, 'L2_MASTER')
smesh.SetName(L2_SLAVE_2, 'L2_SLAVE')
smesh.SetName(L3_3, 'L3')
smesh.SetName(L1_2, 'L1')
smesh.SetName(L1_1, 'L1')
smesh.SetName(L2_3, 'L2')
smesh.SetName(L3_2, 'L3')
smesh.SetName(L2_2, 'L2')
smesh.SetName(L3_SLAVE_1, 'L3_SLAVE')
smesh.SetName(L1_MASTER_1, 'L1_MASTER')
smesh.SetName(L2_SLAVE_1, 'L2_SLAVE')
smesh.SetName(FIX_1, 'FIX')
smesh.SetName(L2_MASTER_1, 'L2_MASTER')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()

# Kill
# https://www.salome-platform.org/forum/forum_10/645560298#457218771
import os
from killSalomeWithPort import killMyPort
killMyPort(os.getenv('NSPORT'))

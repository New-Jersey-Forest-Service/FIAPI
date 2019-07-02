import arcpy
import os



def Plotting_points():
    CN_Table = r"C:\Users\Abdul\Documents\GitHub\FIAPI\Python3x\reftable.csv"
    Plotted_Points= r"C:\Users\Abdul\Documents\GitHub\FIAPI\Python3x\CNPlots.gdb\Plotted_CNs"

    arcpy.management.XYTableToPoint(CN_Table,Plotted_Points, "LON", "LAT", None,
                                    "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision")



def spatialjoin():
    target_features = r"C:\Users\Abdul\Documents\GitHub\FIAPI\Python3x\CNPlots.gdb\Plotted_CNs"
    join_features = r"C:\Users\Abdul\Documents\GitHub\FIAPI\Python3x\CNPlots.gdb\NJ_Pinelands"
    out_feature_class = r"C:\Users\Abdul\Documents\GitHub\FIAPI\Python3x\CNPlots.gdb\SpatiallyJoined_Plots"
    arcpy.analysis.SpatialJoin(target_features, join_features ,out_feature_class ,
                           "JOIN_ONE_TO_ONE", "KEEP_COMMON",
                           'CN "CN" true true false 8 Double 0 0,First,#,refTable_XYTableToPoint,CN,-1,-1;LON "LON" true true false 8 Double 0 0,First,#,refTable_XYTableToPoint,LON,-1,-1;LAT "LAT" true true false 8 Double 0 0,First,#,refTable_XYTableToPoint,LAT,-1,-1;OBJECTID "OBJECTID" true true false 4 Long 0 0,First,#,NJ,OBJECTID,-1,-1;DESIGNATIO "DESIGNATIO" true true false 80 Text 0 0,First,#,NJ,DESIGNATIO,0,80;WEB_LINK "WEB_LINK" true true false 80 Text 0 0,First,#,NJ,WEB_LINK,0,80;ACRES "ACRES" true true false 8 Double 0 0,First,#,NJ,ACRES,-1,-1;GLOBALID "GLOBALID" true true false 80 Text 0 0,First,#,NJ,GLOBALID,0,80;SHAPE_Leng "SHAPE_Leng" true true false 8 Double 0 0,First,#,NJ,SHAPE_Leng,-1,-1;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,NJ,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0,First,#,NJ,Shape_Area,-1,-1',
                           "CLOSEST", ".5 Miles", None)





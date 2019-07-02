import os
import arcpy


def deleteoldfiles():
    if os.path.exists (r"C:\Users\Abdul\Documents\GitHub\FIAPI\Python3x\reftable.csv"):
        os.remove(r"C:\Users\Abdul\Documents\GitHub\FIAPI\Python3x\reftable.csv")

    else:
        print("Previous File Not Found")


    arcpy.management.Delete(r"C:\Users\Abdul\Documents\GitHub\FIAPI\Python3x\CNPlots.gdb\Plotted_CNs;C:\Users\Abdul\Documents\GitHub\FIAPI\Python3x\CNPlots.gdb\SpatiallyJoined_Plots", None)

    print("Previous Data Deleted")

import os
import arcpy


def deleteoldfiles():
    if os.path.exists (r"C:\Users\Abdul\Documents\GitHub\FIAPI\Python3x\reftable.csv"):
        os.remove(r"C:\Users\Abdul\Documents\GitHub\FIAPI\Python3x\reftable.csv")

    else:
        pass

    if os.path.exists (r"C:\Users\Abdul\Documents\GitHub\FIAPI\Python3x\Pineland_CNS.csv"):
        os.remove(r"C:\Users\Abdul\Documents\GitHub\FIAPI\Python3x\Pineland_CNS.csv")

    else:
        pass




    arcpy.management.Delete(r"C:\Users\Abdul\Documents\GitHub\FIAPI\Python3x\CNPlots.gdb\Plotted_CNs;C:\Users\Abdul\Documents\GitHub\FIAPI\Python3x\CNPlots.gdb\SpatiallyJoined_Plots", None)

    print("Previous Data Deleted")

#----------------------------------------------------------------------------------------
# Name:
#        setInput.py
#
# Purpose:
#        This is the input file for pltSet.py
#
#----------------------------------------------------------------------------------------
#--------------------------------------------------------------
# Names... These are only needed to construct
# file name and directories in this input file.
# If you specify files and directories directly you
# don't need these (e.g. they are not used in plotting program)
#--------------------------------------------------------------

loc        = 'tab'                  # Name of station location
gasName    = 'c2h6'                   # Name of gas
ver        = 'Current_v2'           # Name of retrieval version to process
ctlF       = 'sfit4_v2.ctl'            # Name of ctl file

#------
# Flags
#------
saveFlg    = True                  # Flag to either save data to pdf file (saveFlg=True) or plot to screen (saveFlg=False)
errorFlg   = True                  # Flag to process error data
fltrFlg    = True                   # Flag to filter the data
byYrFlg    = False                  # Flag to create plots for each individual year in date range
szaFlg     = True                   # Flag to filter based on min and max SZA
dofFlg     = True                   # Flag to filter based on min DOFs
pcNegFlg   = True                   # Flag to filter profiles with negative partial columns
tcNegFlg   = True                  # Flagsag to filter profiles with negative total columns
tcMMFlg    = False                  # Flag to filter based on min and max total column amount
cnvrgFlg   = True                   # Flag to filter profiles that did not converge
rmsFlg     = True                   # Flag to filter based on max RMS
chiFlg     = False     	            # Flag to filter based on max CHI_2_Y
mnthFlg    = False                  # Flag to filter based on 
bckgFlg    = False                  # Flag to filter based on slope and/or curvature (first micro-window)

mnths      = [6,7,8]                # Months to filter on (these are the months to include data)
maxRMS     = 2.2     	                 # Max Fit RMS to filter data. Data is filtered according to <= maxrms
minDOF     = 0.5                    # Min DOFs for filtering
maxDOF     = 10.0                    # Max DOFs for filtering
minSZA     = 0.0                   # Min SZA for filtering
maxSZA     = 90.0                   # Max SZA for filtering
maxCHI     = 2.0                    # Max CHI_y_2 value
maxTC      = 5.0E24                # Max Total column amount for filtering
minTC      = 0.0                 # Min Total column amount for filtering
sclfct     = 1.0E9                  # Scale factor to apply to vmr plots (ppmv=1.0E6, ppbv=1.0E9, etc)
sclfctName = 'ppbv'                 # Name of scale factor for labeling plots
minSlope   = 0.0
maxSlope   = 1.0
minCurv    = 0.0
maxCurv    = 1.0

#----------------------
# Date range to process
#----------------------
iyear      = 1999
imnth      = 1
iday       = 1
fyear      = 2019
fmnth      = 12
fday       = 31

#----------------------------
# Partial Columns Bounds [km] 
# [lower bound, upper bound]
# To turn off set to False
#----------------------------
pCols = [[0.0,8.0],[8.0,16.0],[16.0,25.0]]

#------------
# Directories
#------------ -
#retDir = '/Volumes/data1/ebaumer/'+loc.lower()+'/'+gasName.lower()+'/'+ver+'/'  
retDir = '/data1/ebaumer/'+loc.lower()+'/'+gasName.lower()+'/'+ver+'/'  


#------
# Files
#-----
#ctlFile  = '/Volumes/data1/ebaumer/'+loc.lower()+'/'+gasName.lower()+'/'+'x.'+gasName.lower()+'/'+ctlF
ctlFile  = '/data1/ebaumer/'+loc.lower()+'/'+gasName.lower()+'/'+'x.'+gasName.lower()+'/'+ctlF
#pltFile  = '/Volumes/data1/ebaumer/'+loc.lower()+'/' + 'Plots/' + loc + '_' + gasName + '_' + ver + '.pdf'

if(iyear == fyear):
    pltFile  = '/data1/ebaumer/'+loc.lower()+'/'+gasName.lower()+'/'+gasName.upper()+'_'+str(iyear)+'_'+ver+'.pdf'
else:
    pltFile  = '/data1/ebaumer/'+loc.lower()+'/'+gasName.lower()+'/'+gasName.upper()+'_'+str(iyear)+'_'+str(fyear)+'_'+ver+'.pdf' 
       

set MAYA_LOCATION=C:\Program Files\Autodesk\Maya2017

set MAYA_INCLUDE_DIR=%MAYA_LOCATION%\include\python2.7

set MAYA_LIBS_DIR=%MAYA_LOCATION%\lib

set MAYA_BIN_DIR=%MAYA_LOCATION%\bin

set COMPILE_CODE=%~dp0\py2pyd.py


subst a: %1 & A:

"%MAYA_BIN_DIR%\mayapy.exe" "%COMPILE_CODE%" build_ext --inplace -I "%MAYA_INCLUDE_DIR%" -L "%MAYA_LIBS_DIR%"

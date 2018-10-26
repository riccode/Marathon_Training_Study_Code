@echo off

SET CWD=%~dp0
set APP_DIR=fit_java_tool
set APP_NAME=FitCSVTool.jar
set APP_PATH="%CWD%%APP_DIR%\%APP_NAME%"

set a=%1
set a = "%a%"
set CSV_NAME=%a%
set CSV_NAME=%CSV_NAME:.fit=%

ECHO %CSV_Name%
call java -jar %APP_PATH% -b %a% %CSV_Name% --defn none --data record

ECHO "Conversion complete..."

EXIT
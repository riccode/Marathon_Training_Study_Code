@echo off
set /p id="Enter Participant ID: "
set /p min_date="Enter MIN DATE: "
set /p max_date="Enter MAX DATE: "
cmd /c "cd /d C:\Users\Running Injury Clini\Desktop\Marathon Training\Report_generator & python gen_report.py %id% %min_date% %max_date% & pause"
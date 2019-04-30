##Alterando formato da data
@echo off
setlocal
rem get the date
rem use findstr to strip blank lines from wmic output
for /f "usebackq skip=1 tokens=1-3" %%g in (`wmic Path Win32_LocalTime Get Day^,Month^,Year ^| findstr /r /v "^$"`) do (
  set _day=00%%g
  set _month=00%%h
  set _year=%%i
  )
rem pad day and month with leading zeros
set _month=%_month:~-2%
set _day=%_day:~-2%
rem get day of the week
for /f %%k in ('powershell ^(get-date^).DayOfWeek') do (
  set _dow=%%k
  )
rem output format required is DD-MM-YYYY_weekday
echo %_day%-%_month%-%_year%_%_dow%
endlocal

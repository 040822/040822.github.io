@echo off
setlocal

:: 定义文件名
set "fileA=photos_github.yml"
set "fileB=photos.yml"

:: 定义临时文件名
set "tempFile=temp.yml"

:: 确保临时文件名不会与现有文件冲突
if exist "%tempFile%" (
    echo Error: Temporary file "%tempFile%" already exists.
    exit /b
)

:: 交换文件名
ren "%fileA%" "%tempFile%"
ren "%fileB%" "%fileA%"
ren "%tempFile%" "%fileB%"

endlocal
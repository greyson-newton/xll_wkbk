@echo off

for %%A IN (*.py) do start /b /wait "" python "%%~fA"
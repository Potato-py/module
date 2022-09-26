@echo off
echo.
set pythonCMD=""
set pipCMD=""
python3 --version>nul 2>nul && set pythonCMD=python3
python2 --version>nul 2>nul && set pythonCMD=python2
python3 --version>nul 2>nul && set pythonCMD=python
pip3>nul 2>nul && set pipCMD=pip3
pip2>nul 2>nul && set pipCMD=pip2
pip>nul 2>nul && set pipCMD=pip
if pythonCMD=="" if pipCMD=="" echo ��⵽δ��װpython��pip
if not pythonCMD=="" if not pipCMD=="" (
echo ��⵽�Ѱ�װpython��pip����
echo.
%pipCMD%  install -r requirements.txt && echo python���õ�����Ѱ�װ��ϡ���
echo.
)
pause
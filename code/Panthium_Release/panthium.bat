ECHO "Panthium's requirements are being installed on your computer..."

@echo off
for /f "tokens=*" %%a in (requirements.txt) do (
  echo installing: %%a
  %%a
  
)


ECHO "Done :D"
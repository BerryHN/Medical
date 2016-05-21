del /S /AH *.db

echo creating folders for pictures
for /D %%i in ( * ) do for %%j in ( %%i\*.png ) do mkdir "%%~pnj"
echo putting each picture to a folder
for /D %%i in ( * ) do for %%j in ( %%i\*.png ) do move "%%j" "%%~pnj\%%~nj.TODO"

echo coloring well-known layers
for /D %%i in ( "head\*" ) do for %%j in ( "%%i\*.TODO" ) do move "%%j" "%%~pnj.T.skin.png"
for /D %%i in ( "body_back\*" ) do for %%j in ( "%%i\*.TODO" ) do move "%%j" "%%~pnj.T.skin.png"
for /D %%i in ( "body_front\*" ) do for %%j in ( "%%i\*.TODO" ) do move "%%j" "%%~pnj.O.9.png"
for /D %%i in ( "body_front_color\*" ) do for %%j in ( "%%i\*.TODO" ) do move "%%j" "%%~pnj.O.10.T.dress.png"
for /D %%i in ( "hair_back\*" ) do for %%j in ( "%%i\*.TODO" ) do move "%%j" "%%~pnj.T.hair.png"
for /D %%i in ( "hair_front\*" ) do for %%j in ( "%%i\*.TODO" ) do move "%%j" "%%~pnj.T.hair.png"
for /D %%i in ( "eye\*" ) do for %%j in ( "%%i\*.TODO" ) do move "%%j" "%%~pnj.T.eyes.png"

echo renaming not-so-well-known layers
for /D %%d in ( * ) do for /D %%i in ( "%%d\*" ) do for %%j in ( "%%i\*.TODO" ) do move "%%j" "%%~pnj.png"

echo moving well-known layers
move hair_back "20.back hair"
mkdir "30.dress"
for /D %%i in ( "body_back\*" ) do mkdir "30.dress\%%~ni"
for /D %%i in ( "body_back\*" ) do move "%%i\*" "30.dress\%%~ni"
for /D %%i in ( "body_front\*" ) do mkdir "30.dress\%%~ni"
for /D %%i in ( "body_front\*" ) do move "%%i\*" "30.dress\%%~ni"
for /D %%i in ( "body_front_color\*" ) do mkdir "30.dress\%%~ni"
for /D %%i in ( "body_front_color\*" ) do move "%%i\*" "30.dress\%%~ni"
rmdir /S /Q body_back body_front body_front_color
move head "50.head"
move eye "60.eyes"
move face_front "70.face"
move hair_front "80.front hair"

echo removing empty folders
for /D %%i in ( * ) do rmdir "%%i"



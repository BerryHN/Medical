rm *_stat.txt
for /D %%i in ( sandwich\* ) do (
    echo ### %%i ### >>conditions_stat.txt
    ls "%%i" -R1 | grep "\.IF\." | sed "s/=://" | sed "s/.*\.IF\./IF /"  | sort -u  >>conditions_stat.txt
    ls "%%i" -R1 | grep "\.set" | sed "s/\(.*\)\.set/SET \1/" | sort -u  >>conditions_stat.txt
)
for /D %%i in ( sandwich\* ) do (
    echo ### %%i ### >>colors_stat.txt
    ls "%%i" -R1 | grep -v "\.A\.set" | grep "\.A\." | sed "s/.*\.A\./A /" | sed "s/\..*//" | sort -u  >>colors_stat.txt
    ls "%%i" -R1 | grep "\.C\." | sed "s/.*\.C\./C /" | sed "s/\..*//" | sort -u  >>colors_stat.txt
    ls "%%i" -R1 | grep "\.T\." | sed "s/.*\.T\./T /" | sed "s/\..*//" | sort -u  >>colors_stat.txt
)
# Leviathan Level 6
# Tests all 4 number combinations until entry to shell is granted

for i in {0000..9999}
do
~/leviathan6 $i
printf "%s\n" "$i"
done

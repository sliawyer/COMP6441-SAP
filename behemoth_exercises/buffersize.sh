# Behemoth Level 1 
# Script to determine the size of the buffer 

i=10
result='initial'
while [ ! -z "$result" ]
do
        i=$((i+1))
        result=$(python3 -c "print($i*'A')" | /behemoth/behemoth1)
        echo $result
done
echo "behemoth1 crashes at $i"
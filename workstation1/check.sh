for run in {1..100}
do
python generator.py >input.txt
python naive.py <input.txt >naive_output.txt
python my.py <input.txt > output.txt
echo '-----------------------------------------------'
echo $run
result=`python comparer.py`
echo $result
if [ $result ==  "Failed" ]; then
  break
fi
done

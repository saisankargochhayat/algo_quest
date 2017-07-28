for run in {1..100}
do
python generator.py >input.txt
python naive.py <input.txt >naive_output.txt
python my.py <input.txt >output.txt
python comparer.py
done

@ECHO OFF
python simulation.py > tmp/simulation_output.txt
python -c "print(open(r'simulation_expected_output.txt').read() == open(r'tmp/simulation_output.txt').read() and 'test success' or 'test fail')"
for i in {1..250}; do python ./hacker.py && selenium-side-runner selenium-output.side && echo ${i}; done
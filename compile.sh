gfortran -Wall -fbounds-check -O -Wuninitialized -ffpe-trap=invalid,zero,overflow -fbacktrace $1 -o `basename $1 f90`x

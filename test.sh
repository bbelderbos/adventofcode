for i in `ls -d 2*/day*`;
do
	echo "Running tests for $i" ; pytest $i
done

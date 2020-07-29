# sortIPs
Python script to read IPs from file, sort ascending, remove duplicates, and output a sorted file

# Read From File, Output Any IP Addresses Found In Sorted List

The script sortIPs.py allows you to input a text file containing IP addresses, and it will output a text file with any duplicate IP addresses removed, and sorted in ascending order.  It can serve as a library to be imported as well.

## Run Application

In the directory where the script is stored run:

```
python sortedIPs.py SomeFile.txt
```

If running properly there will be no output but you will create a file in the same directory from which it ran containing the output.

Alternately, you can run the script with the -x flag:

```
python sortedIPs.py -x SomeFile.txt
```

If running properly, the file created will contain a list of sanitized IOCs for use in threat reporting
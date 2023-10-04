## Bloom Filter
This project is an implementation of a Bloom filter in Python. A Bloom filter is a probabilistic data structure used to check if an element belongs to a set. The Bloom filter uses various hash functions to map elements to a set of positions in a bit array. Then, to check if an element belongs to the array, the same hash functions are applied to that element and it is checked if all the corresponding bits in the bit array are on. If all bits are on, the element probably belongs to the set; otherwise, it can be said with certainty that the element is not in the set. It is said that "it is probable" that it is in the set, for that reason that collisions can occur in which two elements produce the same positions in the bit array.

This project implements a Bloom filter that uses multiple hash functions, which improves its accuracy in detecting elements in the array and reduces the probability of false positives. The number of hash functions used depends on the size of the set and the acceptable error rate.

The acceptable error rate is used to determine the size of the bit array used for the Bloom filter, and therefore the number of hash functions needed. When you create an instance of the BloomFilter class, you specify the expected size of the array and the acceptable error rate. The size of the bit array is calculated from these values, and the number of hash functions is automatically calculated based on the size of the bit array. The acceptable error rate is the probability that false positives will occur.

The BloomFilter class uses a custom implementation of a bit array, represented as a integer. This implementation allows efficient handling of the individual bits of the bit array. The BitArray class defines methods to set and get bits at a specific position in the bit integer.

### Use
To use this bloom filter in your own project, simply add the bloom_filter.py file to your project and create an instance of the BloomFilter class. You can then add elements to the filter using the add method and check if an element is present using the contains method.

```python
from bloom_filter import BloomFilter

bf = BloomFilter(1000, 0.01)
bf.add("example")
bf.add("another example")

if bf.contains("example"):
       print("The element 'example' is in the filter.")
else:
       print("The element 'example' is not in the filter.")
```

In this example, a Bloom filter is created with a capacity of 1000 elements and an acceptable error rate of 1%. Two elements are added to the filter, and then it is checked if the element "example" is present. If present, a message is printed indicating that the item is in the filter; otherwise, a message is printed indicating that it is not in the filter.

## Output
The test that is done in the project code uses the files in1.csv and in2.csv as the inputs to add the elements to the bloom filter. All the elements in the in1.csv file are added to the bloom filter and the elements in the in2.csv file are used to check whether or not they are in the bloom filter. The output of the code is the following:

```
weseGLCIEPTUusDlU@aol.com, Probably in the DB
qYHiFYrGlwM@gmail.com,Not in the DB
PLekUVqtWnRVWShep@hotmail.com, Probably in the DB
BXgWIGaZRv@aol.com, Probably in the DB
NathUxfEPTEj@upr.edu,Not in the DB
hmCdguIbyk@aol.com, Probably in the DB
iUdkOTYeDMzzwIrytHSh@upr.edu, Probably in the DB
HZDJvGTwH@yahoo.com,Not in the DB
McdmnpxEjob@hotmail.com,Not in the DB
```

### Contributions
If you find any bugs or have suggestions for improvement, feel free to contribute to the project!

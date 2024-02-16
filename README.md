# Codebeez One Billion Row Challenge - Python

The original Java challenge: https://github.com/gunnarmorling/1brc

## Creating the test data

Make sure you have activated the virtual environment and run the following command:

```python
python -m data.create_data NUM_OF_ROWS
```

If no argument is provided, 1 billion rows will be created. You can find the input in `data/measurements.txt`.

The text file contains temperature values for a range of weather stations. Each row is one measurement in the format `<station name: string>;<measurement: float>`, with the measurement value having exactly one fractional digit. The following shows ten rows as an example:

```
Hamburg;12.0
Bulawayo;8.9
Palembang;38.8
St. John's;15.2
Cracow;12.6
Bridgetown;26.9
Istanbul;6.2
Roseau;34.4
Conakry;31.2
Istanbul;23.0
```

Now that you have the data, you can implement your solution in the `src/` folder.


The task is to write a Python program which reads the file, calculates the min, mean, and max temperature value per weather station, and emits the results on stdout like this (i.e. sorted alphabetically by station name, and the result values per station in the format <min>/<mean>/<max>, rounded to one fractional digit):

```
{Abha=-23.0/18.0/59.2, Abidjan=-16.2/26.0/67.3, Abéché=-10.0/29.4/69.0, Accra=-10.1/26.4/66.4, Addis Ababa=-23.7/16.0/67.0, Adelaide=-27.8/17.3/58.5, ...}
```

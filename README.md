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

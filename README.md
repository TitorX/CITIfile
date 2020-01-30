# CITIfile

Read CITI format file by python.

## Introduction

`CITIfile` is a tiny library that allows you to read
CITI format file by using Python.

## Installation

```shell script
pip install -U CITIfile
```

## Tutorial

`CITIfile` is easy to use:

```python
from CITIfile import read_citifile


data = read_citifile("data.citi")
```

Then, it will parse the data file and
return a `xarray.Dataset` object. Like the following:

```
<xarray.Dataset>
Dimensions:   (C_d2: 3, L_load: 6, freq: 6)
Coordinates:
  * L_load    (L_load) float64 20.0 21.0 22.0 23.0 24.0 25.0
  * C_d2      (C_d2) float64 1.0 1.5 2.0
  * freq      (freq) float64 3e+07 3.1e+07 3.2e+07 3.3e+07 3.4e+07 3.5e+07
Data variables:
    S[1,1]    (L_load, C_d2, freq) complex128 (0.0517763713-0.00941470346j) ... (0.0593002475-0.0233189028j)
    S[1,2]    (L_load, C_d2, freq) complex128 (0.771829001+0.00291050315j) ... (0.774683786+0.0184790199j)
    S[2,1]    (L_load, C_d2, freq) complex128 (0.771829001+0.00291050315j) ... (0.774683786+0.0184790199j)
    S[2,2]    (L_load, C_d2, freq) complex128 (0.0517763713-0.00941470346j) ... (0.0593002475-0.0233189028j)
```

`CITIfile` parses and converts CITI format to `xarray.Dataset` object,
because CITI format file stores data in multidimensional array format
and `xarray` are designed to handle this kind of data.

See [xarray documents](http://xarray.pydata.org/en/stable/) to
learn that how to manipulate `xarray.Dataset` object.

## Websites

Main website:
https://github.com/TitorX/CITIfile

CITIfile Definitions:
http://literature.cdn.keysight.com/litweb/pdf/ads15/cktsim/ck2016.html

xarray document:
http://xarray.pydata.org/en/stable/

## Reports

Report bugs or ask questions at
https://github.com/TitorX/CITIfile/issues.

## Contact

Written by Shoukun Sun.

Email: titor.sun@gmail.com

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

### Displaying Coordinates and Data Variables

```python
print('Coordinates:')
for cname in data.coords:
    cdata = data.coords[cname].data
    print(f'- {cname}: {len(cname)} ({cdata}, {cdata.dtype})')

print('Data:')
for vname in data.data_vars:
    vdata = data.data_vars[vname]
    print(f'- {vname}: {vdata.dtype}')
```

This displays the names and types of the corrdinates and data variables, as well as the available corrdinate values (which are `numpy.ndarray`).

### Extracting Usable 2D Data

In this example, we extract `S[1,1]` vs. `freq`, at some given coordinates for `C_load` and `C_d2`:

```python
# select the data variable at the given corrdinates
data_slice = data.data_vars["S[1,1]"].sel(L_load=20, C_d2=1)

# now there is only one coordinate (freq) left as independent variable
x = data_slice.coords["freq"].data

# dependent variable (Y-axis)
y = data_slice.data

for px, py in zip(x, y):
    print(f"freq={px} -> S[1,1]={py}")
```

Both `x` and `y` are `numpy.ndarray`.

### File Comments

If any comments are found in the file, they are stored in the `comments` attribute:

```python
if 'comments' in data.attrs:
    print(data.attrs['comments'])
```


## Websites

Main website:
https://github.com/TitorX/CITIfile

CITIfile Definitions:
https://helpfiles.keysight.com/csg/N1930xB/FilePrint/CITIfile_Format.htm

xarray document:
http://xarray.pydata.org/en/stable/

## Reports

Report bugs or ask questions at
https://github.com/TitorX/CITIfile/issues.

## Contact

Written by Shoukun Sun.

Email: titor.sun@gmail.com

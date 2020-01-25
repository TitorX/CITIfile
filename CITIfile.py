import numpy as np
import xarray as xr


__version__ = "0.1.1"
__author__ = "Titor"
__email__ = "titor.sun@gmail.com"


def parse_variable(lines, array):
    if array.dtype == np.float:
        def _convert(x):
            return np.float(x)
    else:
        def _convert(r, i):
            return np.complex(np.float(r), np.float(i))

    idx = 0
    while lines:
        line = lines.pop(0).split(",")
        if "END" in line[0]:
            break

        array.put(idx, _convert(*line))
        idx += 1


def parse_package(lines):
    shape = []
    # [[name, array], [name, array] ...]
    var_list = []
    data_list = []
    variables = []
    data = []

    name = lines.pop(0).split(" ")[1][:-1]

    while lines:
        line = lines.pop(0)[:-1].split(" ")

        if line[0] == "VAR":
            length = int(line[-1])  # amount of data points
            dtype = np.float if line[-2] == "MAG" else np.complex  # data type

            shape.append(length)
            array = np.zeros(length, dtype)
            var_list.append((line[1], array))

        elif line[0] == "DATA":
            dtype = np.float if line[-1] == "MAG" else np.complex  # data type
            array = np.zeros(shape, dtype=dtype)
            data_list.append((line[1], array))

        elif line[0] == "VAR_LIST_BEGIN":
            variable = var_list.pop(0)
            parse_variable(lines, variable[1])
            variables.append(variable)

        elif line[0] == "BEGIN":
            variable = data_list.pop(0)
            parse_variable(lines, variable[1])
            data.append(variable)

        elif line[0] == "":
            break

    return name, variables, data


def read_citifile(filename):
    packages = []

    f = open(filename)
    lines = f.readlines()
    f.close()

    while lines:
        line = lines.pop(0)
        if line.startswith("CITIFILE A.01.00"):
            packages.append(parse_package(lines))

    ds = {}
    for package in packages:
        name, variables, data = package
        dataset = {d[0]: xr.DataArray(d[1], coords=variables) for d in data}
        dataset = xr.Dataset(dataset)
        ds[name] = dataset

    return ds

# kiCadCsvSchPopulate
populate info to sch file from csv

## Usage info

### Basic setup
```
chmod u+x parser.py
./parser.py -h
```

### Basic usage
```
./parser.py -d database.csv -s kicad_schema.sch > errorlog
```

Be sure to feed it a correct .csv and a correct .sch as input and output files; there is little to no error checking in the code :p

### About
This repository includes two scripts (1) perf.py (2) covid.py.

### Dependencies

`pip install -r requirements.txt`

### perf.py 
Format: perf.py -l -j host

positional arguments:
  host                  The host address that will be tested

optional arguments:

  `-h, --help`            show this help message and exit
  
  `-l LATENCY, --latency` LATENCY
                        Max latency limit before considered critical
                        
  `-j JITTER, --jitter` JITTER
                        Max jitter limit before considered critical


### Example
`python perf.py -l 25 google.com`

output: `HOST NOT_OK - rtt=33.969 ms | OK - jitter=4.666 ms`

### covid.py
Calls an API to get the global total number of covid cases.

usage: covid.py [options]

optional arguments:
  `-h, --help`   show this help message and exit
  
  `--active`     Include active cases
  
  `--deaths`     Include number of deaths
  
  `--recovered`  Include recovered cases
  
  ### Example
  `python covid.py`
  
  output: `[2021-07-22 23:05:36] 200 CASES - 193007589`
  
  `python covid.py --active`
  
  output: `[2021-07-22 23:05:36] 200 CASES - 193007589 | active: 13377552`
  
  ### Credits
  Covid data API: `https://corona.lmao.ninja/v2/all?yesterday`

# simple-comments-parser
Simple python script to extract comments from the source code of some programming languages.

This script uses comment-parser module to parse the comments from the source code.

Please refer to the [module page on PyPi.org](https://pypi.org/project/comment-parser/) for more information about installation.


## Usage
```
python parser.py <filename>
```

or

```
python parser.py
Please enter the full path of the file: <filename>
```
## Supported Programming Languages

| Language   | Mime String            |
| :--------- | :--------------------- |
| C          | text/x-c               |
| C++/C#     | text/x-c++             |
| Go         | text/x-go              |
| HTML       | text/html              |
| Java       | text/x-java-source     |
| Javascript | application/javascript |
| Shell      | text/x-shellscript     |
| XML        | text/xml               |

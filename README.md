# pparse
Utility to Process a File, Text Blob, or URL string for proofpoint URLS

##usage:

pparse [-f] [-b] [-u] [-o | -O] file | url

* Parse a file for URL's and write New file
  * `pparse -f mylogfile.log -o myparsedlogfile.log`
  
* Parse a file for URL's and overwrite existing
  * `pparse -Of mylogfile.log  `

* Parse a text blob ( *can also be used with -o to output to file* ) 
  * `pparse -b "MY BLOB OF TEXT"`
  
* Parse a URL String
  * `pparse -u Http://myproofpointed.URL`
  
```
Positional arguments:

file        text file with embedded Proofpoint encoded URL's    
url         Proofpoint encoded URL.
  
optional arguments:
-f, --file file_name
-b, --blob <quoted text blob>
-u, --url <url_string...>
-O, --overwrite # overwrites input file To be used in conjunction with -f -h --help
-o, --outfile <outfile name> used with -b or -f
```
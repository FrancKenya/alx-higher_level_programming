 #!/bin/bash
 # This script takes in A URL, sends a request to that URL,
 # and displays the size of the body of the response

 if [ $# -ne 1 ]; then
	 exit 1
 fi
 url=$2
 path_to_output=$1

 curl -s -o "$path_to_output" -w "%{size_download}" "$url"

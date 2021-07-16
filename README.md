# Large-file-downloader
These are different strategies to download a large file in TCP connection in C++. 
* Strategy 1:  opens a TCP connection to the server,  issues a GET request, downloads the entire content, and stores it in a file in one go.
* Strategy 2:  opens a TCP connection to the server, issues a GET request for a particular range of bytes and repeats till the entire content is downloaded
* Strategy 3:  opens TCP connections to different servers via threads and downloading a particular chunk size of 10k and book keeping which chunks have been downloaded till the entire content is downloaded. The thread ends in case a tcp connection breaks. 
* Strategy 4:  Imitates bittorrent and opens TCP connections to different servers via threads and downloading a particular chunk size of 10k and book keeping which chunks have been downloaded till the entire content is downloaded. The thread doesnt end in case of a connection failure.  

1) First of all I was not able to download the log file, so I downloaded the zip file and extracted the log file
2) I chose line by line preprocessing for the log data as it will be able to handle large inputs without requiring significant memory, also this method is easy to implement and maintain without relying on external tools or database. It also processes logs sequentially ensuring minimum resource allocation.


STEPS TO RUN THE FILE
1) First of all clone the repository and open the src folder then in terminal write
          curl -L -o test_logs.log "https://limewire.com/d/90794bb3-6831-4e02-8a59-ffc7f3b8b2a3#X1xnzrH5s4H_DKEkT_dfBuUT1mFKZuj4cFWNoMJGX98"
2) Ensure python3 is installed on your system with specified python compiler path
3) Ensure input log file is on the same directory as the script
4) Open the terminal and navigate the directory containing extract_logs.py and execute the following script
    python extract_logs.py YYYY-MM-DD
    Replace YYYY-MM-DD with the specified date
5) The filtered log files will be saved to output directory output_<YYYY-MM-DD>.txt

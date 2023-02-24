# Here's a high-level overview of how the program can work
1-Read in all the .epub files from the input folder.
2-Generate all possible combinations of the input files, keeping in mind that the order of the input files matters (i.e., combining A+B is different from combining B+A).
3-For each combination, merge the input files into a single output .epub file. To do this, you can use a library like epublib or pyepub.
4-Add a TOC to the start of each output file, with links to each book in the combined file. Again, you can use the same library to do this.
5-Write each output file to the output folder.
6-Sort the output files by the number of input files they contain, from most to least unique.

# Here's how the script works:
1-After adding all the input files to the output file, the script creates an empty TOC using the "add_toc()" method and stores it in the toc variable.
2-For each input file that was added to the output file, the script creates a link using the "add_link()" method. The href argument of "add_link()" is set to the ID of the toc_item object returned by add_html(), which is the ID of the HTML item that contains the content of the input file. The rel argument is set to 'contents', and the title argument is set to the title of the input file.
3-For each input file that was added to the output file, the script adds a nav point to the TOC using the add_nav_point() method. The title argument is set to the title of the input file, the toc_item argument is set to the toc_item object returned by add_html(), and the link argument is set to the link object created in step 2.
4-The output files are written to the output folder and sorted in the same way as before.

Note that you still need to install the epub library using pip before running this script. 

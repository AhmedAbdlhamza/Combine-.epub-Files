import os
import itertools
from epub import EpubFileInMemory, EpubFile

input_folder = 'input'
output_folder = 'output'

# Read in all the .epub files from the input folder.
input_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.epub')]

# Generate all possible combinations of the input files.
combinations = []
for r in range(2, len(input_files) + 1):
    for c in itertools.combinations(input_files, r):
        combinations.append(c)

# Merge the input files into a single output .epub file for each combination.
output_files = []
for c in combinations:
    output_file = EpubFileInMemory()
    toc_items = []
    for f in c:
        with EpubFile(f) as input_file:
            toc_item = output_file.add_html(input_file.get_content())
            toc_items.append((input_file.get_title(), toc_item))
    output_file.set_title(' + '.join(os.path.basename(f) for f in c))
    output_file.set_language('en')
    output_file.set_identifier('unique-' + '-'.join(os.path.basename(f)[:-5] for f in c))
    output_file.set_cover(input_file.get_cover())

    # Add a TOC that links to each book in the output file.
    toc = output_file.add_toc([])
    for title, toc_item in toc_items:
        link = output_file.add_link(href=toc_item.get_id(), rel='contents', title=title)
        toc.add_nav_point(title, toc_item, link=link)

    output_files.append(output_file)

# Write each output file to the output folder.
for i, f in enumerate(output_files):
    with EpubFile(os.path.join(output_folder, f'{i+1}.epub'), 'w') as output_file:
        output_file.write(f)

# Sort the output files by the number of input files they contain, from most to least unique.
output_files.sort(key=lambda x: len(x.get_contents()), reverse=True)

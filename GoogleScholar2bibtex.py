# AUTHOR: Oguz Toragay
# This code generate a .bib file from all the entries that are presented in the author's Google Scholar account.
# Note: All the enteries are added as article{}.

from scholarly import scholarly

author_name = 'YOUR NAME HERE'
search_query = scholarly.search_author(author_name)
authors = list(search_query)

print('The following authors found. Please select the correct one based on the affiliation:\n')

for idx, author in enumerate(authors):
    print(f"{idx + 1}: affiliation: {author['affiliation']}")

selected_index = int(input('\n Enter the number corresponding to the correct author: ')) - 1
selected_author = scholarly.fill(authors[selected_index])

file_name = str(selected_author['name'].replace(' ', ''))+'.bib'
with open(file_name, "w", encoding="utf-8") as bibtex_file:
    for pub in selected_author['publications']:
        filled_pub = scholarly.fill(pub)
        if 'bib' in filled_pub:
            bib_data = filled_pub['bib']
            bibtex_entry = f"@article{{{bib_data.get('title', 'Unknown').replace(' ', '')[:10]+str(bib_data.get('pub_year'))},\n"
            bibtex_entry += f"  title = {{{bib_data.get('title', 'Unknown')}}},\n"
            bibtex_entry += f"  author = {{{bib_data.get('author', 'Unknown')}}},\n"
            bibtex_entry += f"  journal = {{{bib_data.get('journal', 'Unknown')}}},\n"
            bibtex_entry += f"  volume = {{{bib_data.get('volume', 'Unknown')}}},\n"
            bibtex_entry += f"  number = {{{bib_data.get('number', 'Unknown')}}},\n"
            bibtex_entry += f"  pages = {{{bib_data.get('pages', 'Unknown')}}},\n"
            bibtex_entry += f"  year = {{{bib_data.get('pub_year', 'Unknown')}}},\n"
            bibtex_entry += f"  publisher = {{{bib_data.get('publisher', 'Unknown')}}}\n"
            bibtex_entry += "}\n"
            bibtex_file.write(bibtex_entry + "\n")
        else:
            print(f"Missing 'bib' data for publication: {filled_pub.get('bib_id', 'Unknown ID')}")

print('BibTeX entries have been saved to -->' + file_name)

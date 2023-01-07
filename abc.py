import html2text

# Read the HTML file
with open('input.html', 'r',encoding='utf-8') as f:
    html = f.read()

# Convert the HTML to Markdown using html2text
markdown = html2text.html2text(html)

# Write the Markdown to a file
with open('output.md', 'w', encoding='utf-8') as f:
    f.write(markdown)

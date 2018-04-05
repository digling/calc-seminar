# author   : Johann-Mattis List
# email    : mattis.list@uni-marburg.de
# created  : 2015-06-29 16:46
# modified : 2015-06-29 16:46
"""
<++>
"""

__author__="Johann-Mattis List"
__date__="2015-06-29"

import markdown
import glob

files = glob.glob('posts/*.md')
template = open('templates/template.html').read()

links = []
for f in files:
    
    name = f.split('/')[-1].replace('.md','.html')
    data = open(f).read().split('\n')
    
    header,main = data[0], '\n'.join(data[1:])

    links += [(name,header)]
    
    content = '<section>{0}</section>\n'
    content = content.format(markdown.markdown(main))
    with open(name,'w') as f:
        f.write(
                template.format(
                    CONTENT = content
                    )
                )

with open('index.html','w') as f:
    txt = '## Übersicht\n'
    for l,n in sorted(links, key=lambda x: x[1]):
        txt += '* [{0}]({1})\n'.format(
                '-'.join(n.split('-')[1:]),
                l)
    f.write(template.format(
        CONTENT = '<section>'+markdown.markdown(txt)+'</section>\n'))



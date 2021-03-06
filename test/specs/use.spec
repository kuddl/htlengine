#
### sightly use function
#
<div data-sly-use.page="./use_spec/test_page.js">Hello ${page.title}.</div>
===
<div>Hello Jupiter.</div>
^^^
29:     $.dom.append($n, var_0);
#
### sightly use variables are case insensitive
#
<div data-sly-use.testpage="./use_spec/test_page.js">Hello ${testPage.title}.${testPage.TiTle}</div>
===
<div>Hello Jupiter.undefined</div>
#
### passing params
#
<div data-sly-use.page="${'./use_spec/test_page.js' @ value1='Moon', value2='Europa'}">${page.subTitle}</div>
===
<div>Moon: Europa</div>
^^^
28:     $.dom.append($n, var_0);
#
### passing params with colon
#
<div data-sly-use.page="${'./use_spec/test_page.js' @ jcr:title='Space Report'}">${page.title}</div>
===
<div>Space Report</div>
#
### using functions
#
<div data-sly-use.page="${'./use_spec/test_page.js' @ radius='70000'}">Surface Area: ${page.area}</div>
===
<div>Surface Area: 61575216010.35994</div>
^^^
29:     $.dom.append($n, var_0);
#
### using functions with colon
#
<div data-sly-use.page="${'./use_spec/test_page.js'}">etag: ${page.jcr:etag}</div>
===
<div>etag: 1234</div>
#
### using async use classes
#
<div data-sly-use.page="./use_spec/test_page_async.js">Hello ${page.title}.</div>
===
<div>Hello Saturn.</div>
^^^
29:     $.dom.append($n, var_0);
#
### get like function
#
<div data-sly-use.page="${'./use_spec/test_page.js'}">text: ${page.text}</div>
===
<div>text: some text</div>
#
### normal function
#
<div data-sly-use.page="${'./use_spec/test_page.js'}"><button enabled="${page.isBold}">bold</button></div>
===
<div><button enabled>bold</button></div>
#
### async function
#
<div data-sly-use.page="${'./use_spec/test_page.js'}">delayed: ${page.delayedText}</div>
===
<div>delayed: delayed hello.</div>
#
### get like function with 'in' operator
#
<div data-sly-use.page="${'./use_spec/test_page.js'}">text: ${'text' in page}</div>
===
<div>text: true</div>
#
###

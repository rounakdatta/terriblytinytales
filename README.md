# Terribly Tiny Tales

This is an assignment for the application to **Terribly Tiny Tales** for their Software Engineering Internship for summer 2018.

* The text is first web-scraped using requests, cleaned and put into data-structure
* Uses trie data-structure to store the words (and their breakups)
* Uses list-of-lists to store the word set (word, frequency)
* Flask web-sever to render the content to HTML tables

## Local usage

```make```

### Working

* First, the script scrapes the text file from [here](http://terriblytinytales.com/test.txt) using *requests* module.
 The entire text is split into words and converted to lower case.
* Then, the words are put into trie data-structure as well as added to the final_list *[ Σ['key', 'count'] ]* with count=0.
 Whenever there is a collision (the word exists), the final_list only is updated (count increased).
* Apart from this, the trie data-structure implemented here has attributes data (char), list of children, branch_end, count and has functions for addition of data as well as finding if data exists.
* To render a frontend to it, Flask is used. The API to the above algorithm is *give_count(n)* which is called from Flask *app.py* to get the final_list.
 To render it, *tables.py* converts it into HTML table and creates *result.html* (of course using *os* py-module) which is then displayed.

Here's a quick visualization of the trie data-structure :

                       *
                    /     \
                  a         b
                /   \       |
              ap     as     ba
              /\      |     / \
            app apk   ask  bac  bak
                            |     |
                           back  bake

Scripting and markup languages used : **Python**, **HTML**<br>
Frameworks used : **Flask**<br>
PaaS used : **Heroku**, **PythonAnywhere**<br>

![Sample](https://github.com/rounakdatta/terriblytinytales/blob/master/demo/demo.gif)

The demo is currently live at [tttales.tk](http://tttales.tk).<br>
I've also made a blog post [here](http://rounakdatta.tk/2018/03/18/terriblytinytales.html).

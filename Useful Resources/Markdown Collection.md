# Markdown Collection
#### A complete list of Markdown Features

## Purpose:
* As a guide for people new to Markdown–a quick and powerful way to format, stylize, and decorate plain text for graphics.
* To list all the features of Markdown for reference.

### What is Markdown Good For?

There are many things that Markdown can be used for.
- Creating GitHub Documents (Like the one you're reading right now). Markdown is universal on GitHub.
- Creating Websites without any HTML. Quite Amazing!
- Quickly stylize and format documents with no HTML and minimal effort, trust me, it becomes easier as you use it more.
- And some people even write/publish books with it!

### A Quick Note on HTML in Markdown (Preface)

There are a few crucial things to know about Markdown.

The first is that Markdown is a straightforward and powerful simplification of HTML. This means that some HTML attributes will apply to it.

And it is important to remember, if you are using a raw editor to edit markdown (like I am), that leaving an empty line between two lines (of text or otherwise) will tell the implementation to wrap the text in \<p>\</p>.

So if you don't want your text to be jumbled together, make sure to double space. It is also good for the code visually, in the rare event that it needs to be debugged (probably a forgotten escape, unclosed bracket, or "reused" conflicting reference). You can read more about HTML and Markdown [here][HTML].

# General

### Headers:
# Heading 1
`# Heading 1` equivalent to an `<h1>` tag:

## Heading 2
`## Heading 2` equivalent to an `<h2>` tag:

### Heading 3
`### Heading 3` equivalent to an `<h3>` tag:

#### Heading 4
`#### Heading 4` equivalent to an `<h4>` tag:

##### Heading 5
`##### Heading 5` equivalent to an `<h5>` tag:

###### Heading 6
`###### Heading 6` equivalent to an `<h6>` tag:

Alternatively, you can also use "Underlining" to define `<h1>` and `<h2>`
_(Not Recommended)_. The above method is preferred

Heading 1
==
```
Heading 1
== (2 or more)
```

Heading 2
--
```
Heading 1
-- (2 or more)
```
Note: You cannot actually put anything after the equal signs (=) or hyphens (-)

### Horizontal Rule

Similar to the underlining method, you can also create a *'horizontal rule'*, or a line break, using three or more Hyphens (-), Asterisks (\*), or Underscores (\_), make sure they are separated from text above.

Hyphen Horizontal Rule

---
Asterisk Horizontal Rule

***
Underscore Horizontal rule

___

```
Hyphen Horizontal Rule

---
Asterisk Horizontal Rule

***
Underscore Horizontal rule

___
```

### Emphasis

_Italic_
`_Italic_`

*Italic*
`*Italic*`

__Bold__
`__Bold__`

**Bold**
`**Bold**`

These can be used in combination (examples):

_Italic, **Bold and Italic**_

`_Italic, **Bold and Italic**_`

__Bold *Bold and Italics* Bold__ _Italics_

`__Bold *Bold and Italics* Bold__ _Italics_`

They can be stacked but it is not recommended:

__Bold _Italics_ Bold__

`__Bold _Italics_ Bold__ `

*Italics **Bold** Italics*

`*Italics **Bold** Italics*`

And Strikethroughs:

~~Strikethrough~~
`~~Strikethrough~~`

### Block Quotes:

>Block Quote

`>Block Quote`

>Block Quote _with **Markdown**_ ~~inside~~

`>Block Quote _with **Markdown**_ ~~inside~~`

Block Quotes can be nested, and they can also contain Code Blocks.

> Block Quote.
>
>> Nested Block Quote.
>>
>>> Can be nested multiple times.
>
>`Can have code blocks within them`
>
>```Python
>And large, formatted code blocks too
>import math as m
>print(str(m.pi))
>```

````
> Block Quote.
>
>> Nested Block Quote.
>>
>>> Can be nested multiple times.
>
>`Can have code blocks within them`
>
>```Python
>And large, formatted code blocks too
>import math as m
>print(str(m.pi))
>```
````

_Note_: The (\` \` \`) Triple Backticks are placed next to Backslashes to prevent

### Lists:

Unordered lists can be made using Asterisks (\*), Hyphens (-) and Plusses (+).


* Item 1
* Item 2

- A different lists
- With more items

+ Yet another one
+ With endless possibilities

```
* Item 1
* Item 2

- A different lists
- With more items

+ Yet another one
+ With endless possibilities
```

Ordered lists can be made using numbers.

1. Number one
2. Number two

3. Number three
1. Number four
1. And more

```
1. Number one
2. Number two

3. Number three
1. Number four
1. And more
```

As you see, the number does not have to be in order. However, it is recommended to keep them in order for visual intent of the raw code.

Sublists and Paragraphs:

1. Sublists are quite straightforward
    * There can be Unordered sublists
2. And ordered ones
    1. Like this
    2. and this
3. Now...
    * To create a _Sublist_,
    * All you need is to _indent_.
        * And as with **Block Quotes**
            * You can ~~cannot~~ **nest** _Sublists_
                * And **use _Markdown_**
4. The same works with a Paragraph

    Like This: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vehicula tincidunt libero, id aliquam quam maximus eget. Maecenas consequat neque risus, vitae pellentesque ligula rhoncus aliquet. Vivamus pretium quam accumsan velit aliquam, vel pharetra lorem imperdiet.

    Donec tempor est sit amet congue convallis. Suspendisse potenti. Donec molestie ex at nibh eleifend commodo et et nunc. Integer interdum fringilla ex ut cursus.

5. That's it!

```
1. Sublists are quite straightforward
    * There can be Unordered sublists
2. And ordered ones
    1. Like this
    2. and this
3. Now...
    * To create a _Sublist_,
    * All you need is to _indent_.
        * And as with **Block Quotes**
            * You can ~~cannot~~ **nest** _Sublists_
                * And **use _Markdown_**
4. The same works with a Paragraph

    Like This: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vehicula tincidunt libero, id aliquam quam maximus eget. Maecenas consequat neque risus, vitae pellentesque ligula rhoncus aliquet. Vivamus pretium quam accumsan velit aliquam, vel pharetra lorem imperdiet.

    Donec tempor est sit amet congue convallis. Suspendisse potenti. Donec molestie ex at nibh eleifend commodo et et nunc. Integer interdum fringilla ex ut cursus.

5. That's it!
```

_Note:_ You can create sublists and paragraphs with only one _(extra)_ space; however, it is recommended that you use indents instead, for organization and visual intent.

### Links:

The most basic way to create a link is using angled brackets `<>`

<https://github.com>
`<https://github.com>`

You can create them without the angled brackets too, making sure to use `https://`, but it is recommended that you do so.

You can add titles to links (much like a standard hyperlink) using the standard link format `[title](link)` in-line reference:

[GitHub Website Click Here](https://github.com)
`[GitHub Website Click Here](https://github.com)`

You can also keep your links in the references.

You can access [GitHub] by clicking the hyperlink [here][GitHub]

Here are a few sources cited:

- [Some Search Engine][1].
- [Some Better Search Engine][2]. It's true, they don't track you.
- [Very Reliable Source][3] because it's the _vox populi_.

<!-- References -->
[GitHub]: https://github.com
[1]: https://google.com
[2]: https://duckduckgo.com
[3]: https://en.wikipedia.org

```
You can access [GitHub] by clicking the hyperlink [here][GitHub]

Here are a few sources cited:

- [Some Search Engine][1]
- [Some Better Search Engine][2]. It's true, they don't track you.
- [Very Reliable Source][3] because it's the _vox populi_

<!-- References -->
[GitHub]: https://github.com
[1]: https://google.com
[2]: https://duckduckgo.com
[3]: https://en.wikipedia.org
```

Notice how you didn't see the comments and references, there will be more on that later.

Again, notice the three ways to create a link reference–a hyperlink without directly attaching the URL.
1. Direct reference: `[GitHub]` and then set `[GitHub]: https://GitHub.com`. In some implementations of markdown, you will have to keep the second square bracket `[]` even if it is empty, as such: `[GitHub][]`.

2. Numbered Reference: `[GitHub Here][1]` and then set `[1]: https://GitHub.com`

3. Indirect Reference: `[Content][GitHub]` with `[GitHub]: https://GitHub.com`

You can attach these references anywhere, but it is recommended to list these links in a central location (making sure to use comments and describe each one) or at the end of every section for easier updating of links. Good code ethic is **very** important.

### Images:

Image attachment methods are very useful to know.
Here are a few examples:

![alt text: Gitgub](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png "Official GitHub Logo")
![alt text: Penguin](penguin.jpg)

```
![alt text: Gitgub](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png "Official GitHub Logo")
![alt text: Penguin](penguin.jpg)
```

Notes:
- the [alt text] is for visual accessibility, it is also displayed when internet conditions are insufficient to load the image.
- The first example is of accessing an image with an URL, the second example is of accessing a local image using _relative path_ (also located in this folder of this repository). Be aware that both of them have pros and cons.

Again, there are also indirect ways to reference and access images.

![alt text: GitHub][GitHub Logo]
![alt text: Penguin][4]

<!-- Images -->
[GitHub Logo]: https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png
[4]: penguin.jpg

```
![alt text: GitHub][GitHub Logo]
![alt text: Penguin][4]

<!-- Images -->
[GitHub Logo]: https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png
[4]: penguin.jpg
```

Another reminder is that you want to make sure your references are centralized and organized so that you don't accidentally use a reference twice (as you might have guessed, it won't work).

### Backslash Escapes:

These may not be as fun, but they are just as important for you to utilize markdown the way you envision.

In short, we talked about some other special symbols, like the hash (#) for headings, asterisk (\*), minus (-), plus (+), and numbers (1., 2., 3., _et cetera_) for lists, brackets \<>\[]\() for URLS, and the exclamation mark (!) for pictures. Despite their utility within the markdown format, you will still want to use them normally (without activating the markdown code).

To do that, you want to use the backslash (\\).

Here is a list of all symbols that the backslash works on (_id est_ those that have escape sequences):

\\ – Backslash

\` – Backtick

\* - Asterisk

\_ – Underscore

\{ \} – Curly Braces

\[ \] – Square Brackets

\( \) – Parentheses

\# – Hash Mark

\+ – Plus Sign

\- – Hyphen (Minus Sign)

\. – Dot (Period/Fullstop)

\! – Exclamation Mark

And in code:

```
\\ – Backslash

\` – Backtick

\* - Asterisk

\_ – Underscore

\{ \} – Curly Braces

\[ \] – Square Brackets

\( \) – Parentheses

\# – Hash Mark

\+ – Plus Sign

\- – Hyphen (Minus Sign)

\. – Dot (Period/Fullstop)

\! – Exclamation Mark
```

As seen above, these are the escape sequences. Although most of these sequences won't be needed most of the time, it's always good to know them, in case you ever run into a special case where you need them, it saves you the annoying debugging process.

### Tables:

Below is a basic Markdown table.

| Title | Col. A  | Col. B  |
|------:|:-------:|:--------|
| Row 1 | Cell 1A | Cell 1B |
| Row 2 | Cell 2A | Cell 2B |
| Row 3 | Cell 3A | Cell 3B |

```
| Title | Col. A  | Col. B  |
|------:|:-------:|:--------|
| Row 1 | Cell 1A | Cell 1B |
| Row 2 | Cell 2A | Cell 2B |
| Row 3 | Cell 3A | Cell 3B |
```

As you can see in the raw code, this is considered a pretty table.
> Beautiful is better than ugly.

<div style="text-align: right">
- Line 1 of Stanza 1 of the <b><a href="https://www.python.org/dev/peps/pep-0020/">Zen of Python</a></b>
</div>
<br>

But as you will see, not all tables are created equal. There are much easier, simpler, faster (and perhaps uglier) ways to create tables.

Table | Col1 | Col2
-:|:-|:-:
This | Still | Works
`so` | _**does**_ | [Markdown][GitHub] |

```
Table | Col1 | Col2
-:|:-|:-:
This | Still | Works
`so` | _**does**_ | [Markdown][GitHub] |
```

This is not a "beautiful" table, but it's a simple one.

> Simplicity is the ultimate sophistication.

<div style="text-align: right">
- Leonardo Da Vinci
</div>
<br>

> Simple is better than complex.
>
> Complex is better than complicated.

<div style="text-align: right">
- Lines 3-4 of Stanza 1 of the <b><a href="https://www.python.org/dev/peps/pep-0020/">Zen of Python</a></b>
</div>
<br>

This really goes to show, **simplicity > sophistication > beauty**. A key for success in your way of life and your programming ability alike.

Now, the spaces are between the text and the pipelines (|) are not required, so you can have `Table|Col1|Col2`; however the spaces are preferred for visual intent – _and this is for readability and clarity_.

Lastly, a few things to note:

The second column of the table defines the table (makes Markdown recognize it) and also sets the text alignment within the cells underneath the title. (_The Title Row and Definition Row are mandatory for this to work_, if you don't want it, forget about the ease of Markdown and try HTML)
- `-` sets the text alignment to `justify` or the default setting
- `:-` sets the text alignment to `left`
- `-:` sets the text alignment to `right`
- `:-:` sets the text alignment to `center`

### Comments:

In many other coding languages that have syntax more complex than Markdown, creating a comment (a statement or note that cannot be seen in the output–it stays in the _raw_ code) is as easy as using a hash (\#) and then a Space for style. However, it is not as easy in Markdown.

In Markdown, there are two ways to create a comment. One of which is native to Markdown, this may be intuitive, but this is for you if you are a purist markdown user and would not like to employ HTML in your code. The other, in my opinion, is more aesthetically pleasing, and easier to remember. Have a look at both and decide for yourself.

<br>

Markdown Version:

`[//]: # (Insert Comment Here)`

There are other variants of this Markdown-native comment; however, this is the most platform independent (on various Markdown implementations). Keep the brackets when you replace it with your own comment.

And the HTML Version:

`<!-- Comment Goes Here -->`

This one looks much cleaner than the former, making it easier to understand by readers.

<br>

Commenting your code is very important. However, with Markdown, it is _slightly_ less important because Markdown does not require much code. However, when you do use code, as in labeling References, try to leave a comment so you or someone else reading your code will understand it in the future.

### Code Blocks:

The best part about markdown is that you can directly write code in the format that your terminal emulator or IDE would see it. This is extremely easy, as all you need are the handy back ticks (\` \`).

`Insert Code Here`
\`Insert Code Here\`

And if you are trying to type one out, for some reason, use the backslash (escape sequence): \\\`

Sometimes, you need bigger blocks of code. This can be achieved by indenting four spaces (or a tab) or using these triple back ticks.
````
```
````

the latter is preferred because it is more explicit.

> Explicit is better than implicit.

<div style="text-align: right">
- Line 2 of Stanza 1 of the <b><a href="https://www.python.org/dev/peps/pep-0020/">Zen of Python</a></b>
</div>
<br>

And it is confused less with normal text.

To use it, make sure the triple back ticks are not in the same line with anything else, and put the code in the lines in between.

```
[user@computer ~]$ which python3
[user@computer ~]$ python3 --version
[user@computer ~]$ sudo -H pip3 install pygame
```

The code:

````
```
[user@computer ~]$ which python3
[user@computer ~]$ python3 --version
[user@computer ~]$ sudo -H pip3 install pygame
```
````

And if you're wondering how I typed the triple back ticks (because it is very hard), I did it using quadruple back ticks, since it is of a higher order and will override the triple back ticks.
`````
````
`````
And, I typed the quadruple back ticks with quintuple back ticks, you get the drill.
`````
````
```
Some Code Here
```
````
`````

# GitHub Flavored Markdown
Reference: [GitHub Markdown Guide](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

Here are some interesting features unique to GitHub Markdown. Note that they will _**not**_ work on a Markdown platform other than GitHub's

### Username Mentions:

First of all, you can \@ someone you want. This is mostly used in comments and there isn't much to say about it. You can also mention a Team within an Organization.

When you're not trying to \@ somebody, try sticking a \\ (Backslash) on it. Remember, when in doubt, try sticking a \\ on whatever symbol you are dealing with. It doesn't always work, but it's a good start.

Next time when you make a comment, try mentioning someone.

### Issue References:

This one isn't much different as mentioning people.

You can refer to pull requests or issues with `#1` or `repository#1`/`repository/directory#1` where `#1` is the number of the request.

### Task Lists:

Now, task lists are quite useful. But as much as you would like to tick them on the screen when you are looking at them to give yourself the gratification of ticking off a task, you must edit these task checkmarks in code. Here is an example task list.

- [x] Write run.py
- [ ] Update libraries
- [ ] Review pull requests

```
- [x] Write run.py
- [ ] Update libraries
- [ ] Review pull requests
```

As seen above, writing `- [ ]` _with a space between the brackets_ will create an unfinished task, while `- [x]` with a lowercase 'x' in the brackets will create a checked/finished task.

You can space these lists out with newlines:

- [x] Write run.py

- [x] Update libraries

- [x] Review pull requests

```
- [x] Write run.py

- [x] Update libraries

- [x] Review pull requests
```

As you can see, I have been really productive today. I finished those tasks while writing about task lists.

### Code Highlighting:

Here comes the final useful bit about GitHub's implementation of Markdown.

When you use code blocks, you are able to highlight and style the code **as if** it was written in an IDE. GitHub has language support for many programming languages and all it takes is to write the name of your programming language next to the opening triple back ticks to implement stylizing.

You may become too attached to this and find it difficult to use another Markdown implementation without this feature because it indeed is very useful when dealing with and displaying code.

We'll use the example from the Block Quotes section (Python):

Unhighlighted:
```
import math as m
print('happy', str(m.pi), 'day')
def foo(bar):
    print(f"Foo {bar}!")

print(foo('Bar'))
```
Highlighted:
```Python
import math as m
print('happy', str(m.pi), 'day')
def foo(bar):
    print(f"Foo {bar}!")

print(foo('Bar'))
```

Code for highlighting code blocks:
````
```Python
import math as m
print('happy', str(m.pi), 'day')
def foo(bar):
    print(f"Foo {bar}!")

print(foo('Bar'))
```
````

Just replace `bash` with whatever language your code is in.

But remember, don't mis-stylize your code. I have seen this countless times, when people didn't bother separating their code from their comments/miscellaneous information, the the coloring scheme goes all wrong. That's worse than not having highlighting at all. So please, remember to format your code correctly when highlighting code blocks.

# HTML

##### A bit on HTML.

HTML is not all that useful in Markdown because many of Markdown's native functions were meant to replace HTML as a simpler format. However, by aggressively simplifying HTML from a coding language to more of a text-based markup language causes it to lose some details and functionalities. As a remedy, you are still able to execute any HTML code you please inside of Markdown, and just use Markdown where if is simpler and achieves the same functionality as HTML.

### HTML Classes and Markdown Applicability

So, first, we have the understand the harmonious relationship between Markdown and HTML. Of course, check out [this link][HTML] for more on the topic of HTML integration and Markdown. This doesn't require any substantial knowledge of HTML, however. You just have to understand the two types of HTML tags–*span-level tags and block-level tags*. Span-level tags, as the name suggests, spans large segments of code or text. While block-level tags specify a specific block or object. Technically speaking, it would be better to use XHTML with Markdown as Markdown compiles in XHTML; However, I have not run into any issues with normal HTML and GitHub's implementation of Markdown. I will still provide both for the following tags.

In Markdown, Markdown within span-level are still compiled normally. Span-level tags include: \<span> \<cite> and \<del>

And Markdown within block-level tags _**will not**_ be executed. Block-level tags include: \<div>, \<table>, \<pre>, and \<p>. They also have to be separated from other lines (*you know why*, refer to HTML at the beginning). Fortunately, Markdown will not add unwanted \<p> tags around other block-level HTML tags, which contributes a significant portion to sustaining their harmonious relationship.

In this section, I will be going over some HTML concepts that are useful towards Markdown.

### Newlines and HTML Tag `<br>`

Read more about this HTML tag [here][br_tag].

Remember when I said that you can only get newlines by double spacing your code? Well, there is a lazier way, you just have to add two additional spaces at the end of your code and, _voila_, you get a new line. That is acceptable syntax in Markdown, or else it wouldn't exist, but I wouldn't recommend it because spaces aren't visible and invisible spaces won't help with your code's readability.

Well, there is also a third, _better_ way. It doesn't necessary have to replace Markdown's method, but it can come in handy when trying to make code compact or when you need multiple newlines. This tag is \<br>, or Break Line. In XHTML, the \<br> tag has to be closed properly, resulting in \<br />

Review:

HTML: `<br>`

XHTML: `<br />`

Function: Breaks a line

<!-- There will be more added here -->

# Emojis

And lastly, the thing we love the most. You can find the ~~same~~ list of emojis [here][emojis]
<!-- I won't be implementing the list in the markdown sheet at the moment, it is too large, and easier to access directly from the website-->
<!-- But you're welcome to edit this and put your favorite emojis in-->

## The End.
Congratulations! You've made it to the end.
Now, if you're up to it, look at this page again but select the "raw" mode on GitHub (top-right corner)
There are no easter eggs, but you'll get to see how this document is made, which will help solidify you accumulated knowledge on Markdown.

<!-- References -->
[HTML]: https://daringfireball.net/projects/markdown/syntax
[emojis]: https://www.emoji-cheat-seet.com
[br_tag]: https://www.w3schools.com/tags/tag_br.asp

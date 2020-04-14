# Markdown Collection
#### A complete list of Markdown Features

## Purpose:
* As a guide for people new to Markdown–a quick and powerful way to format, stylize, and decorate plain text for graphics.
* To list all the features of Markdown for reference.

### A Quick Note on HTML in Markdown (Preface)

There are a few crucial things to know about Markdown.

The first is that Markdown is a straightforward and powerful simplification of HTML. This means that some HTML attributes will apply to it.

And it is important to remember, if you are using a raw editor to edit markdown (like I am), that leaving an empty line between two lines (of text or otherwise) will tell the compiler to wrap the text in \<p>\</p>.

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
And large, formatted code blocks too
import math as m
print(str(m.pi))
```

```
> Block Quote.
>
>> Nested Block Quote.
>>
>>> Can be nested multiple times.
>
>`Can have code blocks within them`
>
>```Python
And large, formatted code blocks too
import math as m
print(str(m.pi))
‎```
```

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

[Github Website Click Here](https://github.com)
`[Github Website Click Here](https://github.com)`

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
You can access [Github] by clicking the hyperlink [here][GitHub]

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
1. Direct reference: `[GitHub]` and then set `[GitHub]: https://GitHub.com`.

2. Numbered Reference: `[GitHub Here][1]` and then set `[1]: https://GitHub.com`

3. Indirect Reference: `[Content][GitHub]` with `[GitHub]: https://GitHub.com`

You can attach these references anywhere, but it is recommended to list these links in a central location (making sure to use comments and describe each one) or at the end of every section for easier updating of links. Good code ethic is **very** important

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
- The first example is of accessing an image with an URL, the second example is of accessing a local image (also located in this folder of this repository). Be aware that both of them have pros and cons.

Again, there are also indirect ways to reference and access images.

![alt text: Github][GitHub Logo]
![alt text: Penguin][4]

<!-- Images -->
[GitHub Logo]: https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png
[4]: penguin.jpg

```
![alt text: Github][GitHub Logo]
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



### Tables:
### Comments:

# GitHub Flavored Markdown
Reference: [Github Markdown Guide](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
### Username Mentions:
### Issue References:
### Code Blocks:



<!-- References -->
[HTML]: https://daringfireball.net/projects/markdown/syntax

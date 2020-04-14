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
Heading 2
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
<br />

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
<br />

> Simple is better than complex.
>
> Complex is better than complicated.

<div style="text-align: right">
- Lines 3-4 of Stanza 1 of the <b><a href="https://www.python.org/dev/peps/pep-0020/">Zen of Python</a></b>
</div>
<br />

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

<br />

Markdown Version:

`[//]: # (Insert Comment Here)`

There are other variants of this Markdown-native comment; however, this is the most platform independent (on various Markdown implementations). Keep the brackets when you replace it with your own comment.

And the HTML Version:

`<!-- Comment Goes Here -->`

This one looks much cleaner than the former, making it easier to understand by readers.

<br />

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
<br />

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

And lastly, the thing we love the most. You can find the ~~same~~ list of emojis [here][emojis]. The categorization of emojis come from [itakyang's emoji-cheat-sheet][emojis_categorization]

As with many other platforms, the syntax for an emoji is \:emoji_name\:

Table of Emojis:

#### Face Smiling
Icon | Short Code
:-:|:-
:grinning: | `:grinning:`
:smiley: | `:smiley:`
:smile: | `:smile:`
:grin: | `:grin:`
:laughing: | `:laughing:` <br /> `:satisfied:`
:sweat_smile: | `:sweat_smile:`
:rofl: | `:rofl:`
:joy: | `:joy:`
:slightly_smiling_face: | `:slightly_smiling_face:`
:upside_down_face: | `:upside_down_face:`
:wink: | `:wink:`
:blush: | `:blush:`
:innocent: | `:innocent:`

#### Face Affection
Icon | Short Code
:-:|:-
:heart_eyes: | `:heart_eyes:`
:kissing_heart: | `:kissing_heart:`
:kissing: | `:kissing:`
:relaxed: | `:relaxed:`
:kissing_closed_eyes: | `:kissing_closed_eyes:`
:kissing_smiling_eyes: | `:kissing_smiling_eyes:`

#### Face Tongue
Icon | Short Code
:-:|:-
:yum: | `:yum:`
:stuck_out_tongue: | `:stuck_out_tongue:`
:stuck_out_tongue_winking_eye: | `:stuck_out_tongue_winking_eye:`
:stuck_out_tongue_closed_eyes: | `:stuck_out_tongue_closed_eyes:`
:money_mouth_face: | `:money_mouth_face:`

#### Face Hand
Icon | Short Code
:-:|:-
:hugs: | `:hugs:`
:thinking: | `:thinking:`

#### Face Neutral
Icon | Short Code
:-:|:-
:zipper_mouth_face: | `:zipper_mouth_face:`
:neutral_face: | `:neutral_face:`
:expressionless: | `:expressionless:`
:no_mouth: | `:no_mouth:`
:smirk: | `:smirk:`
:unamused: | `:unamused:`
:roll_eyes: | `:roll_eyes:`
:grimacing: | `:grimacing:`
:lying_face: | `:lying_face:`

#### Face Sleepy
Icon | Short Code
:-:|:-
:relieved: | `:relieved:`
:pensive: | `:pensive:`
:sleepy: | `:sleepy:`
:drooling_face: | `:drooling_face:`
:sleeping: | `:sleeping:`

#### Face Unwell
Icon | Short Code
:-:|:-
:mask: | `:mask:`
:face_with_thermometer: | `:face_with_thermometer:`
:face_with_head_bandage: | `:face_with_head_bandage:`
:nauseated_face: | `:nauseated_face:`
:sneezing_face: | `:sneezing_face:`
:dizzy_face: | `:dizzy_face:`

#### Face Hat
Icon | Short Code
:-:|:-
:cowboy_hat_face: | `:cowboy_hat_face:`

#### Face Glasses
Icon | Short Code
:-:|:-
:sunglasses: | `:sunglasses:`
:nerd_face: | `:nerd_face:`

#### Face Negative
Icon | Short Code
:-:|:-
:confused: | `:confused:`
:worried: | `:worried:`
:slightly_frowning_face: | `:slightly_frowning_face:`
:frowning_face: | `:frowning_face:`
:open_mouth: | `:open_mouth:`
:hushed: | `:hushed:`
:astonished: | `:astonished:`
:flushed: | `:flushed:`
:frowning: | `:frowning:`
:anguished: | `:anguished:`
:fearful: | `:fearful:`
:cold_sweat: | `:cold_sweat:`
:disappointed_relieved: | `:disappointed_relieved:`
:cry: | `:cry:`
:sob: | `:sob:` | :scream:
`:scream:`
:confounded: | `:confounded:`
:persevere: | `:persevere:`
:disappointed: | `:disappointed:`
:sweat: | `:sweat:`
:weary: | `:weary:`
:tired_face: | `:tired_face:`

#### Face Constume
Icon | Short Code
:-:|:-
:triumph: | `:triumph:`
:pout: | `:pout:` <br /> `:rage:`
:angry: | `:angry:`
:smiling_imp: | `:smiling_imp:`
:imp: | `:imp:`
:skull: | `:skull:`
:skull_and_crossbones: | `:skull_and_crossbones:`

#### Cat Face
Icon | Short Code
:-:|:-
:smiley_cat: | `:smiley_cat:`
:smile_cat: | `:smile_cat:`
:joy_cat: | `:joy_cat:`
:heart_eyes_cat: | `:heart_eyes_cat:`
:smirk_cat: | `:smirk_cat:`
:kissing_cat: | `:kissing_cat:`
:scream_cat: | `:scream_cat:`
:crying_cat_face: | `:crying_cat_face:`
:pouting_cat: | `:pouting_cat:`

#### Monkey Face
Icon | Short Code
:-:|:-
:see_no_evil: | `:see_no_evil:`
:hear_no_evil: | `:hear_no_evil:`
:speak_no_evil: | `:speak_no_evil:`

#### Emotion
Icon | Short Code
:-:|:-
:kiss: | `:kiss:`
:love_letter: | `:love_letter:`
:cupid: | `:cupid:`
:gift_heart: | `:gift_heart:`
:sparkling_heart: | `:sparkling_heart:`
:heartpulse: | `:heartpulse:`
:heartbeat: | `:heartbeat:`
:revolving_hearts: | `:revolving_hearts:`
:two_hearts: | `:two_hearts:`
:heart_decoration: | `:heart_decoration:`
:heavy_heart_exclamation: | `:heavy_heart_exclamation:`
:broken_heart: | `:broken_heart:`
:heart: | `:heart:`
:yellow_heart: | `:yellow_heart:`
:green_heart: | `:green_heart:`
:blue_heart: | `:blue_heart:`
:purple_heart: | `:purple_heart:`
:black_heart: | `:black_heart:`
:100: | `:100:`
:anger: | `:anger:`
:boom: | `:boom:` <br /> `:collision:`
:dizzy: | `:dizzy:`
:sweat_drops: | `:sweat_drops:`
:dash: | `:dash:`
:hole: | `:hole:`
:bomb: | `:bomb:`
:speech_balloon: | `:speech_balloon:`
:eye_speech_bubble: | `:eye_speech_bubble:`
:right_anger_bubble: | `:right_anger_bubble:`
:thought_balloon: | `:thought_balloon:`
:zzz: | `:zzz:`

===

#### Hand
Icon | Short Code
:-:|:-
:wave: | `:wave:`
:raised_back_of_hand: | `:raised_back_of_hand:`
:raised_hand_with_fingers_splayed: | `:raised_hand_with_fingers_splayed:`
:hand: | `:hand:` <br /> `:raised_hand:`
:vulcan_salute: | `:vulcan_salute:`
:ok_hand: | `:ok_hand:`
:v: | `:v:`
:crossed_fingers: | `:crossed_fingers:`
:metal: | `:metal:`
:call_me_hand: | `:call_me_hand:`
:point_left: | `:point_left:`
:point_right: | `:point_right:`
:point_up_2: | `:point_up_2:`
:fu: | `:fu:` <br /> `:middle_finger:`
:point_down: | `:point_down:`
:point_up: | `:point_up:`
:+1: | `:+1:` <br /> `:thumbsup:`
:-1: | `:-1:` <br /> `:thumbsdown:`
:fist: | `:fist:` <br /> `:fist_raised:`
:facepunch: | `:facepunch:` <br /> `:fist_oncoming:` <br /> `:punch:`
:fist_left: | `:fist_left:`
:fist_right: | `:fist_right:`
:clap: | `:clap:`
:raised_hands: | `:raised_hands:`
:open_hands: | `:open_hands:`
:handshake: | `:handshake:`
:pray: | `:pray:`
:writing_hand: | `:writing_hand:`
:nail_care: | `:nail_care:`
:selfie: | `:selfie:`

#### Body Parts
Icon | Short Code
:-:|:-
:point_left: | `:point_left:`
:point_right: | `:point_right:`
:point_up_2: | `:point_up_2:`
:fu: | `:fu:` <br /> `:middle_finger:`
:point_down: | `:point_down:`
:point_up: | `:point_up:`
:+1: | `:+1:` <br /> `:thumbsup:`
:-1: | `:-1:` <br /> `:thumbsdown:`
:fist: | `:fist:` <br /> `:fist_raised:`
:facepunch: | `:facepunch:` <br /> `:fist_oncoming:` <br /> `:punch:`
:fist_left: | `:fist_left:`
:fist_right: | `:fist_right:`
:clap: | `:clap:`
:raised_hands: | `:raised_hands:`
:open_hands: | `:open_hands:`
:handshake: | `:handshake:`
:pray: | `:pray:`
:writing_hand: | `:writing_hand:`
:nail_care: | `:nail_care:`
:selfie: | `:selfie:`

#### Person
Icon | Short Code
:-:|:-
:boy: | `:boy:` | :girl: | `:girl:`
:blonde_man: | `:blonde_man:` <br /> `:person_with_blond_hair:` | :blonde_woman: | `:blonde_woman:`
:man: | `:man:` | :woman: | `:woman:`
:older_man: | `:older_man:` | :older_woman: | `:older_woman:` |
:baby: | `:baby:`

#### Person Gesture
Icon | Short Code | Icon | Short Code
:-:|:-|:-:|:-
:frowning_woman: | `:frowning_woman:` <br /> `:person_frowning:` | :frowning_man: | `:frowning_man:`
:person_with_pouting_face: | `:person_with_pouting_face:` <br /> `:pouting_woman:` | :pouting_man: | `:pouting_man:`
:ng_woman: | `:ng_woman:` <br /> `:no_good:` <br /> `:no_good_woman:` | :ng_man: | `:ng_man:` <br /> `:no_good_man:`
:ok_woman: | `:ok_woman:` | :ok_man: | `:ok_man:`
:information_desk_person: | `:information_desk_person:` <br /> `:sassy_woman:` <br /> `:tipping_hand_woman:` | :sassy_man: | `:sassy_man:` <br /> `:tipping_hand_man:`
:raising_hand: | `:raising_hand:` <br /> `:raising_hand_woman:` | :raising_hand_man: | `:raising_hand_man:`
:bow: | `:bow:` <br /> `:bowing_man:` | :bowing_woman: | `:bowing_woman:`
:man_facepalming: | `:man_facepalming:` | :woman_facepalming: | `:woman_facepalming:`
:man_shrugging: | `:man_shrugging:` | :woman_shrugging: | `:woman_shrugging:`

#### Person Role
Icon | Short Code | Icon | Short Code
:-:|:-|:-:|:-
:man_health_worker: | `:man_health_worker:` | :woman_health_worker: | `:woman_health_worker:`
:man_student: | `:man_student:` | :woman_student: | `:woman_student:`
:man_teacher: | `:man_teacher:` | :woman_teacher: | `:woman_teacher:`
:man_judge: | `:man_judge:` | :woman_judge: | `:woman_judge:`
:man_farmer: | `:man_farmer:` | :woman_farmer: | `:woman_farmer:`
:man_cook: | `:man_cook:` | :woman_cook: | `:woman_cook:`
:man_mechanic: | `:man_mechanic:` | :woman_mechanic: | `:woman_mechanic:`
:man_factory_worker: | `:man_factory_worker:` | :woman_factory_worker: | `:woman_factory_worker:`
:man_office_worker: | `:man_office_worker:` | :woman_office_worker: | `:woman_office_worker:`
:man_scientist: | `:man_scientist:` | :woman_scientist: | `:woman_scientist:`
:man_technologist: | `:man_technologist:` | :woman_technologist: | `:woman_technologist:`
:man_singer: | `:man_singer:` | :woman_singer: | `:woman_singer:`
:man_artist: | `:man_artist:` | :woman_artist: | `:woman_artist:`
:man_pilot: | `:man_pilot:` | :woman_pilot: | `:woman_pilot:`
:man_astronaut: | `:man_astronaut:` | :woman_astronaut: | `:woman_astronaut:`
:man_firefighter: | `:man_firefighter:` | :woman_firefighter: | `:woman_firefighter:`
:cop: | `:cop:` <br /> `:policeman:` | :policewoman: | `:policewoman:`
:detective: | `:detective:` <br /> `:male_detective:` | :female_detective: | `:female_detective:`
:guardsman: | `:guardsman:` | :guardswoman: | `:guardswoman:`
:construction_worker: | `:construction_worker:` <br /> `:construction_worker_man:` | :construction_worker_woman: | `:construction_worker_woman:`
:prince: | `:prince:` | :princess: | `:princess:`
:man_with_turban: | `:man_with_turban:` | :woman_with_turban: | `:woman_with_turban:`
:man_with_gua_pi_mao: | `:man_with_gua_pi_mao:` | :man_in_tuxedo: | `:man_in_tuxedo:`
:bride_with_veil: | `:bride_with_veil:` | :pregnant_woman: | `:pregnant_woman:`

#### Fantasy Characters
Icon | Short Code
:-:|:-|
:angel: | `:angel:`
:santa: | `:santa:`
:mrs_claus: | `:mrs_claus:`

#### People Activities
Icon | Short Code | Icon | Short Code
:-:|:-|:-:|:-
:massage_man: | `:massage_man:` | :massage: | `:massage:` <br /> `:massage_woman:`
:haircut_man: | `:haircut_man:` | :haircut: | `:haircut:` <br /> `:haircut_woman:`
:walking: | `:walking:` <br /> `:walking_man:` | :walking_woman: | `:walking_woman:`
:runner: | `:runner:` <br /> `:running:` <br /> `:running_man:` | :running_woman: | `:running_woman:`
:dancer: | `:dancer:` | :man_dancing: | `:man_dancing:`
:dancers: | `:dancers:` <br /> `:dancing_women:` | :dancing_men: | `:dancing_men:`
:business_suit_levitating: | `:business_suit_levitating:`

#### People Sports
Icon | Short Code | Icon | Short Code
:-:|:-|:-:|:-
:person_fencing: | `:person_fencing:` | :horse_racing: | `:horse_racing:`
:skier: | `:skier:` | :snowboarder: | `:snowboarder:`
:golfing_man: | `:golfing_man:` | :golfing_woman: | `:golfing_woman:`
:surfer: | `:surfer:` <br /> `:surfing_man:` | :surfing_woman: | `:surfing_woman:`
:rowboat: | `:rowboat:` <br /> `:rowing_man:` | :rowing_woman: | `:rowing_woman:`
:swimmer: | `:swimmer:` <br /> `:swimming_man:` | :swimming_woman: | `:swimming_woman:`
:basketball_man: | `:basketball_man:` | :basketball_woman: | `:basketball_woman:`
:weight_lifting_man: | `:weight_lifting_man:` | :weight_lifting_woman: | `:weight_lifting_woman:`
:bicyclist: | `:bicyclist:` <br /> `:biking_man:` | :biking_woman: | `:biking_woman:`
:mountain_bicyclist: | `:mountain_bicyclist:` <br /> `:mountain_biking_man:` | :mountain_biking_woman: | `:mountain_biking_woman:`
:man_cartwheeling: | `:man_cartwheeling:` | :woman_cartwheeling: | `:woman_cartwheeling:`
:men_wrestling: | `:men_wrestling:` | :women_wrestling: | `:women_wrestling:`
:man_playing_water_polo: | `:man_playing_water_polo:` | :woman_playing_water_polo: | `:woman_playing_water_polo:`
:man_playing_handball: | `:man_playing_handball:` | :woman_playing_handball: | `:woman_playing_handball:`
:man_juggling: | `:man_juggling:` | :woman_juggling: | `:woman_juggling:`

#### Rest
Icon | Short Code
:-:|:-
:bath: | `:bath:`
:sleeping_bed: | `:sleeping_bed:`

#### Family
Icon | Short Code | Icon | Short Code
:-:|:-|:-:|:-
:two_women_holding_hands: | `:two_women_holding_hands:` | :couple: | `:couple:`
:two_men_holding_hands: | `:two_men_holding_hands:` | :couplekiss_man_woman: | `:couplekiss_man_woman:`
:couplekiss_man_man: | `:couplekiss_man_man:` | :couplekiss_woman_woman: | `:couplekiss_woman_woman:`
:couple_with_heart: | `:couple_with_heart:` <br /> `:couple_with_heart_woman_man:` | :couple_with_heart_man_man: | `:couple_with_heart_man_man:`
:couple_with_heart_woman_woman: | `:couple_with_heart_woman_woman:` | :family: | `:family:` <br /> `:family_man_woman_boy:`
:family_man_woman_girl: | `:family_man_woman_girl:` | :family_man_woman_girl_boy: | `:family_man_woman_girl_boy:`
:family_man_woman_boy_boy: | `:family_man_woman_boy_boy:` | :family_man_woman_girl_girl: | `:family_man_woman_girl_girl:`
:family_man_man_boy: | `:family_man_man_boy:` | :family_man_man_girl: | `:family_man_man_girl:`
:family_man_man_girl_boy: | `:family_man_man_girl_boy:` | :family_man_man_boy_boy: | `:family_man_man_boy_boy:`
:family_man_man_girl_girl: | `:family_man_man_girl_girl:` | :family_woman_woman_boy: | `:family_woman_woman_boy:`
:family_woman_woman_girl: | `:family_woman_woman_girl:` | :family_woman_woman_girl_boy: | `:family_woman_woman_girl_boy:`
:family_woman_woman_boy_boy: | `:family_woman_woman_boy_boy:` | :family_woman_woman_girl_girl: | `:family_woman_woman_girl_girl:`
:family_man_boy: | `:family_man_boy:` | :family_man_boy_boy: | `:family_man_boy_boy:`
:family_man_girl: | `:family_man_girl:` | :family_man_girl_boy: | `:family_man_girl_boy:`
:family_man_girl_girl: | `:family_man_girl_girl:` | :family_woman_boy: | `:family_woman_boy:`
:family_woman_boy_boy: | `:family_woman_boy_boy:` | :family_woman_girl: | `:family_woman_girl:`
:family_woman_girl_boy: | `:family_woman_girl_boy:` | :family_woman_girl_girl: | `:family_woman_girl_girl:`

#### Person Symbol
Icon | Short Code
:-:|:-
:speaking_head: | `:speaking_head:`
:bust_in_silhouette: | `:bust_in_silhouette:`
:busts_in_silhouette: | `:busts_in_silhouette:`
:footprints: | `:footprints:`

===

#### Animal Mammal
Icon | Short Code
:-:|:-
:monkey_face: | `:monkey_face:`
:monkey: | `:monkey:`
:gorilla: | `:gorilla:`
:dog: | `:dog:`
:dog2: | `:dog2:`
:poodle: | `:poodle:`
:wolf: | `:wolf:`
:fox_face: | `:fox_face:`
:cat: | `:cat:`
:cat2: | `:cat2:`
:lion: | `:lion:`
:tiger: | `:tiger:`
:tiger2: | `:tiger2:`
:leopard: | `:leopard:`
:horse: | `:horse:`
:racehorse: | `:racehorse:`
:unicorn: | `:unicorn:`
:deer: | `:deer:`
:cow: | `:cow:`
:ox: | `:ox:`
:water_buffalo: | `:water_buffalo:`
:cow2: | `:cow2:`
:pig: | `:pig:`
:pig2: | `:pig2:`
:boar: | `:boar:`
:pig_nose: | `:pig_nose:`
:ram: | `:ram:`
:sheep: | `:sheep:`
:goat: | `:goat:`
:dromedary_camel: | `:dromedary_camel:`
:camel: | `:camel:`
:elephant: | `:elephant:`
:rhinoceros: | `:rhinoceros:`
:mouse: | `:mouse:`
:mouse2: | `:mouse2:`
:rat: | `:rat:`
:hamster: | `:hamster:`
:rabbit: | `:rabbit:`
:rabbit2: | `:rabbit2:`
:chipmunk: | `:chipmunk:`
:bat: | `:bat:`
:bear: | `:bear:`
:koala: | `:koala:`
:panda_face: | `:panda_face:`
:feet: | `:feet:` <br /> `:paw_prints:`

#### Animal Bird
Icon | Short Code
:-:|:-
:turkey: | `:turkey:`
:chicken: | `:chicken:`
:rooster: | `:rooster:`
:hatching_chick: | `:hatching_chick:`
:baby_chick: | `:baby_chick:`
:hatched_chick: | `:hatched_chick:`
:bird: | `:bird:`
:penguin: | `:penguin:`
:dove: | `:dove:`
:eagle: | `:eagle:`
:duck: | `:duck:`
:owl: | `:owl:`

### Animal Amphibian
:frog: \: `:frog:`

#### Animal Reptile
Icon | Short Code
:-:|:-
:crocodile: | `:crocodile:`
:turtle: | `:turtle:`
:lizard: | `:lizard:`
:snake: | `:snake:`
:dragon_face: | `:dragon_face:`
:dragon: | `:dragon:`

#### Animal Marine
Icon | Short Code
:-:|:-
:whale: | `:whale:`
:whale2: | `:whale2:`
:dolphin: | `:dolphin:` <br /> `:flipper:`
:fish: | `:fish:`
:tropical_fish: | `:tropical_fish:`
:blowfish: | `:blowfish:`
:shark: | `:shark:`
:octopus: | `:octopus:`
:shell: | `:shell:`

#### Animal Bug
Icon | Short Code
:-:|:-
:snail: | `:snail:`
:butterfly: | `:butterfly:`
:bug: | `:bug:`
:ant: | `:ant:`
:bee: | `:bee:` <br /> `:honeybee:`
:beetle: | `:beetle:`
:spider: | `:spider:`
:spider_web: | `:spider_web:`
:scorpion: | `:scorpion:`

#### Plant Flower
Icon | Short Code
:-:|:-
:bouquet: | `:bouquet:`
:cherry_blossom: | `:cherry_blossom:`
:white_flower: | `:white_flower:`
:rosette: | `:rosette:`
:rose: | `:rose:`
:wilted_flower: | `:wilted_flower:`
:hibiscus: | `:hibiscus:`
:sunflower: | `:sunflower:`
:blossom: | `:blossom:`
:tulip: | `:tulip:`

#### Plant Other
Icon | Short Code
:-:|:-
:seedling: | `:seedling:`
:evergreen_tree: | `:evergreen_tree:`
:deciduous_tree: | `:deciduous_tree:`
:palm_tree: | `:palm_tree:`
:cactus: | `:cactus:`
:ear_of_rice: | `:ear_of_rice:`
:herb: | `:herb:`
:shamrock: | `:shamrock:`
:four_leaf_clover: | `:four_leaf_clover:`
:maple_leaf: | `:maple_leaf:`
:fallen_leaf: | `:fallen_leaf:`
:leaves: | `:leaves:`

===

#### Food Fruit
Icon | Short Code
:-:|:-
:grapes: | `:grapes:`
:melon: | `:melon:`
:watermelon: | `:watermelon:`
:mandarin: | `:mandarin:` <br /> `:orange:` <br /> `:tangerine:`
:lemon: | `:lemon:`
:banana: | `:banana:`
:pineapple: | `:pineapple:`
:apple: | `:apple:`
:green_apple: | `:green_apple:`
:pear: | `:pear:`
:peach: | `:peach:`
:cherries: | `:cherries:`
:strawberry: | `:strawberry:`
:kiwi_fruit: | `:kiwi_fruit:`
:tomato: | `:tomato:`

#### Food Vegetable
Icon | Short Code
:-:|:-
:avocado: | `:avocado:`
:eggplant: | `:eggplant:`
:potato: | `:potato:`
:carrot: | `:carrot:`
:corn: | `:corn:`
:hot_pepper: | `:hot_pepper:`
:cucumber: | `:cucumber:`
:mushroom: | `:mushroom:`
:peanuts: | `:peanuts:`
:chestnut: | `:chestnut:`

#### Food Prepared
Icon | Short Code
:-:|:-
:bread: | `:bread:`
:croissant: | `:croissant:`
:baguette_bread: | `:baguette_bread:`
:pancakes: | `:pancakes:`
:cheese: | `:cheese:`
:meat_on_bone: | `:meat_on_bone:`
:poultry_leg: | `:poultry_leg:`
:bacon: | `:bacon:`
:hamburger: | `:hamburger:`
:fries: | `:fries:`
:pizza: | `:pizza:`
:hotdog: | `:hotdog:`
:taco: | `:taco:`
:burrito: | `:burrito:`
:stuffed_flatbread: | `:stuffed_flatbread:`
:egg: | `:egg:`
:fried_egg: | `:fried_egg:`
:shallow_pan_of_food: | `:shallow_pan_of_food:`
:stew: | `:stew:`
:green_salad: | `:green_salad:`
:popcorn: | `:popcorn:`

#### Food Asian
Icon | Short Code
:-:|:-
:bento: | `:bento:`
:rice_cracker: | `:rice_cracker:`
:rice_ball: | `:rice_ball:`
:rice: | `:rice:`
:curry: | `:curry:`
:ramen: | `:ramen:`
:spaghetti: | `:spaghetti:`
:sweet_potato: | `:sweet_potato:`
:oden: | `:oden:`
:sushi: | `:sushi:`
:fried_shrimp: | `:fried_shrimp:`
:fish_cake: | `:fish_cake:`
:dango: | `:dango:`

#### Food Marine
Icon | Short Code
:-:|:-
:crab: | `:crab:`
:shrimp: | `:shrimp:`
:squid: | `:squid:`

#### Food Sweet
Icon | Short Code
:-:|:-
:icecream: | `:icecream:`
:shaved_ice: | `:shaved_ice:`
:ice_cream: | `:ice_cream:`
:doughnut: | `:doughnut:`
:cookie: | `:cookie:`
:birthday: | `:birthday:`
:cake: | `:cake:`
:chocolate_bar: | `:chocolate_bar:`
:candy: | `:candy:`
:lollipop: | `:lollipop:`
:custard: | `:custard:`
:honey_pot: | `:honey_pot:`

#### Drink
Icon | Short Code
:-:|:-
:baby_bottle: | `:baby_bottle:`
:milk_glass: | `:milk_glass:`
:coffee: | `:coffee:`
:tea: | `:tea:`
:sake: | `:sake:`
:champagne: | `:champagne:`
:wine_glass: | `:wine_glass:`
:cocktail: | `:cocktail:`
:tropical_drink: | `:tropical_drink:`
:beer: | `:beer:`
:beers: | `:beers:`
:clinking_glasses: | `:clinking_glasses:`
:tumbler_glass: | `:tumbler_glass:`

#### Dishware
Icon | Short Code
:-:|:-
:plate_with_cutlery: | `:plate_with_cutlery:`
:fork_and_knife: | `:fork_and_knife:`
:spoon: | `:spoon:`
:hocho: | `:hocho:` <br /> `:knife:`
:amphora: | `:amphora:`

===

#### Place Map
Icon | Short Code
:-:|:-
:earth_africa: | `:earth_africa:`
:earth_americas: | `:earth_americas:`
:earth_asia: | `:earth_asia:`
:globe_with_meridians: | `:globe_with_meridians:`
:world_map: | `:world_map:`
:japan: | `:japan:`

#### Place Geography
Icon | Short Code
:-:|:-
:mountain_snow: | `:mountain_snow:`
:mountain: | `:mountain:`
:volcano: | `:volcano:`
:mount_fuji: | `:mount_fuji:`
:camping: | `:camping:`
:beach_umbrella: | `:beach_umbrella:`
:desert: | `:desert:`
:desert_island: | `:desert_island:`
:national_park: | `:national_park:`

#### Place Building
Icon | Short Code
:-:|:-
:stadium: | `:stadium:`
:classical_building: | `:classical_building:`
:building_construction: | `:building_construction:`
:houses: | `:houses:`
:derelict_house: | `:derelict_house:`
:house: | `:house:`
:house_with_garden: | `:house_with_garden:`
:office: | `:office:`
:post_office: | `:post_office:`
:european_post_office: | `:european_post_office:`
:hospital: | `:hospital:`
:bank: | `:bank:`
:hotel: | `:hotel:`
:love_hotel: | `:love_hotel:`
:convenience_store: | `:convenience_store:`
:school: | `:school:`
:department_store: | `:department_store:`
:factory: | `:factory:`
:japanese_castle: | `:japanese_castle:`
:european_castle: | `:european_castle:`
:wedding: | `:wedding:`
:tokyo_tower: | `:tokyo_tower:`
:statue_of_liberty: | `:statue_of_liberty:` | |

#### Place Religious
Icon | Short Code
:-:|:-
:church: | `:church:`
:mosque: | `:mosque:`
:synagogue: | `:synagogue:`
:shinto_shrine: | `:shinto_shrine:`
:kaaba: | `:kaaba:`

#### Place Other
Icon | Short Code
:-:|:-
:fountain: | `:fountain:`
:tent: | `:tent:`
:foggy: | `:foggy:`
:night_with_stars: | `:night_with_stars:`
:cityscape: | `:cityscape:`
:sunrise_over_mountains: | `:sunrise_over_mountains:`
:sunrise: | `:sunrise:`
:city_sunset: | `:city_sunset:`
:city_sunrise: | `:city_sunrise:`
:bridge_at_night: | `:bridge_at_night:`
:hotsprings: | `:hotsprings:`
:carousel_horse: | `:carousel_horse:`
:ferris_wheel: | `:ferris_wheel:`
:roller_coaster: | `:roller_coaster:`
:barber: | `:barber:`
:circus_tent: | `:circus_tent:`

#### Transport Ground
Icon | Short Code
:-:|:-
:steam_locomotive: | `:steam_locomotive:`
:railway_car: | `:railway_car:`
:bullettrain_side: | `:bullettrain_side:`
:bullettrain_front: | `:bullettrain_front:`
:train2: | `:train2:`
:metro: | `:metro:`
:light_rail: | `:light_rail:`
:station: | `:station:`
:tram: | `:tram:`
:monorail: | `:monorail:`
:mountain_railway: | `:mountain_railway:`
:train: | `:train:`
:bus: | `:bus:`
:oncoming_bus: | `:oncoming_bus:`
:trolleybus: | `:trolleybus:`
:minibus: | `:minibus:`
:ambulance: | `:ambulance:`
:fire_engine: | `:fire_engine:`
:police_car: | `:police_car:`
:oncoming_police_car: | `:oncoming_police_car:`
:taxi: | `:taxi:`
:oncoming_taxi: | `:oncoming_taxi:`
:car: | `:car:` <br /> `:red_car:`
:oncoming_automobile: | `:oncoming_automobile:`
:blue_car: | `:blue_car:`
:truck: | `:truck:`
:articulated_lorry: | `:articulated_lorry:`
:tractor: | `:tractor:`
:racing_car: | `:racing_car:`
:motorcycle: | `:motorcycle:`
:motor_scooter: | `:motor_scooter:`
:bike: | `:bike:`
:kick_scooter: | `:kick_scooter:`
:busstop: | `:busstop:`
:motorway: | `:motorway:`
:railway_track: | `:railway_track:`
:oil_drum: | `:oil_drum:`
:fuelpump: | `:fuelpump:`
:rotating_light: | `:rotating_light:`
:traffic_light: | `:traffic_light:`
:vertical_traffic_light: | `:vertical_traffic_light:`
:stop_sign: | `:stop_sign:`
:construction: | `:construction:`

#### Transport Water
Icon | Short Code
:-:|:-
:anchor: | `:anchor:`
:boat: `:boat:` <br /> `:sailboat:`
:canoe: | `:canoe:`
:speedboat: | `:speedboat:`
:passenger_ship: | `:passenger_ship:`
:ferry: | `:ferry:`
:motor_boat: | `:motor_boat:`
:ship: | `:ship:`

#### Transport Air
Icon | Short Code
:-:|:-
:airplane: | `:airplane:`
:small_airplane: | `:small_airplane:`
:flight_departure: | `:flight_departure:`
:flight_arrival: | `:flight_arrival:`
:seat: | `:seat:`
:helicopter: | `:helicopter:`
:suspension_railway: | `:suspension_railway:`
:mountain_cableway: | `:mountain_cableway:`
:aerial_tramway: | `:aerial_tramway:`
:artificial_satellite: | `:artificial_satellite:`
:rocket: | `:rocket:`

DOENS'T BELONG HERE
:bellhop_bell: | `:bellhop_bell:`

#### Time
Icon | Short Code
:-:|:-
:hourglass: | `:hourglass:`
:hourglass_flowing_sand: | `:hourglass_flowing_sand:`
:watch: | `:watch:`
:alarm_clock: | `:alarm_clock:`
:stopwatch: | `:stopwatch:`
:timer_clock: | `:timer_clock:`
:mantelpiece_clock: | `:mantelpiece_clock:`

Icon | Short Code | Icon | Short Code
:-:|:- | :-:|:-
:clock12: | `:clock12:` | :clock1230: | `:clock1230:`
:clock1: | `:clock1:` | :clock130: | `:clock130:`
:clock2: | `:clock2:` | :clock230: | `:clock230:`
:clock3: | `:clock3:` | :clock330: | `:clock330:`
:clock4: | `:clock4:` | :clock430: | `:clock430:`
:clock5: | `:clock5:` | :clock530: | `:clock530:`
:clock6: | `:clock6:` | :clock630: | `:clock630:`
:clock7: | `:clock7:` | :clock730: | `:clock730:`
:clock8: | `:clock8:` | :clock830: | `:clock830:`
:clock9: | `:clock9:` | :clock930: | `:clock930:`
:clock10: | `:clock10:` | :clock1030: | `:clock1030:`
:clock11: | `:clock11:` | :clock1130: | `:clock1130:`

#### Sky and Weather
Icon | Short Code
:-:|:-
:new_moon: | `:new_moon:`
:waxing_crescent_moon: | `:waxing_crescent_moon:`
:first_quarter_moon: | `:first_quarter_moon:`
:moon: | `:moon:` <br /> `:waxing_gibbous_moon:`
:full_moon: | `:full_moon:`
:waning_gibbous_moon: | `:waning_gibbous_moon:`
:last_quarter_moon: | `:last_quarter_moon:`
:waning_crescent_moon: | `:waning_crescent_moon:`
:crescent_moon: | `:crescent_moon:`
:new_moon_with_face: | `:new_moon_with_face:`
:first_quarter_moon_with_face: | `:first_quarter_moon_with_face:`
:last_quarter_moon_with_face: | `:last_quarter_moon_with_face:`
:thermometer: | `:thermometer:`
:sunny: | `:sunny:`
:full_moon_with_face: | `:full_moon_with_face:`
:sun_with_face: | `:sun_with_face:`
:star: | `:star:`
:star2: | `:star2:`
:stars: | `:stars:`
:milky_way: | `:milky_way:`
:cloud: | `:cloud:`
:partly_sunny: | `:partly_sunny:`
:cloud_with_lightning_and_rain: | `:cloud_with_lightning_and_rain:`
:sun_behind_small_cloud: | `:sun_behind_small_cloud:`
:sun_behind_large_cloud: | `:sun_behind_large_cloud:`
:sun_behind_rain_cloud: | `:sun_behind_rain_cloud:`
:cloud_with_rain: | `:cloud_with_rain:`
:cloud_with_snow: | `:cloud_with_snow:`
:cloud_with_lightning: | `:cloud_with_lightning:`
:tornado: | `:tornado:`
:fog: | `:fog:`
:wind_face: | `:wind_face:`
:cyclone: | `:cyclone:`
:rainbow: | `:rainbow:`
:closed_umbrella: | `:closed_umbrella:`
:open_umbrella: | `:open_umbrella:`
:umbrella: | `:umbrella:`
:parasol_on_ground: | `:parasol_on_ground:`
:zap: | `:zap:`
:snowflake: | `:snowflake:`
:snowman_with_snow: | `:snowman_with_snow:`
:snowman: | `:snowman:`
:comet: | `:comet:`
:fire: | `:fire:`
:droplet: | `:droplet:`
:ocean: | `:ocean:`

===

#### Events
Icon | Short Code
:-:|:-
:jack_o_lantern: | `:jack_o_lantern:`
:christmas_tree: | `:christmas_tree:`
:fireworks: | `:fireworks:`
:sparkler: | `:sparkler:`
:sparkles: | `:sparkles:`
:balloon: | `:balloon:`
:tada: | `:tada:`
:confetti_ball: | `:confetti_ball:`
:tanabata_tree: | `:tanabata_tree:`
:bamboo: | `:bamboo:`
:dolls: | `:dolls:`
:flags: | `:flags:`
:wind_chime: | `:wind_chime:`
:rice_scene: | `:rice_scene:`
:ribbon: | `:ribbon:`
:gift: | `:gift:`
:reminder_ribbon: | `:reminder_ribbon:`
:tickets: | `:tickets:`
:ticket: | `:ticket:`


#### Achievements
Icon | Short Code
:-:|:-
:medal_military: | `:medal_military:`
:trophy: | `:trophy:`
:medal_sports: | `:medal_sports:`
:1st_place_medal: | `:1st_place_medal:`
:2nd_place_medal: | `:2nd_place_medal:`
:3rd_place_medal: | `:3rd_place_medal:`

#### Sports
Icon | Short Code
:-:|:-
:soccer: | `:soccer:`
:baseball: | `:baseball:`
:basketball: | `:basketball:`
:volleyball: | `:volleyball:`
:football: | `:football:`
:rugby_football: | `:rugby_football:`
:tennis: | `:tennis:`
:bowling: | `:bowling:`
:cricket: | `:cricket:`
:field_hockey: | `:field_hockey:`
:ice_hockey: | `:ice_hockey:`
:ping_pong: | `:ping_pong:`
:badminton: | `:badminton:`
:boxing_glove: | `:boxing_glove:`
:martial_arts_uniform: | `:martial_arts_uniform:`
:goal_net: | `:goal_net:`
:golf: | `:golf:`
:ice_skate: | `:ice_skate:`
:fishing_pole_and_fish: | `:fishing_pole_and_fish:`
:running_shirt_with_sash: | `:running_shirt_with_sash:`
:ski: | `:ski:`

#### Activities
Icon | Short Code
:-:|:-
:dart: | `:dart:`
:8ball: | `:8ball:`
:crystal_ball: | `:crystal_ball:`
:video_game: | `:video_game:`
:joystick: | `:joystick:`
:slot_machine: | `:slot_machine:`
:game_die: | `:game_die:`
:spades: | `:spades:`
:hearts: | `:hearts:`
:diamonds: | `:diamonds:`
:clubs: | `:clubs:`
:black_joker: | `:black_joker:`
:mahjong: | `:mahjong:`
:flower_playing_cards: | `:flower_playing_cards:`

#### Arts
Icon | Short Code
:-:|:-
:performing_arts: | `:performing_arts:`
:framed_picture: | `:framed_picture:`
:art: | `:art:`

===

#### Clothing
Icon | Short Code
:-:|:-
:eyeglasses: | `:eyeglasses:`
:dark_sunglasses: | `:dark_sunglasses:`
:necktie: | `:necktie:`
:shirt: | `:shirt:` <br /> `:tshirt:`
:jeans: | `:jeans:`
:dress: | `:dress:`
:kimono: | `:kimono:`
:bikini: | `:bikini:`
:womans_clothes: | `:womans_clothes:`
:purse: | `:purse:`
:handbag: | `:handbag:`
 :pouch: | `:pouch:`
:shopping: | `:shopping:`
:school_satchel: | `:school_satchel:`
:mans_shoe: | `:mans_shoe:` <br /> `:shoe:`
:athletic_shoe: | `:athletic_shoe:`
:high_heel: | `:high_heel:`
:sandal: | `:sandal:`
:boot: | `:boot:`
:crown: | `:crown:`
:womans_hat: | `:womans_hat:`
:tophat: | `:tophat:`
:mortar_board: | `:mortar_board:`
:rescue_worker_helmet: | `:rescue_worker_helmet:`
:prayer_beads: | `:prayer_beads:`
:lipstick: | `:lipstick:`
:ring: | `:ring:`
:gem: | `:gem:`

#### Sound
Icon | Short Code
:-:|:-
:mute: | `:mute:`
:speaker: | `:speaker:`
:sound: | `:sound:`
:loud_sound: | `:loud_sound:`
:loudspeaker: | `:loudspeaker:`
:mega: | `:mega:`
:postal_horn: | `:postal_horn:`
:bell: | `:bell:`
:no_bell: | `:no_bell:`

#### Music
Icon | Short Code
:-:|:-
:musical_score: | `:musical_score:`
:musical_note: | `:musical_note:`
:notes: | `:notes:`
:studio_microphone: | `:studio_microphone:`
:level_slider: | `:level_slider:`
:control_knobs: | `:control_knobs:`
:microphone: | `:microphone:`
:headphones: | `:headphones:`
:radio: | `:radio:`

#### Musical Instrument
Icon | Short Code
:-:|:-
:saxophone: | `:saxophone:`
:guitar: | `:guitar:`
:musical_keyboard: | `:musical_keyboard:`
:trumpet: | `:trumpet:`
:violin: | `:violin:`
:drum: | `:drum:`

#### Phone
Icon | Short Code
:-:|:-
:iphone: | `:iphone:`
:calling: | `:calling:`
:phone: | `:phone:` <br /> `:telephone:`
:telephone_receiver: | `:telephone_receiver:`
:pager: | `:pager:`
:fax: | `:fax:`

#### Computer
Icon | Short Code
:-:|:-
:battery: | `:battery:`
:electric_plug: | `:electric_plug:`
:computer: | `:computer:`
:desktop_computer: | `:desktop_computer:`
:printer: | `:printer:`
:keyboard: | `:keyboard:`
:computer_mouse: | `:computer_mouse:`
:trackball: | `:trackball:`
:minidisc: | `:minidisc:`
:floppy_disk: | `:floppy_disk:`
:cd: | `:cd:`
:dvd: | `:dvd:`

#### Film and Lighting
Icon | Short Code
:-:|:-
:movie_camera: | `:movie_camera:`
:film_strip: | `:film_strip:`
:film_projector: | `:film_projector:`
:clapper: | `:clapper:`
:tv: | `:tv:`
:camera: | `:camera:`
:camera_flash: | `:camera_flash:`
:video_camera: | `:video_camera:`
:vhs: | `:vhs:`
:mag: | `:mag:`
:mag_right: | `:mag_right:`
:candle: | `:candle:`
:bulb: | `:bulb:`
:flashlight: | `:flashlight:`
:izakaya_lantern: | `:izakaya_lantern:` <br /> `:lantern:`

#### Book and Paper
Icon | Short Code
:-:|:-
:notebook_with_decorative_cover: | `:notebook_with_decorative_cover:`
:closed_book: | `:closed_book:`
:book: | `:book:` <br /> `:open_book:`
:green_book: | `:green_book:`
:blue_book: | `:blue_book:`
:orange_book: | `:orange_book:`
:books: | `:books:`
:notebook: | `:notebook:`
:ledger: | `:ledger:`
:page_with_curl: | `:page_with_curl:`
:scroll: | `:scroll:`
:page_facing_up: | `:page_facing_up:`
:newspaper: | `:newspaper:`
:newspaper_roll: | `:newspaper_roll:`
:bookmark_tabs: | `:bookmark_tabs:`
:bookmark: | `:bookmark:`
:label: | `:label:`

#### Money
Icon | Short Code
:-:|:-
:moneybag: | `:moneybag:`
:yen: | `:yen:`
:dollar: | `:dollar:`
:euro: | `:euro:`
:pound: | `:pound:`
:money_with_wings: | `:money_with_wings:`
:credit_card: | `:credit_card:`
:chart: | `:chart:`

#### Mail
Icon | Short Code
:-:|:-
:email: | `:email:` <br /> `:envelope:`
:e-mail: | `:e-mail:`
:incoming_envelope: | `:incoming_envelope:`
:envelope_with_arrow: | `:envelope_with_arrow:`
:outbox_tray: | `:outbox_tray:`
:inbox_tray: | `:inbox_tray:`
:package: | `:package:`
:mailbox: | `:mailbox:`
:mailbox_closed: | `:mailbox_closed:`
:mailbox_with_mail: | `:mailbox_with_mail:`
:mailbox_with_no_mail: | `:mailbox_with_no_mail:`
:postbox: | `:postbox:`
:ballot_box: | `:ballot_box:`

#### Writing
Icon | Short Code
:-:|:-
:pencil2: | `:pencil2:`
:black_nib: | `:black_nib:`
:fountain_pen: | `:fountain_pen:`
:pen: | `:pen:`
:paintbrush: | `:paintbrush:`
:crayon: | `:crayon:`
:memo: | `:memo:` <br /> `:pencil:`

#### Office
Icon | Short Code
:-:|:-
:briefcase: | `:briefcase:`
:file_folder: | `:file_folder:`
:open_file_folder: | `:open_file_folder:`
:card_index_dividers: | `:card_index_dividers:`
:date: | `:date:`
:calendar: | `:calendar:`
:spiral_notepad: | `:spiral_notepad:`
:spiral_calendar: | `:spiral_calendar:`
:card_index: | `:card_index:`
:chart_with_upwards_trend: | `:chart_with_upwards_trend:`
:chart_with_downwards_trend: | `:chart_with_downwards_trend:`
:bar_chart: | `:bar_chart:`
:clipboard: | `:clipboard:`
:pushpin: | `:pushpin:`
:round_pushpin: | `:round_pushpin:`
:paperclip: | `:paperclip:`
:paperclips: | `:paperclips:`
:straight_ruler: | `:straight_ruler:`
:triangular_ruler: | `:triangular_ruler:`
:scissors: | `:scissors:`
:card_file_box: | `:card_file_box:`
:file_cabinet: | `:file_cabinet:`
:wastebasket: | `:wastebasket:`

#### Lock
Icon | Short Code
:-:|:-
:lock: | `:lock:`
:unlock: | `:unlock:`
:lock_with_ink_pen: | `:lock_with_ink_pen:`
:closed_lock_with_key: | `:closed_lock_with_key:`
:key: | `:key:`
:old_key: | `:old_key:`

#### Tool
Icon | Short Code
:-:|:-
:hammer: | `:hammer:`
:pick: | `:pick:`
:hammer_and_pick: | `:hammer_and_pick:`
:hammer_and_wrench: | `:hammer_and_wrench:`
:dagger: | `:dagger:`
:crossed_swords: | `:crossed_swords:`
:gun: | `:gun:`
:bow_and_arrow: | `:bow_and_arrow:`
:shield: | `:shield:`
:wrench: | `:wrench:`
:nut_and_bolt: | `:nut_and_bolt:`
:gear: | `:gear:`
:clamp: | `:clamp:`
:balance_scale: | `:balance_scale:`
:link: | `:link:`
:chains: | `:chains:`

#### Science
Icon | Short Code
:-:|:-
:alembic: | `:alembic:`
:microscope: | `:microscope:`
:telescope: | `:telescope:`
:satellite: | `:satellite:`

#### Medical
Icon | Short Code
:-:|:-
:syringe: | `:syringe:`
:pill: | `:pill:`

#### Household
Icon | Short Code
:-:|:-
:door: | `:door:`
:bed: | `:bed:`
:couch_and_lamp: | `:couch_and_lamp:`
:toilet: | `:toilet:`
:shower: | `:shower:`
:bathtub: | `:bathtub:`
:shopping_cart: | `:shopping_cart:`

#### Other
Icon | Short Code
:-:|:-
:smoking: | `:smoking:`
:coffin: | `:coffin:`
:funeral_urn: | `:funeral_urn:`
:moyai: | `:moyai:`

===

#### Transport Sign
Icon | Short Code
:-:|:-
:atm: | `:atm:`
:put_litter_in_its_place: | `:put_litter_in_its_place:`
:potable_water: | `:potable_water:`
:wheelchair: | `:wheelchair:`
:mens: | `:mens:`
:womens: | `:womens:`
:restroom: | `:restroom:`
:baby_symbol: | `:baby_symbol:`
:wc: | `:wc:`
:passport_control: | `:passport_control:`
:customs: | `:customs:`
:baggage_claim: | `:baggage_claim:`
:left_luggage: | `:left_luggage:`

#### Warning
Icon | Short Code
:-:|:-
:warning: | `:warning:`
:children_crossing: | `:children_crossing:`
:no_entry: | `:no_entry:`
:no_entry_sign: | `:no_entry_sign:`
:no_bicycles: | `:no_bicycles:`
:no_smoking: | `:no_smoking:`
:do_not_litter: | `:do_not_litter:`
:non-potable_water: | `:non-potable_water:`
:no_pedestrians: | `:no_pedestrians:`
:no_mobile_phones: | `:no_mobile_phones:`
:underage: | `:underage:`
:radioactive: | `:radioactive:`
:biohazard: | `:biohazard:`

#### Arrow
Icon | Short Code
:-:|:-
:arrow_up: | `:arrow_up:`
:arrow_upper_right: | `:arrow_upper_right:`
:arrow_right: | `:arrow_right:`
:arrow_lower_right: | `:arrow_lower_right:`
:arrow_down: | `:arrow_down:`
:arrow_lower_left: | `:arrow_lower_left:`
:arrow_left: | `:arrow_left:`
:arrow_upper_left: | `:arrow_upper_left:`
:arrow_up_down: | `:arrow_up_down:`
:left_right_arrow: | `:left_right_arrow:`
:leftwards_arrow_with_hook: | `:leftwards_arrow_with_hook:`
:arrow_right_hook: | `:arrow_right_hook:`
:arrow_heading_up: | `:arrow_heading_up:`
:arrow_heading_down: | `:arrow_heading_down:`
:arrows_clockwise: | `:arrows_clockwise:`
:arrows_counterclockwise: | `:arrows_counterclockwise:`
:back: | `:back:`
:end: | `:end:`
:on: | `:on:`
:soon: | `:soon:`
:top: | `:top:`

#### Religion
Icon | Short Code
:-:|:-
:place_of_worship: | `:place_of_worship:`
:atom_symbol: | `:atom_symbol:`
:om: | `:om:`
:star_of_david: | `:star_of_david:`
:wheel_of_dharma: | `:wheel_of_dharma:`
:yin_yang: | `:yin_yang:`
:latin_cross: | `:latin_cross:`
:orthodox_cross: | `:orthodox_cross:`
:star_and_crescent: | `:star_and_crescent:`
:peace_symbol: | `:peace_symbol:`
:menorah: | `:menorah:`
:six_pointed_star: | `:six_pointed_star:`

#### Zodiac
Icon | Short Code
:-:|:-
:aries: | `:aries:`
:taurus: | `:taurus:`
:gemini: | `:gemini:`
:cancer: | `:cancer:`
:leo: | `:leo:`
:virgo: | `:virgo:`
:libra: | `:libra:`
:scorpius: | `:scorpius:`
:sagittarius: | `:sagittarius:`
:capricorn: | `:capricorn:`
:aquarius: | `:aquarius:`
:pisces: | `:pisces:`
:ophiuchus: | `:ophiuchus:`

#### AV Symbol
Icon | Short Code
:-:|:-
:twisted_rightwards_arrows: | `:twisted_rightwards_arrows:`
:repeat: | `:repeat:`
:repeat_one: | `:repeat_one:`
:arrow_forward: | `:arrow_forward:`
:fast_forward: | `:fast_forward:`
:next_track_button: | `:next_track_button:`
:play_or_pause_button: | `:play_or_pause_button:`
:arrow_backward: | `:arrow_backward:`
:rewind: | `:rewind:`
:previous_track_button: | `:previous_track_button:`
:arrow_up_small: | `:arrow_up_small:`
:arrow_double_up: | `:arrow_double_up:`
:arrow_down_small: | `:arrow_down_small:`
:arrow_double_down: | `:arrow_double_down:`
:pause_button: | `:pause_button:`
:stop_button: | `:stop_button:`
:record_button: | `:record_button:`
:cinema: | `:cinema:`
:low_brightness: | `:low_brightness:`
:high_brightness: | `:high_brightness:`
:signal_strength: | `:signal_strength:`
:vibration_mode: | `:vibration_mode:`
:mobile_phone_off: | `:mobile_phone_off:`

#### Math
Icon | Short Code
:-:|:-
:heavy_multiplication_x: | `:heavy_multiplication_x:`
:heavy_plus_sign: | `:heavy_plus_sign:`
:heavy_minus_sign: | `:heavy_minus_sign:`
:heavy_division_sign: | `:heavy_division_sign:`

#### Punctuation
Icon | Short Code
:-:|:-
:bangbang: | `:bangbang:`
:interrobang: | `:interrobang:`
:question: | `:question:`
:grey_question: | `:grey_question:`
:grey_exclamation: | `:grey_exclamation:`
:exclamation: | `:exclamation:` <br /> `:heavy_exclamation_mark:`
:wavy_dash: | `:wavy_dash:`

#### Currency
Icon | Short Code
:-:|:-
:currency_exchange: | `:currency_exchange:`
:heavy_dollar_sign: | `:heavy_dollar_sign:`

#### Other Symbols
Icon | Short Code
:-:|:-
:recycle: | `:recycle:`
:fleur_de_lis: | `:fleur_de_lis:`
:trident: | `:trident:`:name_badge: | `:name_badge:`
:beginner: | `:beginner:`
:o: | `:o:`
:white_check_mark: | `:white_check_mark:`
:ballot_box_with_check: | `:ballot_box_with_check:`
:heavy_check_mark: | `:heavy_check_mark:`
:x: | `:x:`
:negative_squared_cross_mark: | `:negative_squared_cross_mark:`
:curly_loop: | `:curly_loop:`
:loop: | `:loop:`
:part_alternation_mark: | `:part_alternation_mark:`
:eight_spoked_asterisk: | `:eight_spoked_asterisk:`
:eight_pointed_black_star: | `:eight_pointed_black_star:`
:sparkle: | `:sparkle:`
:copyright: | `:copyright:`
:registered: | `:registered:`
:tm: | `:tm:`

#### Keycap
Icon | Short Code
:-:|:-
:hash: | `:hash:`
:asterisk: | `:asterisk:`
:zero: | `:zero:`
:one: | `:one:`
:two: | `:two:`
:three: | `:three:`
:four: | `:four:`
:five: | `:five:`
:six: | `:six:`
:seven: | `:seven:`
:eight: | `:eight:`
:nine: | `:nine:`
:keycap_ten: | `:keycap_ten:`

#### Alphanum
Icon | Short Code
:-:|:-
:capital_abcd: | `:capital_abcd:`
:abcd: | `:abcd:`
:1234: | `:1234:`
:symbols: | `:symbols:`
:abc: | `:abc:`
:a: | `:a:`
:ab: | `:ab:`
:b: | `:b:`
:cl: | `:cl:`
:cool: | `:cool:`
:free: | `:free:`
:information_source: | `:information_source:`
:id: | `:id:`
:m: | `:m:`
:new: | `:new:`
:ng: | `:ng:`
:o2: | `:o2:`
:ok: | `:ok:`
:parking: | `:parking:` | :sos: | `:sos:`
:up: | `:up:`
:vs: | `:vs:`
:koko: | `:koko:`
:sa: | `:sa:`
:u6708: | `:u6708:`
:u6709: | `:u6709:`
:u6307: | `:u6307:`
:ideograph_advantage: | `:ideograph_advantage:`
:u5272: | `:u5272:`
:u7121: | `:u7121:`
:u7981: | `:u7981:`
:accept: | `:accept:`
:u7533: | `:u7533:`
:u5408: | `:u5408:`
:u7a7a: | `:u7a7a:`
:congratulations: | `:congratulations:`
:secret: | `:secret:` | :u55b6: | `:u55b6:`
:u6e80: | `:u6e80:`

#### Geometry
Icon | Short Code
:-:|:-
:red_circle: | `:red_circle:`
:large_blue_circle: | `:large_blue_circle:`
:black_circle: | `:black_circle:`
:white_circle: | `:white_circle:`
:black_large_square: | `:black_large_square:`
:white_large_square: | `:white_large_square:`
:black_medium_square: | `:black_medium_square:`
:white_medium_square: | `:white_medium_square:`
:black_medium_small_square: | `:black_medium_small_square:`
:white_medium_small_square: | `:white_medium_small_square:`
:black_small_square: | `:black_small_square:`
:white_small_square: | `:white_small_square:`
:large_orange_diamond: | `:large_orange_diamond:`
:large_blue_diamond: | `:large_blue_diamond:`
:small_orange_diamond: | `:small_orange_diamond:`
:small_blue_diamond: | `:small_blue_diamond:`
:small_red_triangle: | `:small_red_triangle:`
:small_red_triangle_down: | `:small_red_triangle_down:`
:diamond_shape_with_a_dot_inside: | `:diamond_shape_with_a_dot_inside:`
:radio_button: | `:radio_button:`
:white_square_button: | `:white_square_button:`
:black_square_button: | `:black_square_button:`

===

#### Flag
Icon | Short Code
:-:|:-
:checkered_flag: | `:checkered_flag:`
:triangular_flag_on_post: | `:triangular_flag_on_post:`
:crossed_flags: | `:crossed_flags:`
:black_flag: | `:black_flag:`
:white_flag: | `:white_flag:`
:rainbow_flag: | `:rainbow_flag:`

#### Country Flag
Icon | Short Code
:-:|:-
:andorra: | `:andorra:`
:united_arab_emirates: | `:united_arab_emirates:`
:afghanistan: | `:afghanistan:`
:antigua_barbuda: | `:antigua_barbuda:`
:anguilla: | `:anguilla:`
:albania: | `:albania:`
:armenia: | `:armenia:`
:angola: | `:angola:`
:antarctica: | `:antarctica:`
:argentina: | `:argentina:`
:american_samoa: | `:american_samoa:`
:austria: | `:austria:`
:australia: | `:australia:`
:aruba: | `:aruba:`
:aland_islands: | `:aland_islands:`
:azerbaijan: | `:azerbaijan:`
:bosnia_herzegovina: | `:bosnia_herzegovina:`
:barbados: | `:barbados:`
:bangladesh: | `:bangladesh:`
:belgium: | `:belgium:`
:burkina_faso: | `:burkina_faso:`
:bulgaria: | `:bulgaria:`
:bahrain: | `:bahrain:`
:burundi: | `:burundi:`
:benin: | `:benin:`
:st_barthelemy: | `:st_barthelemy:`
:bermuda: | `:bermuda:`
:brunei: | `:brunei:`
:bolivia: | `:bolivia:`
:caribbean_netherlands: | `:caribbean_netherlands:`
:brazil: | `:brazil:`
:bahamas: | `:bahamas:`
:bhutan: | `:bhutan:`
:botswana: | `:botswana:`
:belarus: | `:belarus:`
:belize: | `:belize:`
:canada: | `:canada:`
:cocos_islands: | `:cocos_islands:`
:congo_kinshasa: | `:congo_kinshasa:`
:central_african_republic: | `:central_african_republic:`
:congo_brazzaville: | `:congo_brazzaville:`
:switzerland: | `:switzerland:`
:cote_divoire: | `:cote_divoire:`
:cook_islands: | `:cook_islands:`
:chile: | `:chile:`
:cameroon: | `:cameroon:`
:cn: | `:cn:`
:colombia: | `:colombia:`
:costa_rica: | `:costa_rica:`
:cuba: | `:cuba:`
:cape_verde: | `:cape_verde:`
:curacao: | `:curacao:`
:christmas_island: | `:christmas_island:`
:cyprus: | `:cyprus:`
:czech_republic: | `:czech_republic:`
:de: | `:de:`
:djibouti: | `:djibouti:`
:denmark: | `:denmark:`
:dominica: | `:dominica:`
:dominican_republic: | `:dominican_republic:`
:algeria: | `:algeria:`
:ecuador: | `:ecuador:`
:estonia: | `:estonia:`
:egypt: | `:egypt:`
:western_sahara: | `:western_sahara:`
:eritrea: | `:eritrea:`
:es: | `:es:`
:ethiopia: | `:ethiopia:`
:eu: | `:eu:` <br /> `:european_union:`
:finland: | `:finland:`
:fiji: | `:fiji:`
:falkland_islands: | `:falkland_islands:`
:micronesia: | `:micronesia:`
:faroe_islands: | `:faroe_islands:`
:fr: | `:fr:`
:gabon: | `:gabon:`
:gb: | `:gb:` <br /> `:uk:`
:grenada: | `:grenada:`
:georgia: | `:georgia:`
:french_guiana: | `:french_guiana:`
:guernsey: | `:guernsey:`
:ghana: | `:ghana:`
:gibraltar: | `:gibraltar:`
:greenland: | `:greenland:`
:gambia: | `:gambia:`
:guinea: | `:guinea:`
:guadeloupe: | `:guadeloupe:`
:equatorial_guinea: | `:equatorial_guinea:`
:greece: | `:greece:`
:south_georgia_south_sandwich_islands: | `:south_georgia_south_sandwich_islands:`
:guatemala: | `:guatemala:`
:guam: | `:guam:`
:guinea_bissau: | `:guinea_bissau:`
:guyana: | `:guyana:`
:hong_kong: | `:hong_kong:`
:honduras: | `:honduras:`
:croatia: | `:croatia:`
:haiti: | `:haiti:`
:hungary: | `:hungary:`
:canary_islands: | `:canary_islands:`
:indonesia: | `:indonesia:`
:ireland: | `:ireland:`
:israel: | `:israel:`
:isle_of_man: | `:isle_of_man:`
:india: | `:india:`
:british_indian_ocean_territory: | `:british_indian_ocean_territory:`
:iraq: | `:iraq:`
:iran: | `:iran:`
:iceland: | `:iceland:`
:it: | `:it:`
:jersey: | `:jersey:`
:jamaica: | `:jamaica:`
:jordan: | `:jordan:`
:jp: | `:jp:`
:kenya: | `:kenya:`
:kyrgyzstan: | `:kyrgyzstan:`
:cambodia: | `:cambodia:`
:kiribati: | `:kiribati:`
:comoros: | `:comoros:`
:st_kitts_nevis: | `:st_kitts_nevis:`
:north_korea: | `:north_korea:`
:kr: | `:kr:`
:kuwait: | `:kuwait:`
:cayman_islands: | `:cayman_islands:`
:kazakhstan: | `:kazakhstan:`
:laos: | `:laos:`
:lebanon: | `:lebanon:`
:st_lucia: | `:st_lucia:`
:liechtenstein: | `:liechtenstein:`
:sri_lanka: | `:sri_lanka:`
:liberia: | `:liberia:`
:lesotho: | `:lesotho:`
:lithuania: | `:lithuania:`
:luxembourg: | `:luxembourg:`
:latvia: | `:latvia:`
:libya: | `:libya:`
:morocco: | `:morocco:`
:monaco: | `:monaco:`
:moldova: | `:moldova:`
:montenegro: | `:montenegro:`
:madagascar: | `:madagascar:`
:marshall_islands: | `:marshall_islands:`
:macedonia: | `:macedonia:`
:mali: | `:mali:`
:myanmar: | `:myanmar:`
:mongolia: | `:mongolia:`
:macau: | `:macau:`
:northern_mariana_islands: | `:northern_mariana_islands:`
:martinique: | `:martinique:`
:mauritania: | `:mauritania:`
:montserrat: | `:montserrat:`
:malta: | `:malta:`
:mauritius: | `:mauritius:`
:maldives: | `:maldives:`
:malawi: | `:malawi:`
:mexico: | `:mexico:`
:malaysia: | `:malaysia:`
:mozambique: | `:mozambique:`
:namibia: | `:namibia:`
:new_caledonia: | `:new_caledonia:`
:niger: | `:niger:`
:norfolk_island: | `:norfolk_island:`
:nigeria: | `:nigeria:`
:nicaragua: | `:nicaragua:`
:netherlands: | `:netherlands:`
:norway: | `:norway:`
:nepal: | `:nepal:`
:nauru: | `:nauru:`
:niue: | `:niue:`
:new_zealand: | `:new_zealand:`
:oman: | `:oman:`
:panama: | `:panama:`
:peru: | `:peru:`
:french_polynesia: | `:french_polynesia:`
:papua_new_guinea: | `:papua_new_guinea:` | :philippines: | `:philippines:`
:pakistan: | `:pakistan:`
:poland: | `:poland:`
:st_pierre_miquelon: | `:st_pierre_miquelon:`
:pitcairn_islands: | `:pitcairn_islands:`
:puerto_rico: | `:puerto_rico:`
:palestinian_territories: | `:palestinian_territories:`
:portugal: | `:portugal:`
:palau: | `:palau:`
:paraguay: | `:paraguay:`
:qatar: | `:qatar:`
:reunion: | `:reunion:`
:romania: | `:romania:`
:serbia: | `:serbia:`
:ru: | `:ru:`
:rwanda: | `:rwanda:`
:saudi_arabia: | `:saudi_arabia:`
:solomon_islands:
`:solomon_islands:`
:seychelles: | `:seychelles:`
:sudan: | `:sudan:`
:sweden: | `:sweden:`
:singapore: | `:singapore:`
:st_helena: | `:st_helena:`
:slovenia: | `:slovenia:`
:slovakia: | `:slovakia:`
:sierra_leone: | `:sierra_leone:`
:san_marino: | `:san_marino:`
:senegal: | `:senegal:`
:somalia: | `:somalia:`
:suriname: | `:suriname:`
:south_sudan: | `:south_sudan:`
:sao_tome_principe: | `:sao_tome_principe:`
:el_salvador: | `:el_salvador:`
:sint_maarten: | `:sint_maarten:`
:syria: | `:syria:`
:swaziland: | `:swaziland:`
:turks_caicos_islands: | `:turks_caicos_islands:`
:chad: | `:chad:`
:french_southern_territories: | `:french_southern_territories:`
:togo: | `:togo:`
:thailand: | `:thailand:`
:tajikistan: | `:tajikistan:`
:tokelau: | `:tokelau:`
:timor_leste: | `:timor_leste:`
:turkmenistan: | `:turkmenistan:`
:tunisia: | `:tunisia:`
:tonga: | `:tonga:`
:tr: | `:tr:`
:trinidad_tobago: | `:trinidad_tobago:`
:tuvalu: | `:tuvalu:`
:taiwan: | `:taiwan:`
:tanzania: | `:tanzania:`
:ukraine: | `:ukraine:`
:uganda: | `:uganda:`
:us: | `:us:`
:uruguay: | `:uruguay:`
:uzbekistan: | `:uzbekistan:`
:vatican_city: | `:vatican_city:`
:st_vincent_grenadines: | `:st_vincent_grenadines:`
:venezuela: | `:venezuela:`
:british_virgin_islands: | `:british_virgin_islands:`
:us_virgin_islands: | `:us_virgin_islands:`
:vietnam: | `:vietnam:`
:vanuatu: | `:vanuatu:`
:wallis_futuna: | `:wallis_futuna:`
:samoa: | `:samoa:`
:kosovo: | `:kosovo:`
:yemen: | `:yemen:`
:mayotte: | `:mayotte:`
:south_africa: | `:south_africa:`
:zambia: | `:zambia:`
:zimbabwe: | `:zimbabwe:`

## GitHub Specific Emojis

Here are a few emoji codes that only work on GitHub.

Icon | Short Code
:-:|:-
:atom: | `:atom:`
:basecamp: | `:basecamp:`
:basecampy: | `:basecampy:`
:bowtie: | `:bowtie:`
:electron: | `:electron:`
:feelsgood: | `:feelsgood:`
:finnadie: | `:finnadie:`
:goberserk: | `:goberserk:`
:godmode: | `:godmode:`
:hurtrealbad: | `:hurtrealbad:`
:neckbeard: | `:neckbeard:`
:octocat: | `:octocat:`
:rage1: | `:rage1:`
:rage2: | `:rage2:`
:rage3: | `:rage3:`
:rage4: | `:rage4:`
:shipit: | `:shipit:` <br /> `:squirrel:`
:suspect: | `:suspect:`
:trollface: | `:trollface:`


## The End.
Congratulations! You've made it to the end.
Now, if you're up to it, look at this page again but select the "raw" mode on GitHub (top-right corner)
There are no easter eggs, but you'll get to see how this document is made, which will help solidify you accumulated knowledge on Markdown.

<!-- References -->
[HTML]: https://daringfireball.net/projects/markdown/syntax
[emojis]: https://www.webfx.com/tools/emoji-cheat-sheet/
[emojis_categorization]: https://github.com/ikatyang/emoji-cheat-sheet
[br_tag]: https://www.w3schools.com/tags/tag_br.asp

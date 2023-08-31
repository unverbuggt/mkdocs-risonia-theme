title: Markdown Test, TEst, tEst, test...
<!-- "title" is shown in top bar -->

# This is a title

## This is a heading

### This is a subheading

#### This is a subsubheading (not shown in toc)

This is a paragraph.

Normal
line breaks
are
ignored.

You can force line breaks  
by adding two spaces at the end of the line (but this is invisible in some editors).

But you can also force line breaks\
by adding a backslash at the end of the line (but this is only possible if `pymdownx.escapeall: hardbreak: true` is set in `markdown_extensions`).

Words can be highlighted in **bold** and *italic*, but [underline]() is reserved for links.

There can be `code` within a paragraph.
```plaintext
That
    is
      shown
           inside
                 a code window
with all formatting intact.
```

CSS classes can also be added to paragraphs (`attr_list` in `markdown_extensions` is required).
{ .font-lobster .w3-panel .w3-leftbar .w3-rightbar .w3-border-red }


> This is a citation.

This is a list:

* Apples
* Pears
* Plums

This is a numbered list:

1. Walnuts
2. Almonds
2. Hazelnuts (Numbering is continued automatically)

This is a table:

| Fruit | Nuts | Pulse |
| ---- | ---- | ---- |
| Apples | Almonds | Beans |
| Plums | Walnuts | Peanuts |
| Pears | Hazelnuts | Peas |

This is an image:
![](../img/logo192.png)

Furthermore inline HTML is possible: <svg class="svg-1em"><use xlink:href="#encrypted" /></svg>.

## This is how the page looks in Markdown:

```markdown
title: Markdown Test, TEst, tEst, test...
<!-- "title" is shown in top bar -->

# This is a title

## This is a heading

### This is a subheading

#### This is a subsubheading (not shown in toc)

This is a paragraph.

Normal
line breaks
are
ignored.

You can force line breaks  
by adding two spaces at the end of the line (but this is invisible in some editors).

But you can also force line breaks\
by adding a backslash at the end of the line (but this is only possible if `pymdownx.escapeall: hardbreak: true` is set in `markdown_extensions`).

Words can be highlighted in **bold** and *italic*, but [underline]() is reserved for links.

There can be `code` within a paragraph.
\```plaintext
That
    is
      shown
           inside
                 a code window
with all formatting intact.
\```

CSS classes can also be added to paragraphs (`attr_list` in `markdown_extensions` is required).
{ .font-lobster .w3-panel .w3-leftbar .w3-rightbar .w3-border-red }


> This is a citation.

This is a list:

* Apples
* Pears
* Plums

This is a numbered list:

1. Walnuts
2. Almonds
2. Hazelnuts (Numbering is continued automatically)

This is a table:

| Fruit | Nuts | Pulse |
| ---- | ---- | ---- |
| Apples | Almonds | Beans |
| Plums | Walnuts | Peanuts |
| Pears | Hazelnuts | Peas |

This is an image:
![](../../img/logo192.png)

Furthermore inline HTML is possible: <svg class="svg-1em"><use xlink:href="#encrypted" /></svg>.
```

## This is how the page looks in HTML:

```html
<!-- "title" is shown in top bar -->
<h1 id="this-is-a-title">This is a title</h1>
<h2 id="this-is-a-heading">This is a heading</h2>
<h3 id="this-is-a-subheading">This is a subheading</h3>
<h4 id="this-is-a-subsubheading-not-shown-in-toc">This is a subsubheading (not shown in toc)</h4>
<p>This is a paragraph.</p>
<p>Normal
line breaks
are
ignored.</p>
<p>You can force line breaks<br/>
by adding two spaces at the end of the line (but this is invisible in some editors).</p>
<p>But you can also force line breaks<br/>
by adding a backslash at the end of the line (but this is only possible if <code class="w3-codespan">pymdownx.escapeall: hardbreak: true</code> is set in <code class="w3-codespan">markdown_extensions</code>).</p>
<p>Words can be highlighted in <strong>bold</strong> and <em>italic</em>, but <a href="">underline</a> is reserved for links.</p>
<p>There can be <code class="w3-codespan">code</code> within a paragraph.</p>
<pre class="w3-code w3-responsive"><code class="language-plaintext">That
    is
      shown
           inside
                 a code window
with all formatting intact.
</code></pre>
<p class="font-lobster w3-panel w3-leftbar w3-rightbar w3-border-red">CSS classes can also be added to paragraphs (<code class="w3-codespan">attr_list</code> in <code class="w3-codespan">markdown_extensions</code> is required).</p>
<div class="w3-panel w3-theme-l3 w3-leftbar w3-border-theme">
<p>This is a citation.</p>
</div>
<p>This is a list:</p>
<ul>
<li>Apples</li>
<li>Pears</li>
<li>Plums</li>
</ul>
<p>This is a numbered list:</p>
<ol>
<li>Walnuts</li>
<li>Almonds</li>
<li>Hazelnuts (Numbering is continued automatically)</li>
</ol>
<p>This is a table:</p>
<div class="w3-responsive"><table class="w3-table w3-bordered w3-striped">
<thead>
<tr>
<th>Fruit</th>
<th>Nuts</th>
<th>Pulse</th>
</tr>
</thead>
<tbody>
<tr>
<td>Apples</td>
<td>Almonds</td>
<td>Beans</td>
</tr>
<tr>
<td>Plums</td>
<td>Walnuts</td>
<td>Peanuts</td>
</tr>
<tr>
<td>Pears</td>
<td>Hazelnuts</td>
<td>Peas</td>
</tr>
</tbody>
</table></div>
<p>This is an image:
<img alt="" class="w3-image" src="../../img/logo192.png"/></p>
<p>Furthermore inline HTML is possible: <svg class="svg-1em"><use xlink:href="#encrypted"></use></svg>.</p>
```
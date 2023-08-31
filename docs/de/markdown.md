title: Markdown Test, TEst, tEst, test...
<!-- "title" wird in der Titelleiste angezeigt -->

# Dies ist der Seitentitel

## Dies eine Überschrift

### Und eine Unterüberschrift

#### Und eine Unterunterüberschrift (wird nicht mehr im Inhaltsverzeichnis angezeigt)

Dies ist ein Absatz.

Normale
Zeilenumbrüche
werden
ignoriert.

Man kann Zeilenumbrüche  
mit zwei Leerzeichen am Zeilenende erzwingen (dies bleibt aber leider in einigen Editoren unsichtbar).

Aber man kann Zeilenumbrüche\
auch durch Backslash am Zeilenende erzwingen. (dies setzt allerdings `pymdownx.escapeall: hardbreak: true` in den `markdown_extensions` voraus).

Man kann Worte **fett** oder *kursiv* hervorheben, [unterstrichen]() werden allerdings nur Links.

Man kann im Text auf `Code` verweisen.
```plaintext
Der
   dann
       in
         einem
              Codefenster
inklusive der Formatierung erhalten bleibt.
```

Ein Absatz kann auch CSS Klassen erhalten (Voraussetzung ist `attr_list` in den `markdown_extensions`).
{ .font-lobster .w3-panel .w3-leftbar .w3-rightbar .w3-border-red }


> Dies ist ein Zitat.

Dies ist eine Liste:

* Äpfel
* Birnen
* Pflaumen

Und dies eine nummerierte Liste:

1. Walnüsse
2. Mandeln
2. Haselnüsse (Nummerierung wird automatisch fortgesetzt)

Die ist eine Tabelle:

| Früchte | Nüsse | Hülsenfrüchte |
| ---- | ---- | ---- |
| Äpfel | Mandeln | Bohnen |
| Pflaumen | Walnüsse | Erdnüsse |
| Birnen | Haselnüsse | Erbsen |

Hier ein Bild:
![](../img/logo192.png)

Außerdem ist inline HTML möglich: <svg class="svg-1em"><use xlink:href="#encrypted" /></svg>.

## So sieht der Markdowntext dieser Seite aus:

```markdown
title: Markdown Test, TEst, tEst, test...
<!-- "title" wird in der Titelleiste angezeigt -->

# Dies ist der Seitentitel

## Dies eine Überschrift

### Und eine Unterüberschrift

#### Und eine Unterunterüberschrift (wird nicht mehr im Inhaltsverzeichnis angezeigt)

Dies ist ein Absatz.

Normale
Zeilenumbrüche
werden
ignoriert.

Man kann Zeilenumbrüche  
mit zwei Leerzeichen am Zeilenende erzwingen (dies bleibt aber leider in einigen Editoren unsichtbar).

Aber man kann Zeilenumbrüche\
auch durch Backslash am Zeilenende erzwingen. (dies setzt allerdings `pymdownx.escapeall: hardbreak: true` in den `markdown_extensions` voraus).

Man kann Worte **fett** oder *kursiv* hervorheben, [unterstrichen]() werden allerdings nur Links.

Man kann im Text auf `Code` verweisen.
\```plaintext
Der
   dann
       in
         einem
              Codefenster
inklusive der Formatierung erhalten bleibt.
\```

Ein Absatz kann auch CSS Klassen erhalten (Voraussetzung ist `attr_list` in den `markdown_extensions`).
{ .font-lobster .w3-panel .w3-leftbar .w3-rightbar .w3-border-red }


> Dies ist ein Zitat.

Dies ist eine Liste:

* Äpfel
* Birnen
* Pflaumen

Und dies eine nummerierte Liste:

1. Walnüsse
2. Mandeln
2. Haselnüsse (Nummerierung wird automatisch fortgesetzt)

Die ist eine Tabelle:

| Früchte | Nüsse | Hülsenfrüchte |
| ---- | ---- | ---- |
| Äpfel | Mandeln | Bohnen |
| Pflaumen | Walnüsse | Erdnüsse |
| Birnen | Haselnüsse | Erbsen |

Hier ein Bild:
![](../img/logo192.png)

Außerdem ist inline HTML möglich: <svg class="svg-1em"><use xlink:href="#encrypted" /></svg>.
```

## Und dieses HTML wird daraus erzeugt:

```html
<!-- "title" wird in der Titelleiste angezeigt -->
<h1 id="dies-ist-der-seitentitel">Dies ist der Seitentitel</h1>
<h2 id="dies-eine-uberschrift">Dies eine Überschrift</h2>
<h3 id="und-eine-unteruberschrift">Und eine Unterüberschrift</h3>
<h4 id="und-eine-unterunteruberschrift-wird-nicht-mehr-im-inhaltsverzeichnis-angezeigt">Und eine Unterunterüberschrift (wird nicht mehr im Inhaltsverzeichnis angezeigt)</h4>
<p>Dies ist ein Absatz.</p>
<p>Normale
Zeilenumbrüche
werden
ignoriert.</p>
<p>Man kann Zeilenumbrüche<br/>
mit zwei Leerzeichen am Zeilenende erzwingen (dies bleibt aber leider in einigen Editoren unsichtbar).</p>
<p>Aber man kann Zeilenumbrüche<br/>
auch durch Backslash am Zeilenende erzwingen. (dies setzt allerdings <code class="w3-codespan">pymdownx.escapeall: hardbreak: true</code> in den <code class="w3-codespan">markdown_extensions</code> voraus).</p>
<p>Man kann Worte <strong>fett</strong> oder <em>kursiv</em> hervorheben, <a href="">unterstrichen</a> werden allerdings nur Links.</p>
<p>Man kann im Text auf <code class="w3-codespan">Code</code> verweisen.</p>
<pre class="w3-code w3-responsive"><code class="language-plaintext">Der
   dann
       in
         einem
              Codefenster
inklusive der Formatierung erhalten bleibt.
</code></pre>
<p class="font-lobster w3-panel w3-leftbar w3-rightbar w3-border-red">Ein Absatz kann auch CSS Klassen erhalten (Voraussetzung ist <code class="w3-codespan">attr_list</code> in den <code class="w3-codespan">markdown_extensions</code>).</p>
<div class="w3-panel w3-theme-l3 w3-leftbar w3-border-theme">
<p>Dies ist ein Zitat.</p>
</div>
<p>Dies ist eine Liste:</p>
<ul>
<li>Äpfel</li>
<li>Birnen</li>
<li>Pflaumen</li>
</ul>
<p>Und dies eine nummerierte Liste:</p>
<ol>
<li>Walnüsse</li>
<li>Mandeln</li>
<li>Haselnüsse (Nummerierung wird automatisch fortgesetzt)</li>
</ol>
<p>Die ist eine Tabelle:</p>
<div class="w3-responsive"><table class="w3-table w3-bordered w3-striped">
<thead>
<tr>
<th>Früchte</th>
<th>Nüsse</th>
<th>Hülsenfrüchte</th>
</tr>
</thead>
<tbody>
<tr>
<td>Äpfel</td>
<td>Mandeln</td>
<td>Bohnen</td>
</tr>
<tr>
<td>Pflaumen</td>
<td>Walnüsse</td>
<td>Erdnüsse</td>
</tr>
<tr>
<td>Birnen</td>
<td>Haselnüsse</td>
<td>Erbsen</td>
</tr>
</tbody>
</table></div>
<p>Hier ein Bild:
<img alt="" class="w3-image" src="../img/logo192.png"/></p>
<p>Außerdem ist inline HTML möglich: <svg class="svg-1em"><use xlink:href="#encrypted"></use></svg>.</p>
```
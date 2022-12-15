title: MkDocs

## Introduction

Taken from [MkDocs](https://www.mkdocs.org/) Page:

> MkDocs is a **fast**, **simple** and **downright gorgeous** static site generator that's geared
> towards building project documentation. Documentation source files are written in Markdown, and
> configured with a single YAML configuration file. Start by reading the 
> [introductory tutorial](https://www.mkdocs.org/getting-started/),
> then check the [User Guide](https://www.mkdocs.org/user-guide/) for more information.

## Themes

MkDocs includes two built-in themes (`mkdocs` and `readthedocs`). 
However, many [third party themes](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes) are available to choose from as well.

### Size comparison

I once (as of 2022-12-14) generated this site using different themes to get a sense of the size of the generated site.
All size indications in kilobytes (rounded up).

Theme | Version | HTML | CSS | JS/JSON/MAP | Webfonts | Miscellaneous | Total
---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
`risonia` | 0.1 | 712 | 213 | 439 | 76 | 807 | 2247
`mkdocs` | 1.4.2 | 593 | 203 | 597 | 1030 | 803 | 3226
`material` | 8.5.10 | 1045 | 151 | 2183 | 76 | 801 | 4256
`material` | 8.4.4-insiders | 1110 | 534 | 2946 | 703 | 801 | 6094

HTML, CSS, JS should be somewhat comperable, whereat Risonia doesn't use "minify".
To be fair the `material` theme uses [Pygments](https://pygments.org/)
instead of [highlight.js](https://highlightjs.org/) for code highlighting, which increses the size of HTML.

The webfont size is not really comperable, because `mkdocs` f.ex. supplies all flavors of the webfonts for best downward compatibility.
Risonia doesn't use webfonts by default.

The "insiders" version of `material` was configured with the `privacy` plugin,
so all dependencies were downloaded.
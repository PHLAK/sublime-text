cdSublime Text Setup
==================

A list of my Sublime Text packages, settings, and key bindings.

![Sublime Text 2 Screenshot](https://raw.github.com/PHLAK/sublime-text/master/screenshot.png)


Theme, Color Scheme & Font
--------------------------

  * [Theme - Soda](https://github.com/buymeasoda/soda-theme/) (Soda Dark)
  * [Base16 Color Schemes](https://github.com/chriskempson/base16-textmate) (Base 16 Tomorrow Dark)
  * [Ubuntu Mono](http://font.ubuntu.com/)


Packages
--------

  * [AdvancedNewFile](https://github.com/skuroda/Sublime-AdvancedNewFile) - File creation plugin
  * [Alignment](https://github.com/wbond/sublime_alignment) - Easy alignment of multiple and multi-line selections
  * [BracketHighlighter](https://github.com/facelessuser/BracketHighlighter) - Bracket and tag highlighter
  * [DocBlockr](https://github.com/spadgos/sublime-jsdocs) - Simplifies writing DocBlock comments
  * [Emmet](https://github.com/sergeche/emmet-sublime) - HTML/CSS workflow enhancement suite
  * [Gist](https://github.com/condemil/Gist) - Create and edit Gists from within Sublime Text
  * [GitGutter](https://github.com/jisaacks/GitGutter) - Adds git diff icons to the gutter
  * [Nettuts+ Fetch](https://github.com/weslly/Nettuts-Fetch) - Fetch remote files and zip packages
  * [Package Control](https://github.com/wbond/sublime_package_control) - Full-featured package manager
  * [Pretty JSON](https://github.com/dzhibas/SublimePrettyJson) - JSON prettifier
  * [SideBarEnhancements](https://github.com/titoBouzout/SideBarEnhancements) - Adds additional functionality to the sidebar
  * [SublimeCodeIntel](https://github.com/Kronuz/SublimeCodeIntel) - Full-featured code intelligence and smart autocomplete engine
  * [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) - Highlight syntax errors


Syntaxes
--------

  * [HTML5](https://github.com/mrmartineau/HTML5) - HTML5 bundle for Sublime Text 2
  * [jQuery](https://github.com/SublimeText/jQuery) - jQuery package bundle
  * [Sass](https://github.com/nathos/sass-textmate-bundle) - Sass support for Sublime Text 2


Settings
--------
```js
{
    "close_windows_when_empty": true,
    "color_scheme": "Packages/Base16 Color Schemes/base16-tomorrow.dark.tmTheme",
    "default_line_ending": "system",
    "drag_text": false,
    "draw_minimap_border": true,
    "font_face": "Ubuntu Mono",
    "font_size": 12,
    "highlight_line": true,
    "highlight_modified_tabs": true,
    "ignored_packages":
    [
        "Vintage"
    ],
    "overlay_scroll_bars": "system",
    "rulers":
    [
        100
    ],
    "shift_tab_unindent": true,
    "tab_size": 4,
    "theme": "Soda Dark.sublime-theme",
    "translate_tabs_to_spaces": true,
    "trim_trailing_white_space_on_save": true,
    "word_wrap": false
}
```

Key Bindings
------------
```js
[
    { "keys": ["ctrl+tab"], "command": "next_view" },
    { "keys": ["ctrl+shift+tab"], "command": "prev_view" },

    { "keys": ["ctrl+alt+n"], "command": "advanced_new_file"},
    { "keys": ["ctrl+shift+alt+n"], "command": "advanced_new_file", "args": {"is_python": true}}
]
```

PHP.sublime-settings
--------------------
```js
{
    "word_separators": "./\\()\"'-:,.;<>~!@#%^&*|+=[]{}`~?"
}

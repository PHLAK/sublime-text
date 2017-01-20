Sublime Text Setup
==================

A list of my Sublime Text packages, settings, and key bindings.

![Sublime Text 3 Screenshot](https://raw.github.com/PHLAK/sublime-text/master/screenshot.png)


Theme, Color Scheme & Font
--------------------------

  * [Theme - Spacegray](https://github.com/kkga/spacegray) (Eighties)
  * [Base16 Color Schemes](https://github.com/chriskempson/base16-textmate) (Base 16 Eighties - Included with Spacegray theme)
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
  * [Package Control](https://github.com/wbond/sublime_package_control) - Full-featured package manager
  * [PHP Companion](https://github.com/erichard/SublimePHPCompanion) - Cool stuff for PHP 5.3+
  * [Pretty JSON](https://github.com/dzhibas/SublimePrettyJson) - JSON prettifier
  * [SideBarEnhancements](https://github.com/titoBouzout/SideBarEnhancements) - Adds additional functionality to the sidebar
  * [Sublime Bookmarks](https://github.com/bollu/sublimeBookmark) - A better bookmark system for SublimeText
  * [SublimeCodeIntel](https://github.com/Kronuz/SublimeCodeIntel) - Full-featured code intelligence and smart autocomplete engine
  * [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) - Highlight syntax errors
  * [SublimeLinter-php](https://github.com/SublimeLinter/SublimeLinter-php) - Highlight PHP syntax errors
  * [WakaTime](https://github.com/wakatime/sublime-wakatime) - Automatic metrics, insights, and time tracking


Syntaxes & Snippets
-------------------

  * [Dockerfile Syntax Highlighting](https://github.com/asbjornenge/Dockerfile.tmLanguage) - Dockerfile syntax highliting
  * [HTML5](https://github.com/mrmartineau/HTML5) - HTML5 bundle for Sublime Text 3
  * [jQuery](https://github.com/SublimeText/jQuery) - jQuery package bundle
  * [Sass](https://github.com/nathos/sass-textmate-bundle) - Sass support for TextMate & Sublime Text (2 & 3)
  * [Laravel Blade](https://github.com/Medalink/laravel-blade) - Syntax definitions for the Laravel 4 & 5 Blade engine
  * [LaravelCollective HTML Form Snippets](https://github.com/PHLAK/laravelcollective-html-form-snippets) - Sublime Text 3 snippets for LaravelCollective/html form elements.


Settings
--------
```js
{
	"always_show_minimap_viewport": true,
	"auto_complete_commit_on_tab": true,
	"bold_folder_labels": true,
	"color_scheme": "Packages/User/SublimeLinter/base16-eighties.dark (SL).tmTheme",
	"default_line_ending": "system",
	"drag_text": false,
	"font_face": "Ubuntu Mono",
	"font_size": 13,
	"highlight_line": true,
	"highlight_modified_tabs": true,
	"ignored_packages":
	[
		"Vintage"
	],
	"line_padding_bottom": 5,
	"line_padding_top": 5,
	"overlay_scroll_bars": "system",
	"rulers":
	[
		80,
		120
	],
	"shift_tab_unindent": true,
	"spacegray_fileicons": true,
	"tab_size": 4,
	"theme": "Spacegray Eighties.sublime-theme",
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
    { "keys": ["ctrl+shift+alt+n"], "command": "advanced_new_file", "args": {"is_python": true}},
    
    { "keys": ["ctrl+alt+u"], "command": "find_use" },
    { "keys": ["ctrl+alt+i"], "command": "import_namespace" },
    { "keys": ["ctrl+alt+f"], "command": "expand_fqcn" },
    { "keys": ["ctrl+alt+g"], "command": "implement" }
]
```

AdvancedNewFile.sublime-settings
--------------------------------
```js
{
    "completion_type": "nix",
    "folder_permissions": "775",
    "file_permissions": "664",
    "warn_overwrite_on_move": true,
    "cursor_before_extension": true
}
```


PHP.sublime-settings
--------------------
```js
{
    "word_separators": "./\\()\"'-:,.;<>~!@#%^&*|+=[]{}`~?"
}
```

Sass.sublime-settings
---------------------
```js
{
    "word_separators": "/\\()\"':,;<>~!%^&*|+=[]{}`~?",
}
```

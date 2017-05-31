Sublime Text Setup
==================

A list of my Sublime Text packages, settings, and key bindings.

![Sublime Text 3 Screenshot](https://raw.github.com/PHLAK/sublime-text/master/screenshot.png)


Theme, Color Scheme & Font
--------------------------

  * [Theme - Spacegray](https://github.com/kkga/spacegray)
  * [Base16 Color Schemes](https://github.com/chriskempson/base16-textmate) (Base 16 Ocean - Included with Spacegray theme)
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
  * [SublimeCodeIntel](https://github.com/Kronuz/SublimeCodeIntel) - Full-featured code intelligence and smart autocomplete engine
  * [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) - Highlight syntax errors
  * [SublimeLinter-php](https://github.com/SublimeLinter/SublimeLinter-php) - Highlight PHP syntax errors
  * [TodoReview](https://github.com/jonathandelgado/SublimeTodoReview) - Review todo (and other) comments within your code.
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
	"caret_style": "phase",
	"color_scheme": "Packages/User/SublimeLinter/base16-ocean.dark (SL).tmTheme",
	"default_line_ending": "system",
	"drag_text": false,
	"ensure_newline_at_eof_on_save": true,
	"font_face": "Ubuntu Mono",
	"font_size": 12,
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
	"show_definitions": false,
	"spacegray_fileicons": true,
	"tab_size": 4,
	"theme": "Spacegray.sublime-theme",
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
    
    { "keys": ["ctrl+insert"], "command": "import_namespace" },
    { "keys": ["ctrl+shift+i"], "command": "find_use" },
    { "keys": ["ctrl+alt+i"], "command": "implement" },
    { "keys": ["ctrl+lagitt+f"], "command": "expand_fqcn" },
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


Base File.sublime-settings (DocBlockr)
--------------------------------------
```js
{
   "jsdocs_align_tags": "shallow",
   "jsdocs_return_description": true,
   "jsdocs_spacer_between_sections": true,
   "jsdocs_per_section_indent": true,
}
```


TodoReview.sublime-settings
--------------------------------------
```js
{
    "patterns": {
        "TODO": "TODO[\\s]*?:[\\s]*(?P<todo>.*)$",
        "NOTE": "NOTE[\\s]*?:[\\s]*(?P<note>.*)$",
        "FIXME": "FIX ?ME[\\s]*?:[\\s]*(?P<fixme>.*)$"
    },
    "patterns_weight": {
    },
    "exclude_folders": [
        "*.git*",
        "*vendor*"
    ],
    "render_include_folder": false,
    "render_header_date": "%A %B %d, %Y at %I:%M %p"
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

Sublime Text Setup
==================

A list of my Sublime Text packages, settings, and key bindings.

![Sublime Text 3 Screenshot](https://raw.github.com/PHLAK/sublime-text/master/screenshot.png)

Look & Feel
-----------

  * **Theme:** [Spacegray](https://github.com/kkga/spacegray)
  * **Color Scheme**: [Base16 Ocean](https://github.com/chriskempson/base16-textmate) (Included with Spacegray theme)
  * **Font:** [Ubuntu Mono](http://font.ubuntu.com/)

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
  * [SublimeLinter-phpcs](https://github.com/SublimeLinter/SublimeLinter-phpcs) - Highlight PHP coding standard issues
  * [SublimeLinter-phpmd](https://github.com/SublimeLinter/SublimeLinter-phpmd) - Highlight potential PHP problems
  * [TodoReview](https://github.com/jonathandelgado/SublimeTodoReview) - Review todo (and other) comments within your code.
  * [WakaTime](https://github.com/wakatime/sublime-wakatime) - Automatic metrics, insights, and time tracking
  * [Xdebug Client](https://github.com/martomo/SublimeTextXdebug) - Xdebug debugger client integration for Sublime Text

Syntaxes & Snippets
-------------------

  * [Dockerfile Syntax Highlighting](https://github.com/asbjornenge/Dockerfile.tmLanguage) - Dockerfile syntax highlighting
  * [HTML5](https://github.com/mrmartineau/HTML5) - HTML5 bundle for Sublime Text 3
  * [jQuery](https://github.com/SublimeText/jQuery) - jQuery package bundle
  * [Sass](https://github.com/nathos/sass-textmate-bundle) - Sass support for TextMate & Sublime Text (2 & 3)
  * [Laravel Blade](https://github.com/Medalink/laravel-blade) - Syntax definitions for the Laravel 4 & 5 Blade engine
  * [LaravelCollective HTML Form Snippets](https://github.com/PHLAK/laravelcollective-html-form-snippets) - Sublime Text 3 snippets for LaravelCollective/html form elements.

Settings
--------

  * Settings can be found in the [config](config) directory.
  * Key mappings can be found in the [keymaps](keymaps) directory.
  * Snippets can be found in the [snippets](snippets) directory.

Install
-------

  1. [Install Sublime Text 3](https://www.sublimetext.com/docs/3/linux_repositories.html)
  2. Start Sublime Text and enable Package Control (`Tools -> Install Package Control...`)
  3. Install packages listed above
  4. Clone the project to your home folder:

     ```
     $ git clone git@github.com:PHLAK/sublime-text.git ~/.sublime-config
     ```

  5. Run the install.py script:

     ```
     $ ~/.sublime-config/install.py
     ```

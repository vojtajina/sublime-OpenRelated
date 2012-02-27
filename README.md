# OpenRelated (Sublime Text 2 plugin)

A plugin for quick navigation between related files (e.g. test/implementation) in awesome text editor - [Sublime Text 2].

## Instalation
Recommended way is using [PackageControll] package.

Or you can download the [tarball] and extract it to your `~/Library/Application Support/Sublime Text 2/Packages/OpenRelated`.

## Configuration
Check out the default configuration: https://github.com/vojtajina/sublime-OpenRelated/blob/master/Preferences.sublime-settings

You can override this configuration per project :-D

````
["*/test/*spec.js", "*/lib/*.js]
````
This pattern maps both directions:

- when editting `/some/test/a.spec.js` file, it will open (if file exists) `/some/lib/a.js`
- when editting `/other/lib/b.js`, it will open `/other/test/b.spec.js`

## Defining key shortcut
By default, "open_related" is mapped to `CMD+T`, however you can easily change that, just add to your keymap preferences:

````
{ "keys": ["super+t"], "command": "open_related" }
````

Note, if you have multiple groups opened (split view), related file will be opened in next group.


[Sublime Text 2]: http://www.sublimetext.com/
[PackageControll]: http://wbond.net/sublime_packages/package_control/installation
[tarball]: https://github.com/vojtajina/sublime-OpenRelated/tarball/master
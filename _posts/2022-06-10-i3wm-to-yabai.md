---
layout: post
title: "Tiling macOS: Moving from i3wm to Yabai"
description: This post is going to give a brief introduction to deep models, the history of object detection ranging from classic methods based on hand-crafted features to the latest deep learning object detectors, object detection datasets, and object detection evaluation metrics.

date: 2022-10-06
assets: assets/posts/2022-10-06-i3wm-to-yabai

authors:
  - name: Steven Lang
    affiliations:
      name: TU Darmstadt


# Below is an example of injecting additional post-specific styles.
# If you use this post as a template, delete this _styles block.
_styles: >
  .fake-img {
    background: #bbb;
    border: 1px solid rgba(0, 0, 0, 0.1);
    box-shadow: 0 0px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 12px;
  }
  .fake-img p {
    font-family: monospace;
    color: white;
    text-align: left;
    margin: 12px 0;
    text-align: center;
    font-size: 16px;
  }
  .center {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
  .small {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 75%;
  }
  .normal {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 100%;
  }
  .video {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 95%;
  }

---

<img class="img-fluid rounded z-depth-2 center normal mb-4" src="{{ site.baseurl }}/{{ page.assets }}/yabai-screenshot.png" data-zoomable>

After using Linux for almost a decade, I've finally gotten annoyed at all the little hiccups and issues that arrive from time to time when working in Linux. ArchLinux has taught me more than anything else about the Linux world, its bleeding edge character, and the issues that come along with it. This has brought me to Fedora Linux about two years ago. While more stable in general, even Fedora has its sharp edges here and there. I've experienced issues with Bluetooth, audio sinks and sources, printers, and more on a daily to weekly basis. After having less and less available time due to my research, constantly tinkering with my system was no longer an option. Therefore, I've decided to finally ditch Linux and give macOS a try. 

My Linux workflow was mainly keyboard-driven, using i3wm as a tiling window manager, Emacs as a programming IDE and as a note-taking tool with [Org mode](https://orgmode.org) and [Org Roam](https://www.orgroam.com), and basically *living* in the terminal. Therefore, my first goal when switching to macOS was to replicate as much as possible of this exact workflow. While finding that (doom) Emacs worked basically out-of-the-box using the `emacs-mac` build (`brew tap railwaycat/emacsmacport brew install emacs-mac --with-modules`) and my Zsh configuration was working without any major changes, finding a workable replacement for i3wm was a much harder task.

## Yabai and skhd to the Rescue!

After fiddling around for a few days, I've settled with a setup that works really well for me: [yabai](https://github.com/koekeishiya/yabai) as a tiling window manager and [skhd](https://github.com/koekeishiya/skhd) to define keyboard shortcuts that perform `yabai` (and some other) commands, replicating most of the functionality that is available in i3wm. In the following, I will go through my yabai and skhd setup and explain how it can replicate the classic i3wm behavior. When giving examples for yabai and skhd commands and configs, these usually go into their respective configuration files at `~/.config/yabai/yabairc` and `~/.config/yabai/yabairc`.

### Open Terminal

For a terminal-focused workflow, it was important to me to have a quick and simple way to open a new terminal instance bound to my preferred shortcut `cmd - return`. [Kitty](https://sw.kovidgoyal.net/kitty/) allows this via the `kitty --single-instance -d ~` arguments. That is, with skhd we can now map `cmd - return` to this exact call:

```sh
cmd - return : kitty --single-instance -d ~
```


If you prefer [iTerm2](https://iterm2.com) over kitty, we can quickly start a new iTerm2 session (as long as there is at least one iTerm2 window already running) with

```sh
cmd - return : osascript -e "tell application \"iTerm2\" to set newSession to create window with default profile end tell"
```
<video class="video mt-4 mb-4 z-depth-2" controls>
  <source src="{{ site.baseurl }}/{{ page.assets }}/open-terminal.mp4" type="video/mp4">
</video>

### Close Window

To quickly close windows, I map `cmd - q` to the specific yabai command:

```zsh
cmd - q : yabai -m window --close
```

<video class="video mt-4 mb-4 z-depth-2" controls>
  <source src="{{ site.baseurl }}/{{ page.assets }}/close-window.mp4" type="video/mp4">
</video>

### Window Focus

Window management in yabai turns out to be pretty similar to i3wm in practice. Yabai allows compass-like focus commands with `yabai -m window --focus <direction>`. I typically use the vim-like keys and bind `h/j/k/l` to `west/south/north/east` respectively as follows:

```zsh
cmd - h : yabai -m window --focus west
cmd - j : yabai -m window --focus south
cmd - k : yabai -m window --focus north
cmd - l : yabai -m window --focus east
```

<video class="video mt-4 mb-4 z-depth-2" controls>
  <source src="{{ site.baseurl }}/{{ page.assets }}/focus-window.mp4" type="video/mp4">
</video>

If you have multiple displays, say next to each other, you can add an alternative command via `||` if the first command fails. That means if the focus is currently on the east-most window, and we call `yabai -m window --focus east`, but there is another display right of your current display, the following will handle switching the display as well:

```zsh
cmd - h : yabai -m window --focus west || yabai -m display --focus west
cmd - l : yabai -m window --focus east || yabai -m display --focus east
```

Similarly, you can switch stacks conditionally, i.e., first try if you can focus the next or previous window in the current stack and if that fails, conditionally focus the next window south/north:
 
```zsh
cmd - j : yabai -m window --focus stack.next || yabai -m window --focus south
cmd - k : yabai -m window --focus stack.prev || yabai -m window --focus north
```

### Move Windows

Similarly, windows can be moved (with my preferred keybinding `cmd + shift - h/j/k/l`):

```zsh
cmd + shift - h : yabai -m window --warp west || yabai -m window --display west
cmd + shift - l : yabai -m window --warp east || yabai -m window --display east
cmd + shift - j : yabai -m window --warp south 
cmd + shift - k : yabai -m window --warp north
```

<video class="video mt-4 mb-4 z-depth-2" controls>
  <source src="{{ site.baseurl }}/{{ page.assets }}/move-window.mp4" type="video/mp4">
</video>


### Spaces

The equivalent of i3wm workspaces in macOS are "Desktops". These can be focused in yabai via the `yabai -m space --focus <label>` command, where `<label>` is a tag you assign in your `yabairc` file:

```zsh
yabai -m space 1 --label 1
yabai -m space 2 --label 2
yabai -m space 3 --label 3
yabai -m space 4 --label 4
yabai -m space 5 --label 5
yabai -m space 6 --label 6
yabai -m space 7 --label 7
yabai -m space 8 --label 8
yabai -m space 9 --label 9
yabai -m space 10 --label 10
```

Then in `skhdrc`, you can use these labels to focus a particular space. Additionally, to simulate the `workspace_auto_back_and_forth yes` setting of i3wm, we can append the command to focus the most recent space if you press the keybinding for the same space again:
```zsh
cmd - 1 : yabai -m space --focus 1 || yabai -m space --focus recent
cmd - 2 : yabai -m space --focus 2 || yabai -m space --focus recent
cmd - 3 : yabai -m space --focus 3 || yabai -m space --focus recent
cmd - 4 : yabai -m space --focus 4 || yabai -m space --focus recent
cmd - 5 : yabai -m space --focus 5 || yabai -m space --focus recent
cmd - 6 : yabai -m space --focus 6 || yabai -m space --focus recent
cmd - 7 : yabai -m space --focus 7 || yabai -m space --focus recent
cmd - 8 : yabai -m space --focus 8 || yabai -m space --focus recent
cmd - 9 : yabai -m space --focus 9 || yabai -m space --focus recent
```

<video class="video mt-4 mb-4 z-depth-2" controls>
  <source src="{{ site.baseurl }}/{{ page.assets }}/focus-space.mp4" type="video/mp4">
</video>

Similar to moving windows around in a specific space, I bind `cmd + shift - <label>` to moving a window to a particular space:
```zsh
cmd + shift - 1 : yabai -m window --space 1
cmd + shift - 2 : yabai -m window --space 2
cmd + shift - 3 : yabai -m window --space 3
cmd + shift - 4 : yabai -m window --space 4
cmd + shift - 5 : yabai -m window --space 5
cmd + shift - 6 : yabai -m window --space 6
cmd + shift - 7 : yabai -m window --space 7
cmd + shift - 8 : yabai -m window --space 8
cmd + shift - 9 : yabai -m window --space 9
```

<video class="video mt-4 mb-4 z-depth-2" controls>
  <source src="{{ site.baseurl }}/{{ page.assets }}/move-window-to-space.mp4" type="video/mp4">
</video>

### Spacebar

As an i3bar replacement, there are several options:

- [simple-bar](https://github.com/Jean-Tinland/simple-bar): A Ubersicht widget, very customizable.
- [spacebar](https://github.com/cmacrae/spacebar): A standalone bar application.

To reserve some space in yabai for the bar, you need to configure the height of the `external_bar` variable in yabai as follows:

```zsh
yabai -m config external_bar all:0:24
```

### Floating Window Settings

Some windows are just not worth floating and you may collect more of those over time. For this, yabai allows to add rules that disable yabai management for specific apps or windows with titles:

```zsh
yabai -m rule --add title='Settings$' manage=off
yabai -m rule --add app="^System Preferences$" manage=off
yabai -m rule --add app="^System Information$" manage=off
yabai -m rule --add title="^Preferences$" manage=off
yabai -m rule --add title="^Digital Colour Meter$" manage=off
yabai -m rule --add title="^General.*" manage=off
```

<video class="video mt-4 mb-4 z-depth-2" controls>
  <source src="{{ site.baseurl }}/{{ page.assets }}/floating-window.mp4" type="video/mp4">
</video>

## Additional Resources

My dotfiles are available [here](https://github.com/steven-lang/dotfiles), including my old [i3wm config](https://github.com/steven-lang/dotfiles/blob/master/configs/i3/.config/i3/config), my new [yabai config](https://github.com/steven-lang/dotfiles/blob/master/configs/yabai/.config/yabai/yabairc), and the [skhd config](https://github.com/steven-lang/dotfiles/blob/master/configs/skhd/.config/skhd/skhdrc).

The yabai GitHub repository also hosts a great [Wiki](https://github.com/koekeishiya/yabai/wiki) that covers everything from installation to configuration. 

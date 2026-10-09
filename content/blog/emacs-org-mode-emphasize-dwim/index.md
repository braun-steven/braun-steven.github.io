---
title: 'Emacs Org Mode: org-emphasize-dwim'
date: '2024-11-15'
slug: emacs-org-mode-emphasize-dwim
# Old URL before switching to Hugo default permalinks
aliases: [/blog/2024/emacs-org-mode-emphasize-dwim/]
description: Add org-emphasize-dwim which wraps org-emphasize and either applies it to the region or to word at pointer.
images:
- org-mode-unicorn.svg
authors: [Steven Braun]
---
<img src="org-mode-unicorn.svg"> 

I use Emacs for programming, note-taking in org-mode, and scientific writing in LaTeX. Org-mode offers a simple function `(org-emphasize &optional CHAR)`, which inserts an emphasis at a point or region and prompts for `CHAR` when called interactively. When I write notes or documentation in org-mode, the usual application of `org-emphasize` is to apply markup such as bold, italic, code, or strikethrough to one or multiple words. Since I'm a previous vim user, I've converted to Emacs via the popular [Doom Emacs](https://github.com/doomemacs/doomemacs) configuration framework, which _emphasizes_ the vim concepts wherever it can. Therefore, my application of `org-emphasize` to regions usually involves first selecting a region with vim motions. In the case of a single word, this breaks down to `ysiw<CHAR>`. Citing tpope's README of [`surround.vim`](https://github.com/tpope/vim-surround): *It's easiest to explain with examples*. Press `ysiw*` (**y**ou **s**urround **i**nner **w**ord) at cursor position `[ ]`: 

```
Hello [W]orld!
```

leads to

```
Hello *[W]orld*!
```

Since I'm heavily relying on `localleader` (keybinding `,`) for Emacs major-mode functionality, I'm inclined to map essential functions to my localleader group. While I could emulate emacs executing normal mode commands such as `ysiw*` for **bold**, `ysiw/` for *italic*, `ysiw=` for `code` and `ysiw~` for ~~strikethrough~~, I think it is more elegant to introduce a **DWIM** wrapper to `org-emphasize`:

```emacs-lisp
(defun sbraun/org-emphasize-dwim (char)
  "DWIM (Do What I Mean) wrapper for org-emphasize.
   If there's an active region, apply emphasis to it.
   Otherwise, apply emphasis to the word at point.
   CHAR is the emphasis character to use."
  (interactive)
  ;; Check if there is an active region (e.g., text is selected).
  (if (use-region-p)
      ;; If a region is active, apply emphasis to the selected region.
      (org-emphasize char)
    ;; Otherwise, apply emphasis to the word at point.
    (save-excursion
      ;; Find the boundaries of the word at point.
      (let ((bounds (bounds-of-thing-at-point 'word)))
        (when bounds
          (goto-char (car bounds))
          (set-mark (cdr bounds))
          ;; Apply emphasis to the selected word.
          (org-emphasize char)
          (deactivate-mark))))))
```

With this defined, I can add keybindings[1], such as

```emacs-lisp
(map! :localleader
      :map org-mode-map
      (:prefix ("t" "text markup")
               :desc "italic" "i" #'(lambda () (interactive) (sbraun/org-emphasize-dwim ?/))
               :desc "bold"   "b" #'(lambda () (interactive) (sbraun/org-emphasize-dwim ?*))
               :desc "code"   "c" #'(lambda () (interactive) (sbraun/org-emphasize-dwim ?=))
               :desc "strike" "s" #'(lambda () (interactive) (sbraun/org-emphasize-dwim ?+))))
```

Back to the original example, pressing `,ti` on:

```org
Hello [W]orld!
```

leads to

```org
Hello /[W]orld/!
```

which saves me ... *drum rolls* ... two keystrokes compared to `ysiw*` -- yay, what a way to procrastinate.

[1] The `map!` syntax is specific to Doom Emacs, see also: [binding-keys](https://github.com/doomemacs/doomemacs/blob/7bc39f2c1402794e76ea10b781dfe586fed7253b/docs/getting_started.org#binding-keys).


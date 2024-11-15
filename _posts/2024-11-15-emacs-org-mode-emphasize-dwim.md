---
layout: post
title: "Emacs Org Mode: org-emphasize-dwim"
description: Add org-emphasize-dwim which wraps org-emphasize and either applies it to the region or to word at pointer.
giscus_comments: true

date: 2024-11-15
assets: assets/posts/2024-11-15-emacs-org-mode-emphasize-dwim
img: assets/posts/2024-11-15-emacs-org-mode-emphasize-dwim/org-mode-unicorn.svg 

authors:
  - name: Steven Braun
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
  .tiny {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 25%;
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

<img class="img-fluid rounded z-depth-0 center tiny mb-4" src="{{ site.baseurl }}/{{ page.assets }}/org-mode-unicorn.svg" data-zoomable> I use Emacs for programming, note-taking in org-mode, and scientific writing in LaTeX. 

Org-mode offers a simple function `(org-emphasize &optional CHAR)`, which inserts an emphasis at a point or region and prompts for `CHAR` when called interactively. When I write notes or documentation in org-mode, the usual application of `org-emphasize` is to apply markup such as bold, italic, code, or strikethrough to one or multiple words. Since I'm a previous vim user, I've converted to Emacs via the popular [Doom Emacs](https://github.com/doomemacs/doomemacs) configuration framework, which _emphasizes_ the vim concepts wherever it can. Therefore, my application of `org-emphasize` to regions usually involves first selecting a region with vim motions. In the case of a single word, this breaks down to `ysiw<CHAR>`. Citing tpope's README of [`surround.vim`](https://github.com/tpope/vim-surround): *It's easiest to explain with examples*. Press `ysiw*` (**y**ou **s**urround **i**nner **w**ord) at cursor position `[ ]`: 

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


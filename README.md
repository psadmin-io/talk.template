# talk.template
Template for talks using [remark](https://github.com/gnab/remark)

# Setup talk from template
```
git clone https://github.com/psadmin-io/talk.NEW.git 
cd talk.NEW
git submodule add https://github.com/psadmin-io/talk.template.git
# set your template branch
git config --file=.gitmodules submodule.talk.template.branch master
git submodule update --init --recursive --remote
python setup.py
```

# Getting started
After running the setup, follow these steps to get started.
1. Find and update markdown files in `/slides`.
    * `class: center, example`
        * Sets style
    * `---`
        * Changes slide
    * `???`
        * Adds speaker notes
1. Update `/index.html` with markdown files to organize slides.
    ```
    var slideshow = remark.create(
      {sourceUrls: [
        // update slides here           
        'slides/intro.md',
        'slides/about.md',
        'slides/close.md',
      ]}
    );
    ```
1. [Serve talk locally](#serve-locally) or publish to GitHub Pages.

# Serve locally
If you are using separate markdown files, they need to be served from a web server. 

Change to the talk's root directory and use the `serve.py` helper script to run a simple web server on port `8000`.
```
cd talk.NEW
python talk.template/serve.py
```

Running directly from command line gives you the option of setting the port number.
```
cd talk.NEW
python3 -m http.server 8003
python2 -m SimpleHTTPServer 8002
```

# Change branch and update
Use these steps to change a template branch or get updates to `remark.js`, css style, example slides, etc.

```
cd talk.NEW
git config --file=.gitmodules submodule.talk.template.branch NEW-BRANCH
git submodule update --init --recursive  --remote
```

# Push template changes upstream
Sometimes you may want to make changes in the template submodule and push upstream. 
```
cd talk.NEW/talk.template
git checkout -b feature/change
# make your changes
git commit -a -m "my change"
git push origin feature/change
```
Do a GitHub PR into `master` or [change your talks.template branch](#change-branch-and-update) as needed. Then update and commit so your talk points to your newly published changes directly.
```
cd talk.NEW
git submodule update --init --recursive --remote
git commit -a -m "updating template"
```

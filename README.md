# talk.template
Template for talks using remark

# Setup talk from template
```
git clone https://github.com/psadmin-io/talk.NEW.git 
cd talk.NEW
git submodule add https://github.com/psadmin-io/talk.template.git
# set your template branch
git config --file=.gitmodules submodule.talk.template.branch master
git submodule update --init --recursive
python setup.py
```

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
git submodule update --init --recursive
```
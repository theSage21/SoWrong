# SoWrong
Slides/Code for [Pycon India 2019 talk](https://in.pycon.org/cfp/2019/proposals/sowrong-absurd-ways-to-do-perfectly-normal-things~bkkXb/)


    Code examples in Python that make you go "This is SO wrong"

The idea is to write common stuff in completely absurd ways. For example, why write APIs like this
```python

@app.get('/my/fancy/url')
def handle_in_a_fancy_fashion():
    return 'hi'
    
```

when you can write them like:

```python

async for request, response in GET('/my/fancy/url'):
    response.body = 'hi'
```
Unlike [WTFPython](https://github.com/satwikkansal/wtfpython), this is not about strange things Python can do. It's about doing normal things in strange ways and understanding why those ways are particularly bad.

Todo
====

- [ ] upload slides on github (once Pycon starts)
- [ ] make code public (once Pycon starts)

<div align="center">
 <h1> Simple Spinner </h1>
 <br>
 It is a way to print a spinning cursor in terminal using Python.  <br />
 I referred <a href="https://stackoverflow.com/questions/4995733/how-to-create-a-spinning-command-line-cursor">this document</a>.<br/><br/>

 "It just Simple Spinning Cursor."
 
<br>
</div>


### **how to use?**

use `start, end` method
```python
spinner = Spinner()
spinner.start(desc='test')
time.sleep(3)
spinner.stop()
```

<br><br>

use `with` reserved word
```python
with Spinner(desc='test'):
    time.sleep(3)
```

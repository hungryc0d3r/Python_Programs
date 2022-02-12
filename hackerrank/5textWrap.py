"""
given a string s and width w.
task is to wrap the string into a paragraph of width w.
"""
# importing textwrap module
import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    return wrapper.fill(text=string)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

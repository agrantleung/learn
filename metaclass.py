'''
from hello_world import Hello
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

h = Hello()
h.hello()
print(type(Hello))
print(type(h))
'''
def fn(self, name= 'world'):
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
print(type(Hello))
print(type(h))


#!/usr/bin/env python3
from curses import wrapper
import operator
import curses


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def hello():
    stack = list()

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        #print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main(stdscr):
    curses.echo()
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.addstr(0, 0, "RPN Calculator\n",curses.color_pair(1) | curses.A_BLINK)
    stdscr.refresh()
    while True:
        stdscr.addstr("Enter Input: ")
        usrInput = stdscr.getstr()
        if usrInput == "quit":
            return
        result = calculate(usrInput)
        stdscr.addstr("Result of (%s) is %d\n" %(usrInput, result), curses.color_pair(2) | curses.A_UNDERLINE )

        
wrapper(main)

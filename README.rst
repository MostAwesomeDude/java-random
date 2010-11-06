===========
Java-Random
===========

Java-Random is a simple implementation of Java's standard java.util.Random
class in Python. Java's random number generation algorithm is exceedingly
straightforward to reimplement in other languages, and this is simply an
implementation for Python.

Installation
============

A standard setup.py is provided.

FAQ
====

Why would you do this?
 I needed this particular generator available in another program, and this was
 the quickest, simplest way to achieve that goal.

What's wrong with Python's random module?
 Nothing. In fact, Python's random module is far superior to this module in a
 number of respects, including predictability, speed, robustness, and
 features. If you're looking for good random number generation in Python, just
 use random instead.

Your code sucks.
 That's not a question. Also, feel free to blame the Java specification for
 that, as they have a very specific way of doing things and I felt that trying
 to spice up my code might lead to some unobvious and unfun bugs.

Where is the official Java specification for this, anyway?
 http://download.oracle.com/javase/6/docs/api/java/util/Random.html, until
 Oracle removes it.

...This is for Minecraft, isn't it?
 No comment.

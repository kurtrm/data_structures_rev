# Revised Data Structures
Repository to house both new and refactored versions of implemented data structures.

I've done some learning over the past few months, and I think it's already time to revisit approaches
to these common data structures.

Below summarizes the data structure. Complexity is the worst case scenario.


To-do:
- Test data-structures against existing implementations for robustness.
- Implement additional data-structures.
- Add CI.
- Incorporate the following where possible:
    - try/except
    - namedtuples
    - generators


## Linked List

- __Parameters__:
    - Accepts an iterable as an optional parameter. 

- __Attributes__:
    - head

- __Methods__:
    - push
    - pop
    - size(len interactive)
    - search
    - remove
    - display(str interactive)

- __Complexity__: O(n)

## Stack

A composition of a linked list that utilizes its pop and push methods.

- __Parameters__:
    - Takes an optional argument of any data type as the value of the node.

- __Attributes__:
    - No public attributes

- __Methods__:
    - push
    - pop
    - len interactive

- __Complexity__: O(n)

## Doubly Linked List

- __Parameters__:
    - Takes no arguments.

- __Attributes__:
    - tail
    - head

- __Methods__:
    - push
    - pop
    - size(len interactive)
    - shift
    - append
    - remove

- __Complexity__: O(n)

## Queue

- __Parameters__:
    - Takes no arguments.

- __Attributes__:
    - tail
    - head

- __Methods__:
    - push
    - pop
    - size(len interactive)
    - shift
    - append
    - remove

- __Complexity__: O(n)

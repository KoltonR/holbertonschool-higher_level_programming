#!/usr/bin/node

class Rectangle {
    /* Rectangle class with 2 args w & h */
    constructor (w, h) {
      const isNonPositiveInt = (w <= 0 || h <= 0);
      const isNotInt = (!Number.isInteger(w) || !Number.isInteger(h));
  
      if (isNonPositiveInt || isNotInt) {
        // If w or h = 0 or not positive ints, create an empty object
      } else {
        this.width = w;
        this.height = h;
      }
    }
  }
  
  module.exports = Rectangle;

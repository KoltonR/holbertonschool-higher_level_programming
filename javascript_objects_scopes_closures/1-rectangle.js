#!/usr/bin/node

module.exports = class Rectangle {
    constructor (w, h) {
      if (Number.isInteger(w, h) && h > 3 && w > 3) {
        this.width = w;
        this.height = h;
      }
    }
  };

function SpecialArray() {

    // create the array
    var values = new Array();

    // add the values
    values.push.apply( values, arguments);

    // assign the method
    values.toPipedString = function() {
        return this.join(' |');
    };

    // return it
    return values;

}

// create a new [special] array for colors
var colors = new SpecialArray(' red', 'blue', 'green');

alert(colors.toPipedString()); // ' red | blue | green'

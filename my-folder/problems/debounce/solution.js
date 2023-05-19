/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timer = null;
  let latestInputs = null;

  return function debounced(...inputs) {
    latestInputs = inputs;

    if (timer) {
      clearTimeout(timer);
    }

    timer = setTimeout(() => {
      fn(...latestInputs);
      timer = null;
      latestInputs = null;
    }, t);
  };
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */
let btn = document.getElementById('btn');
let output = document.getElementById('output');
let quotes = [
    'Life is completely random',
    'Love is stronger',
    'The sea has neither meaning nor pity',
    'Out of difficulties grow miracles',
    'Gotta love animals'
]

btn.addEventListener('click', function(){
    var randomQuote = quotes[Math.floor(Math.random() * quotes.length)]
    output.innerHTML = randomQuote;
})
/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
    
    const combinations = {};
    // Mapping wordRoot to word. For example, '*ot' -> [hot, dot, lot]
    wordList.forEach(word => {
        for (let i = 0; i < word.length; i++) {
            let wordRoot = word.substring(0, i) + '*' + word.substring(i + 1);
            if (combinations[wordRoot] === undefined) {
                combinations[wordRoot] = [];
            }
            combinations[wordRoot].push(word);
        }
    });
    
    let queue = [beginWord];
    let transitions = 0;
    const visitedWords = new Set();
    
    while (queue.length > 0) {
        const neighbors = [];
        
        while (queue.length > 0) {
            let word = queue.pop();
            if (word === endWord) {
                return transitions + 1;
            }
            
            // Consider all roots possible from this word
            for (let i = 0; i < word.length; i++) {
                let wordRoot = word.substring(0, i) + '*' + word.substring(i + 1);
                
                // Consider all words that have the same root
                for (const neighbor of (combinations[wordRoot] || [])) {
                    // If this word has been visited before, continue, else consider it
                    if (!visitedWords.has(neighbor)) {
                        visitedWords.add(neighbor);
                        neighbors.push(neighbor);
                    }
                }
            }
        }
        
        queue = neighbors;
        transitions++;
    }
    
    return 0;// If endWord was found, transitions would've been returned before
    
};

beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
console.log(ladderLength(beginWord,endWord,wordList));
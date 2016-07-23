var TARGET = "George Seed is super cool";
var ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ";
var MUT_PROB = 100;

var generateGenome = function()
    {
    var genome = [];
        for(var i = 0; i<TARGET.length;++i){
            genome[i]=ALPHABET[Math.floor(Math.random()*ALPHABET.length)];
            }
    return genome.join("")

    };


var getFitness = function(genome)
    {
    var fitness = 0;

        for(var i = 0; i<TARGET.length;++i){

            if (genome[i] === TARGET[i]){

                fitness++;

            }

        }
    return fitness
};

var getGenePool = function(genome)
    {
        var genePool = [];
        for(var i = 0; i<500;++i){
            genePool[i] = genome;
            }
    return genePool;

};

var evaluateFitness = function(genePool)
    {
    var highest = 0;
    var index = 0;
        for(var i = 0; i<genePool.length;++i){
            var fitness = getFitness(genePool[i]);

                if (fitness>highest){
                var highest = fitness;
                var index = i;
                }

            }

    return genePool[index];
};

var mutateGenome = function(genome)

    {
    var newGenome = "";
        for(var i = 0; i<genome.length;++i){

                //math.floor gives closest int equal to or small than value
                //math.random gives random value 0-1
                //below gives value 1 in MUT_PROB value (i.e. 10)

            if (Math.floor(Math.random()*MUT_PROB)===1){

                if(genome[i]!=TARGET[i]){
                newGenome+= ALPHABET[Math.floor(Math.random()*ALPHABET.length)];
                }
                else{
                newGenome+= genome[i];
                }
            }
            else{
            newGenome+=genome[i];
            }
        }
    return newGenome;
};

var evolve = function()
    {
        var numGens = 0;
        var fittest = generateGenome();
        console.log(fittest + " (initial seed Gene created)");
            while(getFitness(fittest)!=TARGET.length)
                {
                numGens++;
                // only fittest genome lives to next generation, becomes seed of new genepool
                var pool = getGenePool(fittest);
                var pool2 = [];
                    for (var i=0;i<pool.length;++i){
                    pool2[i]=mutateGenome(pool[i]);
                    }
                fittest = evaluateFitness(pool2);
                if(numGens%10===0){
                    console.log(numGens);
                    console.log(fittest);
                }
            }
        console.log(numGens);
        return console.log(fittest);
};

evolve();

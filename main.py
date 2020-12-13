import random
train = open('./test_data.csv', 'r').read()

test = open('./train_data.csv', 'r').read()

def parseData(file):
    
    init = file.split('\n')

    out = []

    for entry in init:
        output = []
        for idx, value in enumerate( entry.split(',') ):

            if idx == 0:
                output.append(int(value))
                # if int(value) > 40:
                #     output.append(1)
                # else: 
                #     output.append(0)
                # continue

            if value in ['Yes', 'Female', "Positive"]:
                    output.append(1)
            else:
                    output.append(0)
        out.append(output)


    return( out )



        


def dotProduct(vec1, vec2):
    sum = 0
    for i in range(len(vec1)):
        sum += vec1[i] * vec2[i]
    return sum

def addVector(vec1,vec2):
    new = []
    for i in range(len(vec1)):
        new.append( vec1[i] + vec2[i] )
    return new

def subVector(vec1,vec2):
    new = []
    for i in range(len(vec1)):
        new.append( vec1[i] - vec2[i] )
    return new

def genRandomWeights(length):
    return [random.random() for x in range(length)]



def perceptron(file, readjustmentLimit):

    ## last index is if it's true or false
    vecs = parseData(file)


    weights = genRandomWeights( len(vecs[0]) - 1 )

    ogWeight = weights

    readjustments = 0

    while readjustments <= readjustmentLimit:
        for vec in vecs:
            vec_is_positive = vec[-1] == 1
            
            dot_product_with_weight = dotProduct(vec[0:-1], weights)

            classified_as_positive = dot_product_with_weight > 0

            if(classified_as_positive):
                # dp > 0 suggests this was classified as Positive
                if not vec_is_positive:
                    readjustments += 1
                    print('readjusted')

                    weights = subVector(weights, vec[0:-1])

            else:
                # dp < 0 suggests this is Negative
                if vec_is_positive:
                    readjustments += 1
                    print('readjusted')

                    weights = addVector(weights, vec[0:-1])

    return(ogWeight,weights)

def testModel(train_file, test_file, limit):

    (og, new) = perceptron(train_file, limit)

    print(new)

    vecs = parseData(test_file)

    ogCorrect = 0
    newCorrect = 0

    for vec in vecs:

        vec_is_positive = vec[-1] == 1

        dot_product_with_og_weight = dotProduct(vec[0:-1], og)

        dot_product_with_new_weight = dotProduct(vec[0:-1], new)

        if vec_is_positive:

            if(dot_product_with_new_weight > 0):
                newCorrect += 1
            elif dot_product_with_og_weight > 0:
                ogCorrect += 1
        else:
            if(dot_product_with_new_weight <= 0):
                newCorrect += 1
            elif dot_product_with_og_weight <= 0:
                ogCorrect += 1

    print('OG', ogCorrect / len(vecs))
    print('NEW', newCorrect / len(vecs))



testModel(test, train, 30000)







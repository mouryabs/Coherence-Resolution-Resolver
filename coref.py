import spacy
import neuralcoref

## Input: text - string of the text
## Output: modified text 
def coref(text):
    nlp = spacy.load("en_core_web_md")

    neuralcoref.add_to_pipe(nlp)
    doc = nlp(text)
    return doc._.coref_resolved



if __name__ == "__main__":
    text = "Barack Obama is the first president of US. He is from Hawaii and his wife is Michelle"
    print(coref(text))

print(coref("Mourya is good. He is awesome"))

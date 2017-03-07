from document import Document
from category import Category


def get_known_documents(category, path):
    with open(path, 'r') as file:
        known_documents = list()
        texts = file.read().split('###')
        for text in texts:
            known_documents.append(Document(category, text.lower()))
        return known_documents


def get_unknown_document(path):
    with open(path, 'r') as file:
        text = file.read()
        unknown_document = Document(None, text.lower())
        return unknown_document


def categorize_document(unknown_document, k):
    nearest_neighbors = dict()

    for football_document in footballDocuments:
        distance = Document.calculate_tanimoto_distance(unknown_document,
                                                        football_document)
        print(distance)
        if nearest_neighbors.__len__() < k:
            nearest_neighbors[distance] = football_document.category
        else:
            update_neighbors(nearest_neighbors,
                             football_document.category,
                             distance)

    print('\n')

    for python_document in pythonDocuments:
        distance = Document.calculate_tanimoto_distance(unknown_document,
                                                        python_document)
        print(distance)
        if nearest_neighbors.__len__() < k:
            nearest_neighbors[distance] = python_document.category
        else:
            update_neighbors(nearest_neighbors,
                             python_document.category,
                             distance)

    football_documents_count = 0
    python_documents_count = 0

    for value in nearest_neighbors.values():
        if value == Category.Football:
            football_documents_count += 1
        elif value == Category.Python:
            python_documents_count += 1

    if football_documents_count >= python_documents_count:
        document.category = Category.Football
    elif football_documents_count < python_documents_count:
        document.category = Category.Python


def update_neighbors(nearest_neighbors, category, new_distance):
    farthest_neighbor = 2

    for key in nearest_neighbors.keys():
        if key < farthest_neighbor:
            farthest_neighbor = key

    if new_distance > farthest_neighbor:
        del nearest_neighbors[farthest_neighbor]
        nearest_neighbors[new_distance] = category


Document.get_stop_words()

footballDocuments = get_known_documents(
    Category.Football, './football_documents')

for footballDocument in footballDocuments:
    footballDocument.process_document()

pythonDocuments = get_known_documents(
    Category.Python, './python_documents')

for pythonDocument in pythonDocuments:
    pythonDocument.process_document()

document = get_unknown_document('./new_document')

document.process_document()

categorize_document(document, 1)

print()
print('New document is of the category ' + document.category.__str__())
